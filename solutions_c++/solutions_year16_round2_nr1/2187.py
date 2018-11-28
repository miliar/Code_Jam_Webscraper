#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pl;

#define sl(x) scanf("%I64d",&x)
#define pl(x) printf("%I64d\n",x)
#define sf(x) sort(x.begin(),x.end(),func)
#define s(x) sort(x.begin(),x.end())
#define all(v) v.begin(),v.end()
#define rs(v) { s(v) ; r(v) ; }
#define r(v) {reverse(all(v));}
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define f(i,n) for(int i=0;i<n;i++)
#define rep(i,a,b) for(int i=a;i<=b;i++)

const ll mod = 1000000007;
const ll inf = LLONG_MAX;
const ll ninf = LLONG_MIN;
const ld eps = 1e-12;
const ll N = 1000005;
const ll M = 5005;
const ll LOGN = 19;

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	ll t;
	cin >> t;
	ll id = 1;
	while(t--)
    {
        string s;
        cin >> s;
        ll n = s.size();
        ll cnt[30] = {};
        cout << "Case #" << id++ << ": ";
        f(i, n)
        {
            cnt[s[i] - 'A']++;
        }
        ll ans[11] = {};
        ans[0] = cnt['Z' - 'A'];
        cnt['O' - 'A'] -= ans[0];
        ans[2] = cnt['W' - 'A'];
        cnt['T' - 'A'] -= ans[2];
        cnt['O' - 'A'] -= ans[2];
        ans[8] = cnt['G' - 'A'];
        cnt['T' - 'A'] -= ans[8];
        ans[6] = cnt['X' - 'A'];
        cnt['S' - 'A'] -= ans[6];
        ans[7] = cnt['S' - 'A'];
        cnt['N' - 'A'] -= ans[7];
        cnt['V' - 'A'] -= ans[7];
        ans[3] = cnt['T' - 'A'];
        ans[5] = cnt['V' - 'A'];
        cnt['F' - 'A'] -= ans[5];
        ans[4] = cnt['F' - 'A'];
        cnt['O' - 'A'] -= ans[4];
        ans[1] = cnt['O' - 'A'];
        cnt['N' - 'A'] -= ans[1];
        ans[9] = cnt['N' - 'A'] / 2;
        f(i, 10)
        {
            f(j, ans[i])
            {
                cout << i;
            }
        }
        cout << "\n";
    }
    return 0;
}
