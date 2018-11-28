#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int T, N;
    double tmp;

    std::cin >> T;
    for (int i=0; i < T; ++i) {
        int war_win = 0, deceitful_win = 0;
        std::vector<double> naomi, ken, naomi_copy, ken_copy;
        std::cin >> N;

        for (int j=0; j < N; ++j) {
            std::cin >> tmp;
            naomi.push_back(tmp);
        }
        std::sort(naomi.rbegin(), naomi.rend());
        naomi_copy = naomi;
        for (int j=0; j < N; ++j) {
            std::cin >> tmp;
            ken.push_back(tmp);
        }
        std::sort(ken.rbegin(), ken.rend());
        ken_copy = ken;

        for (int j=0; j < N; ++j) {
            // play War
            if (naomi_copy.front() > ken_copy.front()) {
                naomi_copy.erase(naomi_copy.begin());
                ken_copy.pop_back();
                ++war_win;
            } else {
                naomi_copy.erase(naomi_copy.begin());
                ken_copy.erase(ken_copy.begin());
            }

            // play deceitful war
            if (naomi.front() > ken.front()) {
                naomi.erase(naomi.begin());
                ken.erase(ken.begin());
                ++deceitful_win;
            } else if (naomi.back() < ken.front()) {
                // lie
                naomi.pop_back();
                ken.erase(ken.begin());
            } else {
                naomi.pop_back();
                ken.pop_back();
                ++deceitful_win;
            }
        }
        
        printf("Case #%d: %d %d\n", i+1, deceitful_win, war_win);
    }

    return 0;
}
