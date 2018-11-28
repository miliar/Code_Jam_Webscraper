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
int grass[100][100];
int dx[]={1,0,0,-1};
int dy[]={0,1,-1,0};
int main(){
    int tc,n,m,cs=1,c;
    bool flag;
    S(tc);
    FILE *ifp, *ofp;
    char *mode = "r";
    char outputFilename[] = "jam2olarge.txt";
    ofp = fopen(outputFilename, "w");
    while(tc--){
        flag=true;
        S(n);S(m);
        FOR(i,0,n)
            FOR(j,0,m)
                S(grass[i][j]);
        FOR(i,0,n){
            FOR(j,0,m){
                {   c=0;
                    FOR(k,0,n)
                        if(grass[k][j]>grass[i][j]){
                            c++;
                            break;
                        }
                    FOR(k,0,m)
                        if(grass[i][k]>grass[i][j]){
                            c++;
                            break;
                        }
                    //cout<<c<<endl;
                    if(c==2)
                        flag=false;
                }

            }
            if(!flag)
                break;
        }
        if(flag)
            fprintf(ofp,"Case #%d: YES\n",cs++);
        else
            fprintf(ofp,"Case #%d: NO\n",cs++);
    }
}
