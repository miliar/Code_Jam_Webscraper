#include<cstdio>
#include<cstring>

#define ms(a,b) memset(a,b,sizeof(a))

int a, card[4][4];
bool possi[20];

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d", &a);
        a--;
        ms(possi, true);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &card[i][j]);
                if(i != a) possi[card[i][j]] = false;
            }
        }
        scanf("%d", &a);
        a--;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &card[i][j]);
                if(i != a) possi[card[i][j]] = false;
            }
        }
        int ans = 0;
        int p = 0;
        for(int i = 1; i <= 16; i++){
            if(possi[i]) p++, ans = i;
        }
        printf("Case #%d: ", ++cnt);
        if(p == 0) printf("Volunteer cheated!\n");
        else if(p > 1) printf("Bad magician!\n");
        else printf("%d\n", ans);
    }
    return 0;
}
