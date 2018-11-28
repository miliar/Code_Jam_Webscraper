#include<cstdio>
using namespace std;
int a[10][10], b[10][10];
int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T, x, y, res = 1;
    scanf("%d", &T);
    while(T--){
        scanf("%d", &x);
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                scanf("%d", &a[i][j]);
            }
        }
        scanf("%d", &y);
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                scanf("%d", &b[i][j]);
            }
        }
        int cnt = 0, ans;
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                if(a[x][i] == b[y][j]){
                    cnt++;
                    ans = a[x][i];
                }
            }
        }
        if(cnt == 0){
            printf("Case #%d: Volunteer cheated!\n", res++);
        }
        else if(cnt == 1){
            printf("Case #%d: %d\n", res++, ans);
        }
        else printf("Case #%d: Bad magician!\n", res++);
    }
    return 0;
}
