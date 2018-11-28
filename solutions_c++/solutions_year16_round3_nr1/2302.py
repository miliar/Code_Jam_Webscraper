#include<iostream>
#include<queue>
#include<vector>
#include<stack>
#include<string>
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<map>
#include<fstream>

using namespace std;

#define pb   push_back
#define mp   make_pair
#define s    second
#define ll   long long
#define For(i,j,n)  for(int (i) = (j); i < n; i++)
#define MAX(a, b)     ((a) > (b) ? (a) : (b))
#define MIN(a, b)     ((a) < (b) ? (a) : (b))
#define Max INT_MAX
#define Min INT_MIN
#define mod 1000000007

void printArray(int *a,int n){
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

void generateRandomArray(int *a,int n){
    for(int i=0;i<n;i++){
        a[i] = rand()%100;
    }
}

void generateSortedArray(int *a,int n){
    for(int i=0;i<n;i++){
        a[i] = rand()%100;
    }
    sort(a,a+n);
}
void generateLinearArray(int *a,int n){
    For(i,1,n+1){
        a[i-1]=i*2;
    }
    return;
}

void swapNo(int *a,int *b){
    int temp = *a;
    *a=*b;
    *b=temp;
    return;
}

ll power(ll base, ll exp) {
    ll r=1;
    while(exp>0) {
       if(exp%2==1) r=(r*base)%mod;
       base=(base*base)%mod;
       exp/=2;
    }
    return r%mod;
}

bool isPossible(int *a){
    for(int i=0;i<26;i++){
        if(a[i]>0){
            return true;
        }
    }
    return false;
}

bool comp(const pair<int, char>&i, const pair<int, char>&j){
    return i.first < j.first;
}

int main(){
    ifstream in;
    ofstream out;
    in.open("test.txt");
    out.open("result.txt");

    int cases;
    in>>cases;
    int cas=1;
    while(cas<=cases){
        int n,people=0;
        in>>n;
        pair<int, char> parties[n];

        for(int i=0;i<n;i++){
            in>>parties[i].first;
            parties[i].second = (char)('A'+i);
            people+=parties[i].first;
        }
        out<<"Case #"<<cas<<": ";
        while(people>0){
            sort(parties,parties+n,comp);
            if(parties[n-1].first==parties[n-2].first&&parties[n-1].first!=parties[n-3].first){
                people-=2;
                parties[n-1].first--;
                parties[n-2].first--;
                out<<parties[n-1].second<<parties[n-2].second<<" ";
            }else{
                people--;
                parties[n-1].first--;
                out<<parties[n-1].second<<" ";
            }
        }
        out<<endl;
        cas++;
    }
    return 0;
}
