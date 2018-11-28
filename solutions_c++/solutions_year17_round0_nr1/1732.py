//made by kuailezhish
//gl && hf
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <unordered_set>
#include <stack>
#include <list>
#include <sstream>
#include <iomanip>
#include <complex>
#include <cstring>
#include <ctime>
#define mem(a,b) memset(a,b,sizeof(a))
#define INF 0x3f3f3f3f
#define lINF 0x3f3f3f3f3f3f3f3fll
#define dINF 1e30
#define eps 1e-8
#define lld long long
#define sqr(x) ((x)*(x))
#define ab(x) (((x)>0) ? (x) : -(x))
#define PI 3.14159265358979323846
#define psl pair<sting,lld>
#define pll pair<lld,lld>
#define pii pair<int,int>
#define mp make_pair
#define er(i) (1ll<<(i))
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define cp complex<double>
#define here printf("!!!!!!!!\n");
#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin(); it != (v).end(); it++)
#define upmin(a,b) {if ((a)>(b)) (a)=(b);}
#define upmax(a,b) {if ((a)<(b)) (a)=(b);}
#define upmod(a,b) (a)=((a)%(b)+(b))%(b)
#define equ(a,b) (fabs(a-b)<eps)
#define rin freopen("in.txt","r",stdin)
#define pout freopen("out.txt","w",stdout)
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;

#define maxn 1100

char st[maxn];
int n, k;

int process() {
    int ans = 0;
    for (int i = 0; i + k <= n; i++) {
        if (st[i] == '+') continue;
        if (st[i] == '-') {
            for (int j = i; j < i + k; j++) {
                st[j] = '+' + '-' - st[j];
            }
            ans++;
        }
    }
    for (int i = n - k; i < n; i++) {
        if (st[i] == '-') return -1;
    }
    return ans;
}

int main() {
    int T, cas;
    freopen("A-large.in", "r", stdin);
    pout;
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas++) {
        //scanf("%s", st);
        scanf("%s", st);
        n = strlen(st);
        scanf("%d", &k);
        int ans = process();
        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        }
        else {
            printf("Case #%d: %d\n", cas, ans);
        }
    }

    return 0;
}