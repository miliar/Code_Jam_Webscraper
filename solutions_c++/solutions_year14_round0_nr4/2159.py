#include <cstdio>
#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int rt = 1; rt <= T; ++ rt) {
        vector<double> naomi;
        vector<double> ken;
        int n;
        cin >> n;
        double x;
        for (int i = 0; i < n; ++ i) {
            cin >> x;
            naomi.push_back(x);
        }

        for (int i = 0; i < n; ++ i) {
            cin >> x;
            ken.push_back(x);
        }
        sort(naomi.begin(), naomi.end(), greater<double>());
        sort(ken.begin(), ken.end(), greater<double>());

        int k = 0;
        int i = 0, j = n - 1;
        int naomiC = 0;
        while (i <= j) {
            if (naomi[i] > ken[k]) {
                i ++;
                naomiC ++;
            } else {
                if (naomi[j] > ken[k])
                    naomiC ++;
                j --;
            }
            k ++;
        }


        int kenC = 0;
        j = 0, k = n - 1;
        for (int i = 0; i < n; ++ i) {
            if (ken[j] > naomi[i]) {
                kenC ++;
                j ++;
            } else {
                if (ken[k] > naomi[i]) {
                    kenC ++;
                }
                k --;
            }
        }
        cout << "Case #" << rt << ": " << naomiC << " " << n - kenC << endl;
    }
    return 0;
}
