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

#define pb push_back
#define mp make_pair
#define all(x)  (x).begin(),(x).end()
#define tr(c, it)   for(auto it=c.begin(); it!=c.end(); it++)
#define clr(a, b)   memset(a, b, sizeof(a))

int T;
char s[1111];

int main()
{
#ifdef LOCAL
    //freopen("in", "r", stdin);

    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
#endif

    int cas = 1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%s", s);
        int ans = 0;
        int len = strlen(s);

        while(true)
        {
            int p = -1;
            for(int i=len-1; i>=0; i--)
            {
                if(s[i] == '-')
                {
                    p = i;
                    break;
                }
            }

            if(p == -1) break;

            int q = -1;
            for(int i=1; i<len; i++)
                if(s[i] != s[0])
                {
                    q = i;
                    break;
                }

            if(q == -1)
            {
                ans++;
                break;
            }

            ans++;
            for(int i=0; i<q; i++)
                s[i] = s[q];
        }

        printf("Case #%d: %d\n",cas++, ans);


    }

    return 0;
}
