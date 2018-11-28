#include <iostream>
using namespace std;

#define FOR(i, n) for(int i=0;i<n;i++)
#define FORR(i, n) for(int i=n;i>=0;i--)
#define FOR1(i, n) for(int i=1;i<=n;i++) 
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define ll long long

int main () {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    FOR1(c, t) {
        int ans = 0;
        string s;
        cin >> s;
        FOR1(i, s.length() - 1) if(s[i] != s[i - 1]) ans++;
        if(s.back() == '-') ans++;
        cout << "Case #" << c << ": " << ans << "\n";
    }
}