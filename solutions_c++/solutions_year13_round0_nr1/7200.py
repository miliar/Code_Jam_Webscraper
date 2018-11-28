#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<map>
#include<vector>
#include<queue>
#include<string>
#include<stack>
#include<set>
#include<utility>
#include<algorithm>
#include<bitset>

using namespace std;

char str[4][4];


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,test=1;
    char ch;
    bool extra;

    scanf("%d%*c",&t);

    while(t--)
    {
        extra = false;
        bool T = true;


        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            scanf("%c",&str[i][j]);

            scanf("%*c");
        }

        scanf("%*c");

        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(str[i][j]=='.')
            {
                extra=true;
                goto out;
            }
        }

        out:

        bool flag=false;


        int i;
        for(int j=0;j<4;j++)
        {
            ch=str[j][0];

            if(ch=='T')
            {
                flag=true;
                ch=str[j][1];

                if(ch=='T')
                T=false;

                i=2;
            }
            else
            i=1;

            if(T)
            for(;i<4;i++)
            {
                if( (str[j][i]!='T' && str[j][i]!=ch) || (flag && str[j][i]=='T') || ch=='.' )
                break;

                if(str[j][i]=='T')
                flag=true;
            }

            if(i==4)
            {
                printf("Case #%d: %c won\n",test++,ch);
                goto end;
            }
        }

        flag=false;


        for(int j=0;j<4;j++)
        {
            T=true;
            char ch=str[0][j];

            if(ch=='T')
            {
                flag=true;
                ch=str[1][j];

                if(ch=='T')
                T=false;

                i=2;
            }
            else
            i=1;

            if(T)
            for(;i<4;i++)
            {
                if( (str[i][j]!='T' && str[i][j]!=ch) || (flag && str[i][j]=='T') || ch=='.' )
                break;

                if(str[i][j]=='T')
                flag=true;
            }

            if(i==4)
            {
                printf("Case #%d: %c won\n",test++,ch);
                goto end;
            }
        }

        flag=false;
        T=true;

        ch=str[0][0];

        if(ch=='T')
        {
            ch=str[1][1];

            if(ch=='T')
            T=false;

            flag=true;

            i=2;
        }
        else
        i=1;

        if(T)
        for(;i<4;i++)
        {
            if( (str[i][i]!='T' && str[i][i]!=ch) || (flag && str[i][i]=='T') || ch=='.')
            break;

            if(str[i][i]=='T')
            flag=true;
        }

        if(i==4)
        {
            printf("Case #%d: %c won\n",test++,ch);
            goto end;
        }

        flag=false;
        T=true;

        ch=str[0][3];

        if(ch=='T')
        {
            ch=str[1][2];

            if(ch=='T')
            T=false;

            flag=true;

            i=2;
        }
        else
        i=1;

        if(T)
        for(;i<4;i++)
        {
            if( (str[i][3-i]!='T' && str[i][3-i]!=ch) || (flag && str[i][3-i]=='T') || ch=='.')
            break;

            if(str[i][3-i]=='T')
            flag=true;
        }

        if(i==4)
        {
            printf("Case #%d: %c won\n",test++,ch);
            goto end;
        }

        if(extra)
        printf("Case #%d: Game has not completed\n",test++);
        else
        printf("Case #%d: Draw\n",test++);

        end:
        ;
    }
    return 0;
}
