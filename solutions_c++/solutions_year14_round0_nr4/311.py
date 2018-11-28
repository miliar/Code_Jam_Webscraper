#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        int N;
        cin >> N;
        vector<double> naomi(N);
        vector<double> ken(N);
        for (int i = 0; i < N; ++i)
            cin >> naomi[i];
        for (int i = 0; i < N; ++i)
            cin >> ken[i];

        // War
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        int points_ken = 0;
        int num = 0;
        for (int i = 0; i < naomi.size(); ++i) {
            int cur = naomi[i];
            while (num < ken.size() && ken[num] < naomi[i])
                num++;
            if (num < ken.size()) {
                num++;
                points_ken++;
            }
        }
        int points = 0;
        num = 0;
        for (; num < N; ++num) {
            if (naomi.back() > ken.back()) {
                points++;
                naomi.pop_back();
                ken.pop_back();
                continue;
            }
            ken.pop_back();
            naomi.erase(naomi.begin());
        }
        cout << points << " " << N - points_ken;
        cout << endl;
    }
}
