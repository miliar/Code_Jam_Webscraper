#include<cstdio>

using namespace std;

int main()
{
    //freopen("c:\\Users\\Blank\\Desktop\\A-small-attempt0.in", "r", stdin);
   // freopen("c:\\Users\\Blank\\Desktop\\A-small-attempt0.out.txt", "w", stdout);
    int n;
    while(~scanf("%d", &n)){
        int q = 0;
        while(n--){
            int i, j, x, y, t = 0, p = 0, a[5][5] = {0}, b[5][5] = {0};
            q++;
            scanf("%d", &x);
            for(i = 0; i < 4; i++){
                for(j = 0; j < 4; j++){
                    scanf("%d", &a[i][j]);
                }
            }
            scanf("%d", &y);
            for(i = 0; i < 4; i++){
                for(j = 0; j < 4; j++){
                    scanf("%d", &b[i][j]);
                }
            }
            for(i = 0; i < 4; i++){
                for(j = 0; j < 4; j++){
                    if(a[x - 1][i] == b[y - 1][j]){
                        t++;
                        p = a[x - 1][i];
                    }
                }
            }
            if(t == 1){
                printf("Case #%d: %d\n", q, p);
            }
            else if(t == 0){
                printf("Case #%d: ", q);
                printf("Volunteer cheated!\n");
            }
            else if(t > 1){
                printf("Case #%d: ", q);
                printf("Bad magician!\n");
            }
        }
    }
    return 0;
}
