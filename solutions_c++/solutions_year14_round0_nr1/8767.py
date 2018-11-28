#include <cstdio>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    int d1[4], d2[4];
    int c1, c2;
    int tmp;

    for(int k = 1; k <= t; k++){
        scanf("%d", &c1);
        for(int i = 1; i <= 4; i++){
            for(int j = 0; j < 4; j++){
                if(i == c1) scanf("%d", &d1[j]);
                else scanf("%d", &tmp);
            }
        }

        scanf("%d", &c2);
        for(int i = 1; i <= 4; i++){
            for(int j = 0; j < 4; j++){
                if(i == c2) scanf("%d", &d2[j]);
                else scanf("%d", &tmp);
            }
        }

        int res = -1;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(d1[i] == d2[j]){
                    if(res == -1) res = d1[i];
                    else res = -2;
                    break;
                }

            if(res == -2) break;
            }
        }

        if(res == -1) printf("Case #%d: Volunteer cheated!\n", k);
        else if(res == -2) printf("Case #%d: Bad magician!\n", k);
        else printf("Case #%d: %d\n", k, res);

    }
}
