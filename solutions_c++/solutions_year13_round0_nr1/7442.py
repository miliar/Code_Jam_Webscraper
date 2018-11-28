/*
    0   .
    1   X
    2   O
    3   T
*/
#include <cstdio>
#include <cstring>
char a[5][5];
int col[5][4],row[5][4],dial[4],diar[4];
int d[222];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("aab.out","w",stdout);
    int T,n=4;
    d['.']=0;
    d['X']=1;
    d['O']=2;
    d['T']=3;
    scanf("%d\n",&T);
    for (int I(1);I<=T;I++){
        memset(col,0,sizeof(col));
        memset(row,0,sizeof(row));
        memset(dial,0,sizeof(dial));
        memset(diar,0,sizeof(diar));
        for (int i(0);i<n;i++){
            scanf("%s\n",a[i]);
            for (int j(0);j<n;j++){
                col[i][d[a[i][j]]]++;
                row[j][d[a[i][j]]]++;
            }
        }
        scanf("\n");
        for (int i(0);i<n;i++) dial[d[a[i][i]]]++;
        for (int i(0);i<n;i++) diar[d[a[i][3-i]]]++;
        int ans=0;
        for (int i(1);i<=2;i++){
            if (dial[i] && dial[i]+dial[3]==4) ans=i;
            if (diar[i] && diar[i]+diar[3]==4) ans=i;
            if (ans) break;
            for (int j(0);j<n;j++){
                if (col[j][i] && col[j][i]+col[j][3]==4) ans=i;
                if (row[j][i] && row[j][i]+row[j][3]==4) ans=i;
            }
        }
        printf("Case #%d: ",I);
        if (ans) {
            if (ans==1) printf("X");
            if (ans==2) printf("O");
            printf(" won\n");
        } else {
            int tt=0;
            for (int i(0);i<n;i++) tt+=row[i][0];
            if (tt) {
                printf("Game has not completed\n");
            }else {
                printf("Draw\n");
            }
        }
    }
    return 0;
}
