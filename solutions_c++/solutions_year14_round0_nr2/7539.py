#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long ll;

const double esp = 1E-8;

inline int dlcmp(double x) {
    return x < -esp ? -1 : (x > esp ?  1 : 0);
}

void solve() {
    double C, F, X, ans;
    cin >> C >> F >> X;
    if (C >= X) {
        printf("%0.7lf", (X/2));
        return ;
    }
    double last = X/2, now, sum;
    for (int i = 0; ; i++) {
        sum += C / (F*i + 2.0);
        now = X/(2.0 + F*(i+1)) + sum;
        if (dlcmp(now - last) > 0) {
            printf("%0.7lf", last);
            return ;
        }
        last = now;
    }
}

int main() {
    freopen("/Users/KunWang/Downloads/B-small-attempt0.in", "r" , stdin);
    //
    freopen( "/Users/KunWang/Downloads/small.out",  "w",stdout);
    int T , cas = 0;
    cin >> T;
    while(T--) {
         cas ++;
         cout << "Case #"<<cas <<": ";
         solve();
         cout << endl;
    }
    return 0;
}
