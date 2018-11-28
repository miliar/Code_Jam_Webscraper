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

string a;

bool check(int init) {
    int st = init;
    forn(i, a.size()) {
        if (st >= i) {
            st += a[i] - '0';
        } else {
            return false;
        }
    }
    return true;
}

int main() {
#ifdef LOCAL
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    int tt;
    cin >> tt;
    forn(t, tt) {
        int nu;
        cin >> nu;
        cin >> a;
        int l = 0;
        int r = a.size();
        while (l < r) {
            int md = (l + r) / 2;
            if (check(md)) {
                r = md;
            } else {
                l = md + 1;
            }
        }
        cout << "Case #" << t + 1 << ": " << l << endl;
    }
    return 0;
}
