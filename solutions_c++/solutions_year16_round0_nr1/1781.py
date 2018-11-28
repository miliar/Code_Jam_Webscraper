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

bool a[10];

void make(ll n) {
    ll m = n;
    while(m) {
        a[m % 10] = true;
        m /= 10;
    }
}

bool ok() {
    for(int i = 0; i < 10; i++) {
        if(a[i] == false) return false;
    }
    return true;
}

//#define test
int main() {
    ios_base::sync_with_stdio(false);
#ifdef test
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif
    int t;
    cin >> t;
    rep(i, 1, t + 1) {
        memset(a, false, sizeof(a));
        cout << "Case #" << i << ": ";
        ll n;
        cin >> n;
        if(n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        ll ne = n;
        make(ne);
        ll m = 2;
        while(!ok()) {
            ne = n * m;
            m++;
            make(ne);
        }
        cout << ne << endl;
    }
    return 0;
}

