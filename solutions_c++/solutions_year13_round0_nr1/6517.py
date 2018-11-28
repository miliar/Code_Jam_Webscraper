#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int cas;
int kk;
char map[8][8];

int check(char ch)
{
    for(int i=0;i<4;i++){
        int flag=1;
        for(int j=0;j<4;j++){
            if(map[i][j]!=ch&&map[i][j]!='T')
                flag=0;
        }
        if(flag) return 1;
    }
    for(int i=0;i<4;i++){
        int flag=1;
        for(int j=0;j<4;j++){
            if(map[j][i]!=ch&&map[j][i]!='T')
                flag=0;
        }
        if(flag) return 1;
    }
    int flag=1;
    for(int j=0;j<4;j++){
        if(map[j][j]!=ch&&map[j][j]!='T')
            flag=0;
    }
    if(flag) return 1;
    flag=1;
    for(int j=0;j<4;j++){
        if(map[j][3-j]!=ch&&map[j][3-j]!='T')
            flag=0;
    }
    if(flag) return 1;
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cas);
    kk=0;
    while(cas--){
        for(int i=0;i<4;i++)
            scanf("%s",map[i]);
        printf("Case #%d: ",++kk);
        int g1,g2;
        g1 = check('X');
        if(g1) {printf("X won\n");continue;}
        g2 = check('O');
        if(g2) {printf("O won\n");continue;}
        int dr=1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(map[i][j]=='.') dr=0;
        if(dr) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
