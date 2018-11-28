#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <climits>

using namespace std;

#define rep(i,a,b) for(int i = a; i < b; i++)
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define S(x) scanf("%d",&x)
#define P(x) printf("%d\n",x)

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long LL;

const int MAXN = 1011;
char s[MAXN];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);

    int T;
    S(T);

    rep(t,1,T+1) {
        int n;
        scanf("%d %s",&n,&s);
        //cout<<n<<" "<<s<<"\n";
        LL cnt = 0, ans = 0;
        cnt += s[0]-'0';
        rep(i,1,n+1) {
            if(cnt < i) {
                ans += i-cnt;
                cnt += i-cnt;
            }
            cnt += s[i]-'0';
        }

        printf("Case #%d: %lld\n",t,ans);
    }
    return 0;
}
