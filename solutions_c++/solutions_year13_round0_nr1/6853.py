#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    char s[10][10];
    char tmp[10];
    int Cas,cas,posxT,posyT;
    scanf("%d",&Cas);
    for (int cas=1; cas<=Cas; ++cas)
    {
        bool tex=false;
        int dotnum=0;
        for (int i=0; i<4; ++i)
        {
            getchar();
            for (int j=0; j<4; ++j)
            {
                scanf("%c",&s[i][j]);
                if (s[i][j]=='T')
                {
                    tex=true;
                    posxT=i;
                    posyT=j;
                }
                if (s[i][j]=='.')
                    dotnum++;
            }
        }
        getchar();
        /*
        for (int i=0;i<4;i++)
        {
            cout<<"                 ";
            for (int j=0;j<4;j++)
                cout<<s[i][j];
            cout<<endl;
        }
        */

        bool result=false;
        char whowin=' ';

        if (tex) s[posxT][posyT]='X';
        for (int i=0; i<4; ++i)
        {
            bool flag=true;
            for (int j=0; j<4; ++j)
                if (s[i][j]!='X') flag=false;
            if (flag)
            {
                result=true;
                whowin='X';
            }
        }
        for (int i=0; i<4; ++i)
        {
            bool flag=true;
            for (int j=0; j<4; ++j)
                if (s[j][i]!='X') flag=false;
            if (flag)
            {
                result=true;
                whowin='X';
            }
        }
        bool flag;
        flag=true;
        for (int i=0; i<4; ++i)
            if (s[i][i]!='X') flag=false;
        if (flag)
        {
            result=true;
            whowin='X';
        }
        flag=true;
        for (int i=0; i<4; ++i)
            if (s[i][3-i]!='X') flag=false;
        if (flag)
        {
            result=true;
            whowin='X';
        }
        if (whowin=='X')
        {
            printf("Case #%d: X won\n",cas);
            continue;
        }

        if (tex) s[posxT][posyT]='O';
        for (int i=0; i<4; ++i)
        {
            bool flag=true;
            for (int j=0; j<4; ++j)
                if (s[i][j]!='O') flag=false;
            if (flag)
            {
                result=true;
                whowin='O';
            }
        }
        for (int i=0; i<4; ++i)
        {
            bool flag=true;
            for (int j=0; j<4; ++j)
                if (s[j][i]!='O') flag=false;
            if (flag)
            {
                result=true;
                whowin='O';
            }
        }
        flag=true;
        for (int i=0; i<4; ++i)
            if (s[i][i]!='O') flag=false;
        if (flag)
        {
            result=true;
            whowin='O';
        }
        flag=true;
        for (int i=0; i<4; ++i)
            if (s[i][3-i]!='O') flag=false;
        if (flag)
        {
            result=true;
            whowin='O';
        }
        if (whowin=='O')
        {
            printf("Case #%d: O won\n",cas);
            continue;
        }
        if (dotnum==0)
        {
            printf("Case #%d: Draw\n",cas);
            continue;
        }
        else
            printf("Case #%d: Game has not completed\n",cas);

    }
    return 0;
}
