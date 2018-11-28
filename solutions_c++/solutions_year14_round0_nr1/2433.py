#include<iostream>
#include<cstdio>
#include<algorithm>
#include<memory.h>
#include<vector>
#include<stack>
#include<queue>
#include<cassert>
#include<cstdlib>
#include<cmath>
#include<map>
#include<utility>
#include<cstring>

#define DEBUG(x) cout<<#x<<"= "<<x<<endl
#define DEBUGARR(x,i,f) for(int iter = i; iter <= f; ++iter) printf("%s[%d]=%d\n",#x, iter, x[iter])
#define MAX(a,b) ((a)>(b))? (a):(b)
#define MAX3(a,b,c) MAX(a,MAX(b,c))
#define MIN(a,b) ((a)<(b))? (a):(b)
#define MIN3(a,b,c) MIN(a,MIN(b,c))
#define bit(n,i) (n&(1<<(i-1)))
#define setbit(n,i) n |= (1<<(i-1))
#define inf (1<<30)
#define SETZERO(x) memset( x, 0, sizeof(x))
#define SETMIN1(x) memset( x, -1, sizeof(x))
#define CLEAR(x) while(!x.empty()) x.pop();
#define FOR(i,in,fin) for( i = (in); i <= (fin); ++i)
#define FORL(i,in,fin) for( i = (in); i < (fin); ++i)
#define FORD(i,in,fin) for( i = (in); i >= (fin); --i)
#define INC(a,b,c) ((a)<=(b) && (b)<=(c))
#define pb push_back
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d\n",x)
#define sll(x) scanf("%lld",&x)
#define pll(x) printf("%lld\n",x)
#define sortv(v) sort(v.begin(),v.end())
#define sortar(a,i,n) sort(a+i,a+i+n)
#define findmp(mp,x) (mp.find(x)!=mp.end())
typedef long long ill;
using namespace std;
typedef pair <int,int> pii;
const int mod = 1000000007;
//code begins here
int main()
{
    #ifndef ONLINE_JUDGE
        freopen( "a.in", "r", stdin);
        freopen("a.out","w",stdout);
    #endif
    int t,test_case;
    scanf("%d",&t);
    FOR(test_case,1,t)
    {
        int a1,a2,ar1[5],ar2[5],i,j,tmp;
        si(a1);
        FOR(i,1,4){
            FOR(j,1,4)
            if(i==a1){
                si(ar1[j]);
            }
            else
                si(tmp);
        }
        si(a2);
        FOR(i,1,4){
            FOR(j,1,4)
            if(i==a2){
                si(ar2[j]);
            }
            else
                si(tmp);
        }
        vector <int> ans;
        FOR(i,1,4){
            FOR(j,1,4){
                if(ar1[i]==ar2[j]){
                    ans.pb(ar1[i]);
                }
            }
        }
        printf("Case #%d: ",test_case);
        if(ans.size()==0){
            printf("Volunteer cheated!\n");
        }
        else
        if(ans.size()==1){
            pi(ans[0]);
        }
        else
            printf("Bad magician!\n");
    }
}


