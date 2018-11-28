#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;


#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define ford(i, n) for (int i = int(n); i--; )
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define all(a) (a).begin(), (a).end()

template<class T>
ostream& operator<< (ostream& fout, const vector<T>& vec) {
    for (size_t i = 0; i < vec.size(); ++i) {
        fout << vec[i] << ' ';
    }
    return fout;
}

template <class T>
istream& operator>> (istream& fin, vector<T>& vec) {
    for (size_t i = 0; i < vec.size(); ++i) {
        cin >> vec[i];
    }
    return fin;
}

int check(multiset<int> ds, int t) {
    forn(sp, t) {
        int wk = t - sp;
        int res = 0;
        for (const auto& el : ds) {
            if (el > wk) {
                res += (el + wk - 1) / wk - 1;
            }
        }
        if (res <= sp) {
            return true;
        }
    }
    return false;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tt;
    cin >> tt;
    forn(t, tt) {
        int d;
        cin >> d;
        multiset<int> ds;
        forn(i, d) {
            int cur;
            cin >> cur;
            ds.insert(cur);
        }
        int l = 0;
        int r = *(--(ds.end()));
        while (l < r) {
            int mid = (l + r) / 2;
            if (check(ds, mid)) {
                r = mid;
            } else {
                l = mid+1;
            }
        }
        cout << "Case #" << t + 1 << ": " << l << endl;
        cerr << "is ok? " << check(ds, l) + check(ds, l - 1) << endl;
    }
    return 0;
}
