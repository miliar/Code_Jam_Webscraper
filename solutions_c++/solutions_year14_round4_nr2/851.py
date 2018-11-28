#define TESTCASE true
#define DEBUG false

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <queue>
#include <windows.h>
#include <algorithm>
#define FOR(s,t) for(int s = 0;s < t;s++)
#define PI pair<int,int>
typedef long long ll;

using namespace std;
void print(int i) { printf("%d ",i); }
void print(double i) { printf("%f ",i); }
int abs(int a) { return a<0?-a:a; }
int min(int a,int b) { return a<b?a:b;}
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
void solve()
{
    // START HERE <-----------------------------------------
    int n = getInt();
    int arr[n];
    getArray(arr,n);
    // find the max number
    int maxIndex = 0;
    int copyArr[n];
    for(int i = 0;i < n;i++) copyArr[i] = arr[i];
    sortArrayUp(copyArr,n);
    int left = 0;
    int right = n-1;
    int ans = 0;
    for(int i = 0;i < n;i++) {
        for(int j = 0;j < n;j++) {
            if(copyArr[i] == arr[j]) {
                // check to put right or left
                if(j-left <= right-j) {
                    for(int x = j-1;x >= left;x--) {
                        ans++;
                        int tmp = arr[x];
                        arr[x] = arr[x+1];
                        arr[x+1] = tmp;
                    }
                    left++;
                }
                else{
                    for(int x = j;x < right;x++) {
                        ans++;
                        int tmp = arr[x];
                        arr[x] = arr[x+1];
                        arr[x+1] = tmp;
                    }
                    right--;
                }
                if(DEBUG) {
                    for(int k = 0;k < n;k++) printf("%d ",arr[k]);
                    printf("(%d)\n",ans);
                }
                break;
            }
        }
    }

    printf("%d\n",ans);
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
