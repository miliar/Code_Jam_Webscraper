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

string s;
int n;

int f() {
    int i = n - 1;
    while(i >= 0 && s[i] == '+') {
        i--;
    }
    return i;
}

void flip(int k) {
    rep(i, 0, k + 1) {
        if(s[i] == '+') s[i] = '-';
        else s[i] = '+';
    }
}

//#define test
int main() {
    ios_base::sync_with_stdio(false);
#ifdef test
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif
    int t;
    cin >> t;
    rep(i, 1, t + 1) {
        cout << "Case #" << i << ": ";
        cin >> s;
        n = s.size();
        ll sum = 0;
        while(f() >= 0) {
            sum++;
            flip(f());
        }
        cout << sum << endl;
    }
    return 0;
}

