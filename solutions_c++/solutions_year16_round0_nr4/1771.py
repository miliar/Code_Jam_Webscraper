#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define vi vector<int>
#define all(c) c.begin(), c.end()
#define pb push_back
#define f first
#define s second
#define mod 1000000007
#define inf 1e9
#define pl pair<ll,ll>
#define pii pair<pi,pi>
#define f first
#define mp make_pair
#define s second
#define rep(i,a,n) for(int i=a;i<n;i++)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);i--)
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())

//#define test
int main() {
    ios_base::sync_with_stdio(false);
#ifdef test
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("D-small-attempt0.out", "wt", stdout);
#endif
    int t;
    cin >> t;
    rep(zz, 1, t + 1) {
        cout << "Case #" << zz << ": ";
        ll k, c, s;
        cin >> k >> c >> s;
        for(int i = 1; i <= k; i++) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
