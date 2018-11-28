#define debug if(0)
// Grzegorz Guspiel
#include <bits/stdc++.h>
using namespace std;
 
#define REP(i,n) for(int i=0;i<int(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define ALL(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define st first
#define nd second

template<typename T> void maxE(T& a, const T& b) { a = max(a, b); }
template<typename T> void minE(T& a, const T& b) { a = min(a, b); }

istream& operator>>(istream& in, vector<vector<int> >& t) {
    REP (i, 4) {
        t.pb(vector<int>());
        REP (j, 4) {
            int a; cin >> a;
            t.back().pb(a);
        }
    }
    return in;
}

template<typename T>
ostream& operator<<(ostream& out, vector<T>& t) {
    out << "[";
    FOREACH (i ,t) out << *i << ", ";
    out << "]";
    return out;
}

int main() {
    ios_base::sync_with_stdio(0);
	int z; cin >> z;
    for (int zz = 1; zz <= z; zz++) {
        vector<vector<int> > t1, t2;
        int r1; cin >> r1; r1--;
        cin >> t1;
        int r2; cin >> r2; r2--;
        cin >> t2;
        debug cout << "r1 " << r1 << " r2 " << r2 << endl;
        debug cout << "t1 " << t1 << endl << "t2 " << t2 << endl;
        sort(ALL(t1[r1]));
        sort(ALL(t2[r2]));
        vector<int> is(100);
        is.resize(set_intersection(ALL(t1[r1]), ALL(t2[r2]), is.begin()) - is.begin());
        cout << "Case #" << zz << ": ";
        if (SIZE(is) == 1) {
            cout << is[0]; 
        } else if (SIZE(is) > 1) {
            cout << "Bad magician!";
        } else {
            cout << "Volunteer cheated!";
        }
        cout << endl;
	}
	return 0;
}
