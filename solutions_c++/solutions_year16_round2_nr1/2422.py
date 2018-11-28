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

#define test

int main() {
    std::ios::sync_with_stdio(false);
#ifdef test
	freopen("A-large.in","rt",stdin);
	freopen("a.out","wt",stdout);
#endif
    int tt;
    cin >> tt;
    rep(zz, 1, tt + 1) {
        cout << "Case #" << zz << ": ";
        string st;
        cin >> st;
        vector<char> s;
        vector<int> v;
        int n = st.size();
        rep(i, 0, n) s.pb(st[i]);
        string tmp;
        while(find(all(s), 'Z') != s.end()) {
            s.erase(find(all(s), 'Z'));
            s.erase(find(all(s), 'E'));
            s.erase(find(all(s), 'R'));
            s.erase(find(all(s), 'O'));
            v.pb(0);
        }
        while(find(all(s), 'W') != s.end()) {
            s.erase(find(all(s), 'T'));
            s.erase(find(all(s), 'W'));
            s.erase(find(all(s), 'O'));
            v.pb(2);
        }
        while(find(all(s), 'X') != s.end()) {
            s.erase(find(all(s), 'S'));
            s.erase(find(all(s), 'I'));
            s.erase(find(all(s), 'X'));
            v.pb(6);
        }
        while(find(all(s), 'G') != s.end()) {
            s.erase(find(all(s), 'E'));
            s.erase(find(all(s), 'I'));
            s.erase(find(all(s), 'G'));
            s.erase(find(all(s), 'H'));
            s.erase(find(all(s), 'T'));
            v.pb(8);
        }
        while(find(all(s), 'U') != s.end()) {
            s.erase(find(all(s), 'F'));
            s.erase(find(all(s), 'O'));
            s.erase(find(all(s), 'U'));
            s.erase(find(all(s), 'R'));
            v.pb(4);
        }
        while(find(all(s), 'F') != s.end()) {
            s.erase(find(all(s), 'F'));
            s.erase(find(all(s), 'I'));
            s.erase(find(all(s), 'V'));
            s.erase(find(all(s), 'E'));
            v.pb(5);
        }
        while(find(all(s), 'S') != s.end()) {
            s.erase(find(all(s), 'S'));
            s.erase(find(all(s), 'E'));
            s.erase(find(all(s), 'V'));
            s.erase(find(all(s), 'E'));
            s.erase(find(all(s), 'N'));
            v.pb(7);
        }
        while(find(all(s), 'O') != s.end()) {
            s.erase(find(all(s), 'O'));
            s.erase(find(all(s), 'N'));
            s.erase(find(all(s), 'E'));
            v.pb(1);
        }
        while(find(all(s), 'H') != s.end()) {
            s.erase(find(all(s), 'T'));
            s.erase(find(all(s), 'H'));
            s.erase(find(all(s), 'R'));
            s.erase(find(all(s), 'E'));
            s.erase(find(all(s), 'E'));
            v.pb(3);
        }
        while(find(all(s), 'I') != s.end()) {
            s.erase(find(all(s), 'N'));
            s.erase(find(all(s), 'I'));
            s.erase(find(all(s), 'N'));
            s.erase(find(all(s), 'E'));
            v.pb(9);
        }
        sort(all(v));
        rep(i, 0, v.size()) cout << v[i];
        cout << endl;
    }
    return 0;
}
