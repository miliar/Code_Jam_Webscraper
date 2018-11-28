#include<bits/stdc++.h>
#define rep(i,k,n) for(int i= (int) k;i< (int) n;i++)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;
const int limit = 1048576;
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
//     cin.tie(0);
    int T; cin >> T;
    rep(t, 1, T + 1)
    {
        int k, c, s; cin >> k >> c >> s;
        cout << "Case #" << t << ": ";
        rep(i, 1, k + 1)
            cout << i << " ";
        cout << "\n";
    }
    return 0;
}