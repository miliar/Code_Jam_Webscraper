
#include "../../lib/include.h"

struct solver {

    solver() {
    }

    void solve(bool process, istream &cin, ostream &cout) {

        int n;
        cin >> n;

        string line;
        getline(cin, line);

        vector<string> lines;
        for (int i = 0; i < n; i++) {
            getline(cin, line);
            lines.push_back(line);
        }

        LOGIC;

        map<string, int> id;
        vector<vector<int> > rep;
        for (int i = 0; i < n; i++) {
            stringstream ss(lines[i]);
            string word;
            vector<int> cur;
            while (ss >> word) {
                int cid = size(id);
                if (id.find(word) != id.end()) {
                    cid = id[word];
                } else {
                    id[word] = cid;
                }

                cur.push_back(cid);
            }
            rep.push_back(cur);
        }

        int m = size(id);
        char *tp = new char[m];

        int mn = INF;
        for (int bm = 0; bm < (1 << (n - 2)); bm++) {
            memset(tp, 0, m);
            int mask = (bm << 2) | 1;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    for (int j = 0; j < size(rep[i]); j++) {
                        tp[rep[i][j]] |= 1;
                    }
                } else {
                    for (int j = 0; j < size(rep[i]); j++) {
                        tp[rep[i][j]] |= 2;
                    }
                }
            }

            int cnt = 0;
            for (int i = 0; i < m; i++) {
                if (tp[i] == 3) {
                    cnt++;
                }
            }

            mn = min(mn, cnt);
        }

        OUTPUT;

        cout << mn << endl;
    }
};

// see https://github.com/SuprDewd/GoogleCodeJamRunner
#include "../../lib/gcj.h"
