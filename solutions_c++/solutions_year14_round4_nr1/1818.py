    #include <bits/stdc++.h>
    using namespace std;
     
    const int MAX_N = 10007;
    int main() {
    int t;
    cin >> t;
     
    for (int cs = 1; cs <= t; ++cs) {
    int n, x;
    cin >> n >> x;
     
    int a [MAX_N];
    multiset <int> s;
    for (int i = 0; i < n; ++i) {
    cin >> a [i];
    s.insert (a [i]);
    }
     
    sort (a, a + n, greater <int> ());
     
    int ans = 0;
    for (int i = 0; i < n; ++i) {
    multiset <int> :: iterator it = s.find (a [i]);
    if (it == s.end ()) continue;
    s.erase (it);
     
    it = s.upper_bound (x - a [i]);
    if (it != s.begin ()) {
    --it;
    s.erase (it);
    }
    ++ans;
    }
     
    cout << "Case #" << cs << ": " << ans << endl;
    }
    return 0;
    }