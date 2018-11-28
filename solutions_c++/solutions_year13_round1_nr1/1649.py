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

#define unsigned long long int ulli
# define FRm(i, m, n)     for( int i = m; i <=n; i++)
# define FRrev(i, n)         for( int i = n; i >= 0; i-- )
# define FRrevm(i,n,m)         for( int i = n; i >= m; i-- )
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
using namespace std;
int main(){
    int tc,cs=1,r,t;
    lli sum,c;
    bool flag;
    S(tc);
    lli arr[1000];
    FILE *ifp, *ofp;

    char outputFilename[] = "codejamoutput.txt";
    ofp = fopen(outputFilename, "w");
    while(tc--){
        S(r);S(t);
        c=0;
        sum=0;
        while(sum<=t){
            sum+=(((r+1)*(r+1))-((r)*(r)));
            //cout<<sum<<endl;
            r+=2;
            c++;
        }
        fprintf(ofp,"Case #%d: %lld\n",cs++,c-1);
        cout<<c-1<<endl;
    }
    fclose(ofp);
}
