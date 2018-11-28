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

void solve() {
    int fn ,sn, a, number;
    cin >> fn;
    set<int> li;
    for (int i = 1 ;i <= 4 ; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> a;
            if (i == fn) {
               li.insert(a);
            }
        }
    }
    int ans  = 0;
    cin >> sn;
    for (int i = 1 ;i <= 4 ; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> a;
            if (i == sn) {
                if (li.find(a) != li.end()) {
                    ans ++;
                    number = a;
                }
            }
        }
    }
    if (ans == 1) {
        cout << number;
    } else if (ans == 0) {
        cout << "Volunteer cheated!";
    } else {
        cout << "Bad magician!";
    }
}

int main() {
    freopen("/Users/KunWang/Downloads/A-small-attempt0.in", "r" , stdin);
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
