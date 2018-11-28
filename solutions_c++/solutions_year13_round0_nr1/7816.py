#include<cstdio>

int T,TT;
char b[4][5];
int owin,xwin,notcomp;

int main() {
    int i,j,k;
    scanf("%d",&T);
    while(TT<T){TT++;
        printf("Case #%d: ",TT);
        for(i=0;i<4;i++)scanf("%s",b[i]);
        owin=xwin=notcomp=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++)if(b[i][j]!='O' && b[i][j]!='T')break;
            if(j==4)owin=1;
            for(j=0;j<4;j++)if(b[j][i]!='O' && b[j][i]!='T')break;
            if(j==4)owin=1;
        }
        for(j=0;j<4;j++)if(b[j][3-j]!='O' && b[j][3-j]!='T')break;
        if(j==4)owin=1;
        for(j=0;j<4;j++)if(b[j][j]!='O' && b[j][j]!='T')break;
        if(j==4)owin=1;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++)if(b[i][j]!='X' && b[i][j]!='T')break;
            if(j==4)xwin=1;
            for(j=0;j<4;j++)if(b[j][i]!='X' && b[j][i]!='T')break;
            if(j==4)xwin=1;
        }
        for(j=0;j<4;j++)if(b[j][3-j]!='X' && b[j][3-j]!='T')break;
        if(j==4)xwin=1;
        for(j=0;j<4;j++)if(b[j][j]!='X' && b[j][j]!='T')break;
        if(j==4)xwin=1;
        for(i=0;i<4;i++)for(j=0;j<4;j++)if(b[i][j]=='.')notcomp=1;
        if(owin)printf("O won\n");
        else if(xwin)printf("X won\n");
        else if(notcomp)printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
