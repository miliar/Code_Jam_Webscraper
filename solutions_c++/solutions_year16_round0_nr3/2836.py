#include <bits/stdc++.h>
#include <windows.h>

#define f first
#define s second
#define ll long long
#define ld long double
#define pb push_back
#define files1 freopen("input.txt","r",stdin)
#define files2 freopen("output.txt","w",stdout)
#define mp make_pair
#define fast_io ios_base::sync_with_stdio(0);
#define forn() for(int i=0;i<n;i++)
#define pii pair<int,int>
#define vi vector<int>

using namespace std;

const int inf=2e9;
const double eps=1e-9;
const int maxn = 1e6;

ll interp(string & s, int base)
{
    ll ans = 0;
    ll st = 1;
    for (int i= s.size() - 1; i >= 0; i--){
        int cur = s[i] - '0';
        ans += 1LL * cur * st;
        st *= 1LL * base;
    }
    return ans;
}

ll find_divisor(ll x)
{
    for (ll i = 2; i * i <= x && i <= maxn; i++){
        if (x % i == 0 && x != i){
            return i;
        }
    }
    return -1;
}
void solve()
{
    int len = 14;
    int cnt = 50;
    set<string> used;

    for (int i=0;i<cnt;i++){
            cerr << i << endl;
        while (1)
        {
            string s;
            s += '1';
            for (int j=0;j<len;j++){
                s += char(rand() % 2 + '0');
            }
            s += '1';
            if (used.count(s))
                continue;

            vector<ll> divisors;
            for (int j=2;j<=10;j++){
                ll x = interp(s, j);// change to BigInt
                ll Divisor = find_divisor(x);//change to BigInt
                if (Divisor == -1){
                    break;
                }
                divisors.pb(Divisor);
            }

            if (divisors.size() != 9)
                continue;
            used.insert(s);
            cout << s << ' ' ;
            for (int j=0;j<divisors.size();j++){
                cout << divisors[j];
                if (j != divisors.size() - 1)
                    cout << ' ';
            }
            cout << "\n";
            break;
        }
    }
}
int main()
{
    srand(time(0));
//    files1;
    files2;
    int t;
    //fast_io;
    //cin.tie(0);
    //cin >> t;
//    for (int i=1;i<=t;i++){
//        printf("Case #%d: ", i);
//        solve();
//    }
    cout << "Case #1:\n";
    solve();
    return 0;
}
