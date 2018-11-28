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

//#define SMALL
//#define LARGE
//#define test

int main() {
    std::ios::sync_with_stdio(false);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
#ifdef test
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
#endif
    int t;
    cin >> t;
    rep(zz, 1, t + 1) {
        cout << "Case #" << zz << ": ";
        string s;
        cin >> s;
        int n = s.size();
        string t = "";
        t += s[0];
        for(int i = 1; i < n; i++) {
            if(t[0] <= s[i]) t = s[i] + t;
            else t = t + s[i];
        }
        cout << t << endl;
    }
    return 0;
}
