#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;


void alg() {
    int N;
    cin >> N;
    
    int war(0), dwar(0);
    
    list<double> naomi, ken;
    
    for (int i(0); i < N; ++i) {
        double n;
        cin >> n;
        naomi.push_back(n);
    }
    for (int i(0); i < N; ++i) {
        double n;
        cin >> n;
        ken.push_back(n);
    }
    naomi.sort();
    ken.sort();
    
    // dwar
    list<double>::reverse_iterator nit = naomi.rbegin();
    list<double>::reverse_iterator kit = ken.rbegin();
    while (kit != ken.rend()) {
        if (*nit > *kit) {
            ++dwar;
            ++nit;
        }
        ++kit;
    }
    
    // war
    while (!ken.empty()) {
        if (ken.front() > naomi.front()) {
            naomi.pop_front();
        }
        ken.pop_front();
    }
    war = naomi.size();
    
    cout << dwar << " " << war << endl;
}

int main() {
    int n_cases(0);
    cin >> n_cases;
    
    for (int test_case = 1; test_case <= n_cases; test_case++) {
      cout << "Case #" << test_case << ": ";
      alg();
    }

    return EXIT_SUCCESS;
}
