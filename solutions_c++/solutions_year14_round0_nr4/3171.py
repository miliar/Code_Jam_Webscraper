#include <bits/stdc++.h>

using namespace std;

set<double> ken1, naomi1, ken2, naomi2;

int n;

int descentWar() {
    int result = 0;
    while(!ken1.empty()) {
        set<double>::iterator it1 = naomi1.upper_bound(*ken1.begin());
        if(it1 != naomi1.end()) {
            naomi1.erase(it1);
            ken1.erase(ken1.begin());

            ++result;
        } else {
            set<double>::iterator it2 = ken1.upper_bound(*naomi1.begin());

            ken1.erase(it2);

            naomi1.erase(naomi1.begin());
        }

    }

    return result;
}

int normalWar() {
    int result = 0;
    while(!ken2.empty()) {
        set<double>::iterator it1 = naomi2.upper_bound(*ken2.rbegin());

        if(it1 != naomi2.end()) {
            ++result;
            naomi2.erase(it1);
            ken2.erase(ken2.begin());
        }else{
            set<double>::iterator it2 = ken2.upper_bound(*naomi2.begin());
            naomi2.erase(naomi2.begin());
            ken2.erase(it2);
        }

    }

    return result;
}

int main() {
    freopen("D-large.in", "r", stdin);
     freopen("D-large.out", "w", stdout);

    // ios_base::sync_with_stdio(0);
    // cin.tie(0);

    int t;
    cin >> t;

    for(int t1 = 1; t1 <= t; ++t1) {
        printf("Case #%d: ", t1);

        ken1.clear();
        naomi1.clear();

        ken2.clear();
        naomi2.clear();

        cin >> n;

        double v;


        for(int i = 0; i < n; ++i) {
            cin >> v;
            naomi1.insert(v);
            naomi2.insert(v);

        }
        for(int i = 0; i < n; ++i) {
            cin >> v;
            ken1.insert(v);
            ken2.insert(v);
        }

        printf("%d %d\n", descentWar(), normalWar());

    }

}
