#include <iostream>
#include <string>
#include <array>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <iomanip>
#include <sstream>


using namespace std;

struct employee {
    long long numActive = 0LL;
    bool isActive = false;
    long long salary;
    employee* parent;
    vector<long long> children;
};
long long t, n, d, s0, as, cs, rs, m0, am, cm, rm;
employee* ceo;
employee employees[1000005];
vector<pair<long long, long long> > salaries;

void activate(long long i) {
    employees[i].isActive = true;
    employees[i].numActive++;
    employee* cur = employees + i;
    while (cur->parent != NULL) {
        cur = cur->parent;
        cur->numActive += employees[i].numActive;
        if (!cur->isActive) {
            return;
        }
    }
}

void deactivate(long long i) {
    employees[i].isActive = false;
    employee* cur = employees + i;
    while (cur->parent != NULL) {
        cur = cur->parent;
        cur->numActive -= employees[i].numActive;
        if (!cur->isActive) {
            break;
        }
    }
    employees[i].numActive--;
}

int main() {
    cin >> t;
    for (long long test = 1; test <= t; test++) {
        salaries.clear();
        cin >> n >> d >> s0 >> as >> cs >> rs >> m0 >> am >> cm >> rm;
        employees[0].salary = s0;
        employees[0].parent = NULL;
        ceo = employees;
            salaries.push_back(make_pair(s0, 0LL));
        long long curSal = s0, curMan = m0;
        // cout << s0 << " " << -1 << endl;
        for (long long i = 1; i < n; i++) {
            curSal = (curSal * as + cs) % rs;
            curMan = (curMan * am + cm) % rm;
            employees[i].salary = curSal;
            employees[i].parent = employees + (curMan % i);
            employees[curMan % i].children.push_back(i);
            salaries.push_back(make_pair((long long)curSal, (long long)i));
            // cout << curSal << " " << (curMan % i) << endl;
        }
        // cout << endl;
        // for (long long i = 0; i < salaries.size(); i++) {
        //     cout << salaries[i].first << " " << salaries[i].second << endl;
        // }
        std::sort(salaries.begin(), salaries.end());
        // cout << endl;
        // for (long long i = 0; i < n; i++) {
        //     cout << salaries[i].first << " " << salaries[i].second << endl;
        // }
        long long end = 0, max = 0;;
        for (long long i = 0; i < n; i++) {
            while (end < n && salaries[end].first <= salaries[i].first + d) {
                activate(salaries[end].second);
                end++;
            }
            // cout << employees[0].salary << endl;
            // cout << i  << " " << end << " " << salaries[end - 1].first << " " <<salaries[i].first << " " << salaries[end - 1].second << endl;
            // for (long long j = 0; j < n; j++) {
            //     cout << employees[j].numActive << " ";
            // }
            // cout << endl << endl;
            if (ceo->isActive && ceo->numActive > max) {
                max = ceo->numActive;
            }
            deactivate(salaries[i].second);
        }
            cout << "Case #" << test << ": " << max << endl;
    }
}