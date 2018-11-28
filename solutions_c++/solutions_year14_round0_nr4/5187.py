#include <cstdio>
#include <deque>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
    int T, i, n, j, score1, score2;
    deque<double> naomi1, naomi2, ken1, ken2;
    bool removed[1000];
    double tmp, tmp2;
    scanf("%d", &T);
    for(i = 0; i < T; ++i) {
        scanf("%d", &n);
        memset(removed, 0, sizeof(removed));
        for(j = 0; j < n; ++j) {
            scanf("%lf", &tmp);
            naomi1.push_back(tmp);
            naomi2.push_back(tmp);
        }
        for(j = 0; j < n; ++j) {
            scanf("%lf", &tmp);
            ken1.push_back(tmp);
            ken2.push_back(tmp);
        }
        sort(naomi1.begin(), naomi1.end());
        sort(naomi2.begin(), naomi2.end());
        sort(ken1.begin(), ken1.end());
        sort(ken2.begin(), ken2.end());
        score1 = score2 = 0;
        while(!naomi1.empty()){
            tmp = naomi1.back();
            naomi1.pop_back();
            if(tmp > ken1.back()) {
                ken1.pop_front();
                ++score1;
            } else {
                ken1.pop_back();
            }
        }
        while(!naomi2.empty()){
            tmp = naomi2.front();
            naomi2.pop_front();
            if(ken2[ken2.size()-1] < tmp) {
                score2 += ken2.size();
                ken2.clear();
                naomi2.clear();
            } else if(tmp > ken2.front()) {
                ken2.pop_front();
                ++score2;
            } else {
                ken2.pop_back();
            }
        }
        printf("Case #%d: %d %d\n", i+1, score2, score1);
    }
    return 0;
}
