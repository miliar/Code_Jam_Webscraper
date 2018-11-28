/*
    TanTr!k.$aX
*/

using namespace std;
#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<utility>
#include<climits>
#include<sstream>

#define unsigned long long int ulli
#define FRm(i, m, n)     for( int i = m; i <=n; i++)
#define FRrev(i, n)         for( int i = n; i >= 0; i-- )
#define FRrevm(i,n,m)         for( int i = n; i >= m; i-- )
#define max(a,b) ((a)>(b)?(a):(b))
#define S(a) scanf("%d",&(a))
#define P(a) printf("%d",(a))
#define min(a,b) ((a)<(b)?(a):(b))
#define NL printf("\n")
#define sqr(a) ((a)*(a))
#define SL(a) scanf("%lld",&(a))
#define PL(a) printf("%lld",(a))
#define lli long long int
#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define inarrd(arr,n) for(int i=0;i<n;i++)S(arr[i]);
#define outarrd(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PF(" ");}NL;
#define outarrN(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PFN;}
int n,mn;
int a[105];
void counter(int i,int c,int curr){
    if(i==n){
        mn=min(c,mn);
        return;
    }
    if(curr>a[i])
        counter(i+1,c,curr+a[i]);
    else{
        counter(i,c+1,curr+curr-1);
        counter(i+1,c+1,curr);
    }
}
int main(){
    int tc,cs=1,mote,c,curr;
    freopen("C:\\Users\\tantrik\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\tantrik\\Desktop\\output.txt","w",stdout);
    S(tc);
    while(tc--){
        mn=INT_MAX;
        c=0;
        S(mote);S(n);
        curr=mote;

        for(int i=0;i<n;i++)
            scanf("%d",a+i);
        sort(a,a+n);
        /*for(int i=0;i<n;i++){
            if(curr<=a[i]){
                if(curr+curr-1>a[i])
                    curr+=curr-1+a[i];
                c++;
            }
            else
                curr+=a[i];
        }*/
        if(mote==1)
            mn=n;
        else
        counter(0,0,mote);
        printf("Case #%d: %d\n",cs++,mn);
    }
}
