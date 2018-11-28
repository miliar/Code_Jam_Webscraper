#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <iterator>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cassert>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int N;
        cin >> N;
        string uniq, s;
        vector<vi> cnts(N);
        cin >> s;
        char c = 0;
        int k = -1;
        for (int i=0; i<s.size(); ++i) {
            if (s[i] != c) {
                c = s[i];
                ++k;
                uniq.push_back(c);
                cnts[0].push_back(1);
            } else {
                cnts[0][k]++;
            }
        }
        for (int j=1; j<N; ++j) {
            s = "";
            cin >> s;
            c = 0;
            k = -1;
            for (int i=0; i<s.size(); ++i) {
                if (s[i] != c) {
                    c = s[i];
                    ++k;
                    if (k>=uniq.size() || c != uniq[k]) {
                        // cerr << "Case #" << cs << " s[" << i << "] = " << c <<" != " << "uniq[" << k << "] = " << uniq[k] << endl;
                        cout << "Case #" << cs << ": Fegla Won\n";
                        goto case_done;
                    }
                    cnts[j].push_back(1);
                } else {
                    cnts[j][k]++;
                }
            }
            if (k!=uniq.size()-1) {
                cout << "Case #" << cs << ": Fegla Won\n";
                goto case_done;
            }
        }

        {
            int res=0;
            for (int col=0; col<uniq.size(); ++col) {
                vi cc(N);
                for (int i=0; i<N; ++i) cc[i] = cnts[i][col];
                sort(cc.begin(), cc.end());
                int m = cc[cc.size()/2];
                for (int j=0; j<N; ++j) {
                    res += abs(cc[j]-m);
                }
            }
            cout << "Case #" << cs << ": " << res << "\n";
        }
      case_done:
        ;
    }
}
