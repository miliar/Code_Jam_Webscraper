
#include <bits/stdc++.h>

using namespace std;

void tc() {
    static int c = 1;
    cout << "Case #" << c++ << ": ";
    int N, X;
    cin >> N >> X;
    multiset<int> files;
    for (int i = 0; i < N; ++i) {
        int size;
        cin >> size;
        files.insert(size);
    }
    multiset<pair<int, int> > combs;
//    cerr << "combs.." << endl;
//    for (auto it = files.begin(); it != files.end(); ++it) {
//        for (auto it2 = it; (++it2) != files.end() && (*it + *it2 <= X);) {
//            assert(max(*it, *it2) == *it2);
//            combs.insert(make_pair(*it + *it2, *it2));
//        }
//    }
//    cerr << combs.size() << endl;
//    cerr << "loop.." << endl;
    int r = 0;
    while (files.size() > 0) {
        auto it = files.end();
        --it;
        ++r;
        int last = *it;
        files.erase(it);

        it = files.upper_bound(X - last);
        if (it != files.begin()) {
            --it;
            cerr << last << ',' << *it << endl;
            files.erase(it);
        } else
        cerr << last << endl;
    }

//    for (auto it = combs.end(); it != combs.begin();) {
//        --it;
//
//        ++r;
//        int a = it->second;
//        int b = it->first - a;
//        cerr << a << ',' << b << "; ";
//
//        files.erase(files.find(a));
//        for (auto p = files.begin(); p != files.end() && (a + *p <= X); ++p) {
//            auto it2 = combs.find(make_pair(a + *p, max(a, *p)));
//            assert(it2 != combs.end());
//            if (it == it2) {
//                it = combs.erase(it2);
//            } else {
//                combs.erase(it2);
//            }
//        }
//    cerr << combs.size() << endl;
//        files.erase(files.find(b));
//        for (auto p = files.begin(); p != files.end() && (b + *p <= X); ++p) {
//            auto it2 = combs.find(make_pair(b + *p, max(b, *p)));
//            assert(it2 != combs.end());
//            if (it == it2) {
//                it = combs.erase(it2);
//            } else {
//                combs.erase(it2);
//            }
//        }
//    cerr << combs.size() << endl;

//        if (it == combs.begin()) break;
//    }
//    r += files.size();
    cout << r << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) tc();
}
