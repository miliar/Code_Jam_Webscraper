#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

int get_deceitful(list<double> la, list<double> lb) {
    int ans = 0;
    while (!la.empty()) {
        double x = la.front();
        //printf(" x= %d", x);
        la.pop_front();
        if (x > lb.front()) {
            ++ans;
            lb.pop_front();
        }
        else {
            lb.pop_back();
        }
    }
    return ans;
}

int get_war(list<double> la, list<double> lb) {
    int ans = 0;
    while (!la.empty()) {
        double x = la.front();
        la.pop_front();
        if (x > lb.back()) {
            ++ans;
            lb.pop_front();
        }
        else {
            for (list<double>::iterator it=lb.begin(); it != lb.end(); ++it) {
                if ((*it) > x) {
                    lb.remove(*it);
                    break;
                }
            }
        }
    }
    return ans;
}

string solve() {
    int n;
    cin >> n;
    double x;
    list<double> la, lb;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        la.push_back(x);
    }
    for (int i = 0; i < n; ++i) {
        cin >> x;
        lb.push_back(x);
    }
    la.sort();
    lb.sort();

    int r1 = get_deceitful(la, lb);
    int r2 = get_war(la, lb);
    return to_string(r1) + " " + to_string(r2);
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: %s\n", i, solve().c_str());
    }
    return 0;
}
