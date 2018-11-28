#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <iterator>
#include <sstream>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        set<int> fr;
        int f;
        cin >> f;
        for (int i=1; i<=4; ++i) {
            int t;
            if (i==f) {
                for (int j=0; j<4; ++j) {
                    cin >> t;
                    fr.insert(t);
                }
            } else {
                for (int j=0; j<4; ++j) {
                    cin >> t;
                }
            }
        }

        set<int> sr;
        int s;
        cin >> s;
        for (int i=1; i<=4; ++i) {
            int t;
            if (i==s) {
                for (int j=0; j<4; ++j) {
                    cin >> t;
                    sr.insert(t);
                }
            } else {
                for (int j=0; j<4; ++j) {
                    cin >> t;
                }
            }
        }

        vi sol;
        for (set<int>::const_iterator it=fr.begin(); it!=fr.end(); ++it)
            if (sr.count(*it)) sol.push_back(*it);
        cout << "Case #" << cs << ": ";
        switch (sol.size()) {
            case 1:
                cout << sol[0];
                break;
            case 0:
                cout << "Volunteer cheated!";
                break;
            default:
                cout << "Bad magician!";
                break;
        }
        cout << "\n";
    }
}
