#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void doIt(vector<double> &naomi, vector<double> &ken, int T) {
    // max size of T is 50, so the following sorts are essentially constant time
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

    // Deceitful War
    int dw_points = 0;
    vector<double> dw_naomi(naomi);
    vector<double> dw_ken(ken);
    while(dw_naomi.size() != 0) {
        if (dw_naomi[dw_naomi.size() -1] > dw_ken[dw_ken.size() -1]) {
            vector<double>::iterator to_erase = dw_naomi.begin();
            while ((to_erase + 1 != dw_naomi.end()) && (*(to_erase) < *(dw_ken.begin()))) {
                ++to_erase;
            }
            dw_naomi.erase(to_erase);
            dw_ken.erase(dw_ken.begin());
            ++dw_points;
        } else {
            dw_naomi.erase(dw_naomi.begin());
            dw_ken.erase((dw_ken.rbegin()+1).base());
        }
    }
    cout << dw_points << ' ';


    // War
    int w_points = 0;
    vector<double> w_naomi(naomi);
    vector<double> w_ken(ken);
    while (w_naomi.size() != 0) {
        if (w_naomi[w_naomi.size() - 1] > w_ken[w_ken.size() - 1]) {
            w_naomi.erase((w_naomi.rbegin()+1).base());
            w_ken.erase(w_ken.begin());
            ++w_points;
        } else {    // else end of ken is larger than end of naomi
            w_naomi.erase((w_naomi.rbegin()+1).base());
            // I can erase the last one becuase naomi always plays largest to smallest
            w_ken.erase((w_ken.rbegin()+1).base());
        }
    }
    cout << w_points;
    
}

int main() {
    int N, T;
    cin >> N;
    for (int i=0; i<N; ++i) {
        cin >> T;
        //cout << "Before T is: " << T << endl;
        vector<double> naomi(T), ken(T);
        for (int j=0; j<T; ++j) {
            scanf("%lf", &naomi[j]);
        }
        for (int j=0; j<T; ++j) {
            scanf("%lf", &ken[j]);
        }
        cout << "Case #" << i+1 << ": ";
        doIt(naomi, ken, T);
        cout << endl;
    }
    return 0;
}
