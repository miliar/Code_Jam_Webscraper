#include <bits/stdc++.h>

using namespace std;

template<typename U, typename T>
int go(T a, T b) {
    vector<int> v(a, b);
    U c;
    int r = 0;
    for (int i = 0; i < v.size(); ++i) {
        bool g = false;
        for (int j = v.size() - 1; j-- > i; ) {
            if (c(v[j+1], v[j])) {
                swap(v[j], v[j+1]);
                ++r;
                g = true;
            }
        }
        if (!g) break;
    }
    return r;
}
template<typename T>
int cn(vector<T>& v) {
    vector<int> u;
    for (pair<int, int> x : v) u.push_back(x.second);
    return go<less<int>>(u.begin(), u.end());
    int r = 0;
    for (int i = 0; i < v.size(); ++i) {
        r += abs(v[i].second - i);
    }
//    cerr << r << endl;
    return r/2;
}

template<typename U, typename T>
int go_(T a, T b) {
    vector<pair<int, int> > v(b-a);
    for (int i = 0; a != b; i++) v[i] = make_pair(*a++, i);
    sort(v.begin(), v.end(), U());
    return cn(v);
}

template<typename T>
bool ud(vector<T>& v) {
    bool st = false;
    T el = v[0];
    for (int i = 1; i < v.size(); ++i) {
        T e2 = v[i];
        if ((e2 < el) != st) {
            if (st) return false;
            else st = true;
        }
        el = e2;
    }
    return true;
}

void tc() {
    static int cas = 1;
    cout << "Case #" << cas++ << ": ";
    int N;
    cin >> N;
#if 0
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];
    int r = INT_MAX;
    for (int i = 0; i <= N; ++i) {
        r = min(r, go<less<int>>(a.cbegin(), a.cbegin() + i) + go<greater<int>>(a.cbegin() + i, a.cend()));
    }
    cout << r << endl;
#else
    vector<pair<int, int>> a(N);
    for (int i = 0; i < N; ++i) { cin >> a[i].first; a[i].second = i; }
    sort(a.begin(), a.end());
    int r = INT_MAX;
    do {
        if (ud(a)) {
            //for (int i = 0; i < N; ++i) cerr << a[i].first << ' ';
            //cerr << endl;
            r = min(r, cn(a));
        }
    }while (next_permutation(a.begin(), a.end()));
    cout << r << endl;
#endif
}

int main() {
    int T;
    cin >> T;
    while (T--) tc();
}
