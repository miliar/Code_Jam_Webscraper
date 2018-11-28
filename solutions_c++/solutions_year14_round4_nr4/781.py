#define TESTCASE true
#define DEBUG false

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <queue>
#include <algorithm>
#define FOR(s,t) for(int s = 0;s < t;s++)
#define PI pair<int,int>
typedef long long ll;

using namespace std;
void print(int i) { printf("%d ",i); }
void print(double i) { printf("%f ",i); }
int getInt() {
    int a;
    scanf("%d",&a);
    return a;
}
double getDouble() {
    double a;
    scanf("%lf",&a);
    return a;
}

void getArray(int *arr,int size) { for(int i = 0;i < size;i++) arr[i] = getInt(); }
void getArray(double *arr,int size) { for(int i = 0;i < size;i++) arr[i] = getDouble(); }

int sortMinToMax(const void* a,const void* b){ return *((int*)a) - *((int*)b); }
int sortMaxToMin(const void* a,const void* b){ return *((int*)b) - *((int*)a); }

void sortArrayUp(int* arr,int n){ qsort(arr,n,sizeof(int),sortMinToMax); } /* Min -> Max */
void sortArrayDown(int* arr,int n){ qsort(arr,n,sizeof(int),sortMaxToMin); } /* Max -> Min */

template<class t>
t* array(int N) { return (t*)calloc(sizeof(t),N); }

int M,N;
int worstNode,worstCnt;
void check(vector<string> serv[])
{
    int allNode = 0;
    for(int i = 0;i < N;i++) {
        if(serv[i].size() == 0) return;
        int cntThis = 0;
        // count trie tree for this server i
        for(int j = 0;j < serv[i].size();j++) {
            if(j==0) {
                // create full trie tree
                cntThis += serv[i][j].size();
            }
            else {
                int forkMin = serv[i][j].size();
                for(int k = 0;k < j;k++) {
                    // try fork from this (k)
                    bool allPass = true;
                    for(int l = 0;l < serv[i][k].size();l++) {
                        if(serv[i][j].size() <= l) {
                            forkMin = 0;
                            allPass = false;
                            break;
                        }
                        else if(serv[i][k][l] != serv[i][j][l]) {
                            forkMin = min(forkMin,int((serv[i][j].size())-l));
                            allPass = false;
                            break;
                        }
                    }
                    if(allPass == true) {
                        forkMin = min(forkMin,int(serv[i][j].size()-serv[i][k].size()));
                    }
                    if(forkMin == 0) break;
                }
                cntThis += forkMin;
            }
        }
        allNode += cntThis + 1;
        /*cout << i << " ";
        for(int j = 0;j < serv[i].size();j++) {
            cout << serv[i][j] << " ";
        }
        cout << endl;*/
    }
    if(allNode > worstNode) {
        worstNode = allNode;
        worstCnt = 1;
    }
    else if(allNode == worstNode) worstCnt++;

    //system("pause");
}
void recur(int strNow,vector<string> strList,vector<string> serv[])
{
    if(strNow >= M) {
        check(serv);
        return;
    }
    for(int i = 0;i < N;i++) {
        string addStr = strList[strNow];
        serv[i].push_back(addStr);
        recur(strNow+1,strList,serv);
        serv[i].pop_back();
    }
}
void solve()
{
    // START HERE <-----------------------------------------
    worstNode = worstCnt = 0;
    M = getInt();
    N = getInt();
    vector<string> strList;
    vector<string> servList[N];
    for(int i = 0;i < M;i++) {
        string tmp;
        cin >> tmp;
        strList.push_back(tmp);
    }
    recur(0,strList,servList);
    printf("%d %d\n",worstNode,worstCnt);
}

int main()
{
    if(TESTCASE) {
        int t,tt;
        scanf("%d",&tt);
        for(t=0;t < tt;t++)
        {
            printf("Case #%d: ",t+1);
            solve();
        }
    } else {
        solve();
    }
}
