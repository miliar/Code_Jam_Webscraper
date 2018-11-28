#include <cstdio>
#include <vector>
#include <algorithm>

int main()
{
    int t;
    scanf("%d", &t);
    std::vector<int> tab(8);
    for(int ti = 0; ti < t; ++ti) {
        int n;
        scanf("%d", &n);
        --n;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                int x;
                scanf("%d", &x);
                if(i == n) {
                    tab[j] = x;
                }
            }
        }
        scanf("%d", &n);
        --n;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                int x;
                scanf("%d", &x);
                if(i == n) {
                    tab[4 + j] = x;
                }
            }
        }
        std::sort(tab.begin(), tab.begin() + 4);
        std::sort(tab.begin() + 4, tab.end());
        std::vector<int> intersect;
        std::set_intersection(tab.begin(), tab.begin() + 4,
                                                           tab.begin() + 4, tab.end(), std::back_inserter(intersect));
        printf("Case #%d: ", ti + 1);
        if(intersect.size() == 0) {
            printf("Volunteer cheated!\n");
        }else if(intersect.size() > 1) {
            printf("Bad magician!\n");
        }else {
            printf("%d\n", intersect.back());
        }
    }
}

