#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef ONLINE_JUDGE
#define dbg(x) cerr << __LINE__ << " : " << #x << " = " << (x) << endl;
#else
#define dbg(x)
#endif

#define ff first
#define ss second

void solve(){
    int n, len; cin >> n >> len;
    set<string> good;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        good.insert(s);
    }
    string bad; cin >> bad;
    if (good.find(bad) != good.end()) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    if (len == 1){
        cout << "0 ?" << endl;
        return;
    }
    string OZ = "10";
    string s1, s2;
    s1 += OZ;
    s1 += '?';
    for (int i = 0; i < 49; i++){
        s1 += OZ;
    }
    s2 = string(len - 1, '?');
    cout << s1 << ' ' << s2 << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }


    return 0;
}
