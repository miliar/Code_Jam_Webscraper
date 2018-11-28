#include <algorithm>
#include <stack>
#include <bitset>
#include <cassert>
#include <map>
#include <string>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))
#define REP(i,n) for(int (i) = 0; (i) < (n); ++(i))
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define square(a) (a)*(a)
#define mp(a,b) make_pair((a),(b))

const int oo = numeric_limits<int>::max();

int main() {
    int T, r1, r2, tmp;
    set<int> s1, s2;
    vector<int> v;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        s1.clear(); s2.clear(); v.clear();
        v.resize(10);
        cin >> r1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> tmp;
                if (i+1 == r1)
                    s1.insert(tmp);
            }
        }
        cin >> r2;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> tmp;
                if (i+1 == r2)
                    s2.insert(tmp);
            }
        }
        vector<int>::iterator it = set_intersection(all(s1), all(s2), v.begin());
        v.resize(it-v.begin());
        int count = v.size();

        cout << "Case #" << t << ": ";
        if (count == 1)
            cout << *v.begin();
        else if (count == 0)
            cout << "Volunteer cheated!";
        else
            cout << "Bad magician!";
        cout << endl;
    }
}
