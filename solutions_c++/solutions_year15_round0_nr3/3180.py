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

const int MAXN = 10011;
char s[MAXN];

int m[5][5] = { {0, 0, 0, 0, 0},
                {0, 1, 2, 3, 4},
                {0, 2,-1, 4,-3},
                {0, 3,-4,-1, 2},
                {0, 4, 3,-2,-1}
};

int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("csmall.out","w",stdout);
    /*rep(i,1,5) {
        rep(j,1,5) cout<<m[i][j]<<" ";
        cout<<"\n";
    }*/
    int T;
    S(T);

    rep(t,1,T+1) {
        int l,x;
        scanf("%d %d\n%s",&l,&x,&s);
        //cout<<l<<" "<<x<<" "<<s<<"\n";
        bool seen1 = false, seen2 = false;

        int tot = l*x, cmul = 1;
        rep(i,0,tot) {
            int idx = i%l;
            char c = s[idx];
            int y = c-'g';

            int sign = 1;
            if(cmul < 0) sign = -1;
            cmul = m[abs(cmul)][y];
            cmul *= sign;
            //if(t!=5) cout<<cmul<<" ";
            if(!seen1 && cmul == 2) seen1 = true;
            if(seen1 && !seen2 && cmul == 4) {
                seen2 = true;
            }
        } //cout<<"\n";

        printf("Case #%d: ",t);
        if(seen1 && seen2 && cmul == -1) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
