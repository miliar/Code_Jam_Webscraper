#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main () {
    int T;
    scanf("%d", &T);
    int t, n;
    for (t = 1; t <= T; t++) {
        scanf("%d", &n);
        int i, j;
        double a;

        vector<double> naomi;
        vector<double> ken;

        for (i = 0; i < n; i++) {
            scanf("%lf", &a);
            naomi.push_back(a);
        }
        for (i = 0; i < n; i++) {
            scanf("%lf", &a);
            ken.push_back(a);
        }

        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        
        // Optimal Deceitful War   
        i = j = 0;
        while (i < n && j < n) {
            while (j < n && naomi[j] < ken[i]) j++;
            if (j < n) {
                i++;
                j++;
            }
        }
        int score1 = i;
    
        // Optimal War
        i = j = 0;
        while (i < n && j < n) {
            while (j < n && ken[j] < naomi[i]) j++;
            if (j < n) {
                i++;
                j++;
            }
        }
        int score2 = n - i;
        printf("Case #%d: %d %d\n", t, score1, score2);
    }
}
