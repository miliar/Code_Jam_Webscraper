#include <cstdio>

int main() {
    int t;
    scanf("%d",&t);
    for(int k = 1;k <= t;k++) {
        char tab[4][6];
        int aux = 1;
        for(int i = 0;i < 4;i++) {
            scanf("%s",tab[i]);
        }
        int l1 = 0, l2 = 0, c1 = 0, c2 = 0, d1 = 0, d2 = 0, d3 = 0, d4 = 0;
        int p1 = 0, p2 = 0;
        for(int i = 0;i <= 3;i++) {
            l1 = l2 = c1 = c2 = 0;
            for(int j = 0;j <= 3;j++) {
                if(tab[i][j] == 'X' || tab[i][j] == 'T') l1++;
                if(tab[i][j] == 'O' || tab[i][j] == 'T') l2++;

                if(tab[j][i] == 'X' || tab[j][i] == 'T') c1++;
                if(tab[j][i] == 'O' || tab[j][i] == 'T') c2++;

                if(tab[i][j] == '.') aux = 0;
            }
            if(l1 == 4 || c1 == 4) {
                p1 = 1;
                break;
            }
            if(l2 == 4 || c2 == 4) {
                p2 = 1;
                break;
            }
            if(tab[i][i] == 'X' || tab[i][i] == 'T') d1++;
            if(tab[i][i] == 'O' || tab[i][i] == 'T') d2++;
            if(tab[i][3-i] == 'X' || tab[i][3-i] == 'T') d3++;
            if(tab[i][3-i] == 'O' || tab[i][3-i] == 'T') d4++;
        }
        if(d1 == 4 || d3 == 4) p1 = 1;
        if(d2 == 4 || d4 == 4) p2 = 1;


        if(p1) printf("Case #%d: X won\n",k);
        else if(p2) printf("Case #%d: O won\n",k);
        else if(aux) printf("Case #%d: Draw\n",k);
        else printf("Case #%d: Game has not completed\n",k);

        scanf("\n");
    }
    return 0;
}
