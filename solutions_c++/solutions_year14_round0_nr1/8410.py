#include<cstdio>
using namespace std;

int tab[17], numbers[4];

int main() {
    int tests;
    scanf("%d", &tests);
    for(int t=1; t<=tests; ++t) {
        int row;
        scanf("%d", &row);
        for(int i=1; i<=4; ++i) {
            for(int j=0; j<4; ++j)
                scanf("%d", &numbers[j]);
            if(row == i)
                for(int j=0;j<4; ++j)
                    tab[numbers[j]]=t;
        }
        scanf("%d", &row);
        int poss =0 , ans;
        for(int i=1; i<=4; ++i) {
            for(int j=0; j<4; ++j)
                scanf("%d", &numbers[j]);
            if(row == i)
                for(int j=0; j<4; ++j)
                    if(tab[numbers[j]] == t) {
                        ++poss;
                        ans = numbers[j];
                    }
        }
        printf("Case #%d: ", t);
        if(poss == 1) printf("%d\n", ans);
        else if(poss == 0) printf("Volunteer cheated!\n");
            else printf("Bad magician!\n");
    }
    return 0;
}
