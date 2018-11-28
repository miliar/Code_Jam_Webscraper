/* sjsakib  */ 
#include <bits/stdc++.h>

#define stream istringstream
#define rep(i,n) for(int i=0; i<(int)n; i++)
#define repv(i,n) for(int i=n-1; i>=0; i--)
#define repl(i,n) for(int i=1; i<=(int)n; i++)
#define replv(i,n) for(int i=n; i>=1; i--)


#define INF (1<<28)
#define PI 3.141592653589793238462643383279502
#define pb(x) push_back(x)
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x))
#define eps 1e-9
#define pii pair<int,int>
#define vi vector<int>
#define pmp make_pair


#define sdi(x) scanf("%d",&x)
#define sdii(x,y) scanf("%d%d",&x,&y)
#define sdc(x) scanf("%c",&x)
#define SDs(x) scanf("%s",x)
#define uu first
#define vv second

using namespace std;

//template<class T> T power(T N,T P){ return (P==0)?  1: N*power(N,P-1); }

int  power(int a,int n) {
    return (n==0)?1:a*power(a,n-1);
}

typedef long long i64  ;
typedef unsigned long long ui64  ;

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)



int main() {
    READ("in");
    WRITE("out");
    int t;
    sdi(t);
    rep(i,t) {
        int k,c,s;
        sdii(k,c);
        sdi(s);
        if(s<k-1 || (c==1 && s<k)) {
            printf("Case #%d: IMPOSSIBLE\n",i+1);
        } else if(c == 1) {
            printf("Case #%d:",i+1);
            for(int j = 1;j<=k;j++) {
                printf(" %d",j);
            }
            printf("\n");
        } else if(k==1) {
            printf("Case #%d: 1\n",i+1);
        } else  {
            printf("Case #%d:",i+1);
            for(int j = 2;j<=k;j++) {
                printf(" %d",j);
            }
            printf("\n");
        }
    }
    return 0;
}