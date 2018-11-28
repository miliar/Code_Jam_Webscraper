#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <utility>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;
int war_ken;
int war_naomi;
int dwar_ken;
int dwar_naomi;
vector<double> ken;
vector<double> naomi;

void solve_war(vector<double> a, vector<double> b) {
    bool found;
    int i;
    while (a.size() != 0) {
        found = false;
        for (i = 0; i < b.size(); i++) {
            if (a[0] > b[i]) {
                found = true;
                war_ken++;
                b.erase(b.begin() + i);
                break;
            }
        }
        vector<double>::iterator it = a.begin();
        a.erase(it);
        if (found != true) {
            war_naomi++;
        }
    }
}

void solve_dwar(vector<double> b, vector<double> a) {
    bool found;
    int i;
    while (b.size() != 0) {
        found = false;
        for (i = 0; i < a.size(); i++) {
            if (b[0] > a[i]) {
                found = true;
                dwar_naomi++;
                a.erase(a.begin() + i);
                break;
            }
        }
        vector<double>::iterator it = b.begin();
        b.erase(it);
        if (found != true) {
            dwar_ken++;
        }
    }
}

int main() {
    int i, t, cases = 1, n;
    double x;
    scanf("%d", &t);
    while (cases <= t) {
        naomi.clear();
        ken.clear();
        war_ken = war_naomi = 0;
        dwar_ken = dwar_naomi = 0;
        scanf("%d", &n);
        for (i = 1; i <= n; i++) {
            scanf("%lf", &x);
            naomi.push_back(x);
        }
        for (i = 1; i <= n; i++) {
            scanf("%lf", &x);
            ken.push_back(x);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        solve_war(ken, naomi);
        solve_dwar(naomi, ken);
        printf("Case #%d: %d %d\n", cases, dwar_naomi, war_naomi);
        cases++;
    }
    return 0;
}

