#include <iostream>
#include <map>
#include <set>
#include <bitset>
#include <string>
#include <algorithm>
using namespace std;
vector<string> split(string s) {
    string tmp = "";
    vector<string> res;
    for (int i=0; i<s.length(); i++) {
        if (s[i] == ' ') {
            res.push_back(tmp);
            tmp = "";
        } else tmp += s[i];
    }
    if (tmp != "") res.push_back(tmp);
    return res;
}
int main() {
    ios_base::sync_with_stdio(0);
    int T, N;
    cin >> T;
    for (int t=1; t<=T; t++) {
        cin >> N;
        vector<string> v[N];
        vector<int> vi[N];
        map<string, int> id;
        int cnt = 1;
        for (int i=0; i<N; i++) {
            string ss;
            getline(cin, ss);
            while (ss.length() == 0) getline(cin, ss);
            v[i] = split(ss);
            for (string &s: v[i]) {
                if (id[s] == 0) id[s] = cnt++;
                vi[i].push_back(id[s]);
            }
        }
        bitset<3000> vb[N];
        for (int i=0; i<N; i++)
            for (int x: vi[i])
                vb[i][x] = 1;
        int res = 1e9;
        bitset<3000> a;
        bitset<3000> b;
        for (int i=0; i<(1<<(N-2)); i++) {
            a.reset();
            b.reset();
            for (int x: vi[0]) a[x] = 1;
            for (int x: vi[1]) b[x] = 1;
            for (int j=2; j<N; j++) {
                if (i & (1<<(j-2))) {
                    for (int x: vi[j]) a[x] = 1;
                } else {
                    for (int x: vi[j]) b[x] = 1;
                }
            }
            a &= b;
            res = min(res, (int)a.count());
        }
        cout << "Case #" << t << ": " << res << "\n";
    }
    return 0;
}
