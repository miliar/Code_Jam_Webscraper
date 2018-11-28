#include <cassert>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define debug(args...) {vector<string> _v = split(#args, ','); err(_v.begin(), args); puts("");}
vector<string> split(const string& s, char c) {vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.emplace_back(x); return move(v);}
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) {cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; err(++it, args...);}

#define PB push_back
#define mp make_pair
#define all(x)  (x).begin(),(x).end()
#define tr(c, it)   for(auto it=c.begin(); it!=c.end(); it++)
#define clr(a, b)   memset(a, b, sizeof(a))

int T;
int n, k;
double p[222];
double dp[222][222];

vector<double> candi;

double fun(int pre, int last)
{
    candi.clear();
    for (int i = 0 ; i < pre ; ++i) candi.PB(p[i]);
    int l= last;
    for (int j = n - 1 ; l; --j , --l) candi.PB(p[j]);
    clr(dp, 0);




    dp[1][1] = candi[0];
    dp[1][0] = 1. - candi[0];
    for (int i = 1 ; i < k ; ++i){
        for (int j = 0 ; j <= i ; ++j){
            dp[i + 1][j + 1] += dp[i][j] * candi[i];
            dp[i + 1][j] += dp[i][j] * (1. - candi[i]);
        }
    }
    return dp[k][k / 2];
}

int main()
{
#ifdef LOCAL
    //freopen("in", "r", stdin);

    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
#endif

    int cas = 1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n, &k);
        for(int i=0; i<n; i++)
        {
            cin >> p[i];
        }

        sort(p, p+n);

        double ans = 0;
        for(int pre=0; pre<=k; pre++)
        {
            int last = k - pre;
            ans = max(ans, fun(pre, last));
        }
        printf("Case #%d: %.10lf\n",cas++, ans);

    }
    return 0;
}
