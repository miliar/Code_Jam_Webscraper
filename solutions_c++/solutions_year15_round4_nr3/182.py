#include <iostream>
#include <vector>
#include <map>
#include <unordered_set>
#include <string>
#include <iterator>
#include <sstream>
#include <bitset>

using namespace std;

int main() {
    ios::sync_with_stdio(false);

    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> n >> ws;

        vector<vector<string>> v(n);
        vector<vector<size_t>> ws(n);

        map<string, int> id;

        for (int i = 0; i < n; i++) {
            string line;
            getline(cin, line);
            istringstream iss(line);
            copy(istream_iterator<string>(iss), istream_iterator<string>(), back_inserter(v[i]));

            for (string w : v[i]) {
                if (id.count(w) == 0) {
                    int nid = id.size();
                    id[w] = nid;
                }
                ws[i].push_back(id[w]);
            }
        }

        size_t ans = v[0].size() + v[1].size();

        for (int ss = 0; ss < (1 << n); ss++) {
            if ((ss & 0b11) != 0b01) {
                continue;
            }

//            cerr << "trying " << ss << '\n';

            bitset<1 << 12> words[2];

            for (int i = 0; i < n; i++) {
                for (const auto& w : ws[i]) {
                    int lang = (ss & (1 << i)) > 0;
//                    cerr << w << " " << lang << endl;
                    words[lang].set(w);
                }
            }

            ans = min(ans, (words[0] & words[1]).count());
        }

        cout << "Case #" << tc << ": " << ans << '\n';
    }

    return 0;
}
