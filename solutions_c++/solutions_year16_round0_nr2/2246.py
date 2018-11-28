#include <bits/stdc++.h>
using namespace std;
/* macros */
// memory
#define zeroset(A) memset((A), 0, sizeof((A)))
#define negset(A) memset((A), -1, sizeof((A)))
#define all(c) (c).begin(), (c).end()
#define pb push_back
// input & output
#define inpt(a) freopen(a,"r",stdin)
#define otpt(a) freopen(a,"w",stdout)
#define eol "\n"
// types
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<ll,ll> pll;
#define ff first
#define ss second
// constants
#define EPS 1e-9
#define MAXN 300005
#define INF INT_MAX
#define MOD 1000000007

int pan[MAXN];

int main()
{
    //ios::sync_with_stdio(false);
    //inpt("sample.in");
    inpt("B-large.in");
    otpt("large_B.out");
    int T;
    //scanf("%d", &T);
    cin >> T;
    for(int ts = 1; ts<=T; ++ts){
        string s;
        cin >> s;
        for(int i = 0; i<s.size(); ++i){
            if(s[i] == '+') pan[i] = 1;
            else pan[i] = 0;
        }
        int f = 0, i=s.size() - 1, ans = 0;
        while(i >= 0){
            while(i>=0 && pan[i]^f == 1) i--;
            if(i>=0){
                while(i>=0 && pan[i]^f == 0) i--;
                f = (++ans) % 2;
            }
        }
        printf("Case #%d: %d\n", ts, ans);
    }
    return 0;
}
