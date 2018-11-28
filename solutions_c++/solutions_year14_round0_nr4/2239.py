#include <cstdio>
#include <vector>
#include <algorithm>

typedef double Real;

std::vector<Real> ken;
std::vector<Real> naomi;

int standard() {
    int score = 0;
    Real used = 0.0;
    for(unsigned int i = 0; i < naomi.size(); ++i) {
        std::vector<Real>::iterator it =
                std::upper_bound(ken.begin(), ken.end(), std::max(naomi[i], used));
        if(it == ken.end()) {
            score++;
        }else {
            used = *it;
        }
    }
    return score;
}

int deceitful() {
    int score = 0;
    int kp = 0;
    for(unsigned int i = 0; i < naomi.size(); ++i) {
        if(naomi[i] > ken[kp]) {
            score++;
            kp++;
        }
    }
    return score;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int ti = 0; ti < t; ++ti) {
        int n;
        scanf("%d", &n);
        ken.resize(n);
        naomi.resize(n);
        for(int i = 0; i < n; ++i) {
            scanf("%lf", &naomi[i]);
        }
        for(int i = 0; i < n; ++i) {
            scanf("%lf", &ken[i]);
        }
        std::sort(ken.begin(), ken.end());
        std::sort(naomi.begin(), naomi.end());
        int r1 = standard();
        int r2 = deceitful();
        printf("Case #%d: %d %d\n", ti + 1, r2, r1);
    }
}
