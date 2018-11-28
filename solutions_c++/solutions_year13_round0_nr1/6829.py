#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char map[4][4];
bool xwon,owon,draw,unfinish;

int main()
{
    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        memset(map,0,sizeof(map));
        xwon=owon=draw=unfinish=false;

        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++){
                scanf("%c",&map[i][j]);
                while(map[i][j]=='\n') scanf("%c",&map[i][j]);
        }
        //for (int i=0;i<4;i++)
          //  for (int j=0;j<4;j++) printf("%c",map[i][j]);

        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                if (map[i][j]=='.') unfinish=true;
        for (int i=0;i<4;i++)
        {
            bool flag=true;
            for (int j=0;j<4;j++)
                if (map[i][j]=='X'||map[i][j]=='.') flag=false;
            if (flag) owon=true;
        }
        for (int i=0;i<4;i++)
        {
            bool flag=true;
            for (int j=0;j<4;j++)
                if (map[j][i]=='X'||map[j][i]=='.') flag=false;
            if (flag) owon=true;
        }
        bool flag=true;
        for (int j=0;j<4;j++)
            if (map[j][j]=='X'||map[j][j]=='.') flag=false;
        if (flag) owon=true;
        flag=true;
        for (int j=0;j<4;j++)
            if (map[j][3-j]=='X'||map[j][3-j]=='.') flag=false;
        if (flag) owon=true;


        for (int i=0;i<4;i++)
        {
            bool flag=true;
            for (int j=0;j<4;j++)
                if (map[i][j]=='O'||map[i][j]=='.') flag=false;
            if (flag) xwon=true;
        }
        for (int i=0;i<4;i++)
        {
            bool flag=true;
            for (int j=0;j<4;j++)
                if (map[j][i]=='O'||map[j][i]=='.') flag=false;
            if (flag) xwon=true;
        }
        flag=true;
        for (int j=0;j<4;j++)
            if (map[j][j]=='O'||map[j][j]=='.') flag=false;
        if (flag) xwon=true;
        flag=true;
        for (int j=0;j<4;j++)
            if (map[j][3-j]=='O'||map[j][3-j]=='.') flag=false;
        if (flag) xwon=true;

        printf("Case #%d: ",cases);
        if (xwon) printf("X won\n");
        else if (owon) printf("O won\n");
            else if (unfinish) printf("Game has not completed\n");
                else printf("Draw\n");
    }
    return 0;
}
