#include <cstdio>

using namespace std;

int freq[20];

int main()
{
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; ++t){
        for (int i=1; i<=16; ++i){
            freq[i] = 0;
        }
        int ans1, ans2;
        scanf("%d", &ans1);
        for (int i=1; i<=4; ++i){
            for (int j=1; j<=4; ++j){
                int card;
                scanf("%d", &card);
                if (i == ans1){
                    ++freq[card];
                }
            }
        }
        int found = 0;
        int result;
        scanf("%d", &ans2);
        for (int i=1; i<=4; ++i){
            for (int j=1; j<=4; ++j){
                int card;
                scanf("%d", &card);
                if (i == ans2){
                    if (++freq[card] == 2){
                        result = card;
                        ++found;
                    }
                }
            }
        }

        if (found == 0){
            printf("Case #%d: Volunteer cheated!\n", t);
        }else if (found == 1){
            printf("Case #%d: %d\n", t, result);
        }else{
            printf("Case #%d: Bad magician!\n", t);
        }
    }

    return 0;
}
