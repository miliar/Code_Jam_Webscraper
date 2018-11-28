#include<stdio.h>
#include<string.h>

using namespace std;

char arr[4][4];

bool xx=false;
bool oo=false;

void chk_row(int st,char ch)
{
    int cnt=0;
    for(int i=0;i<4;i++)
    {
        if(arr[st][i]==ch or arr[st][i]=='T') cnt++;
    }

    if(cnt==4)
    {
        if(ch=='X') xx=true;
        else if(ch=='O') oo=true;
    }
    return;
}


void chk_col(int st,char ch)
{
    int cnt=0;
    for(int i=0;i<4;i++)
    {
        if(arr[i][st]==ch or arr[i][st]=='T') cnt++;
    }

    if(cnt==4)
    {
        if(ch=='X') xx=true;
        else if(ch=='O') oo=true;
    }
    return;
}


void chk_diag(char ch)
{
    int cnt=0;
    for(int i=0;i<4;i++)
    if(arr[i][i]==ch || arr[i][i]=='T') cnt++;

    if(cnt==4)
    {
        if(ch=='X') xx=true;
        else if(ch=='O') oo=true;

        return;
    }

    cnt=0;

    for(int i=3;i>=0;i--)
    if(arr[3-i][i]==ch || arr[3-i][i]=='T') cnt++;

    if(cnt==4)
    {
        if(ch=='X') xx=true;
        else if(ch=='O') oo=true;

        return;
    }
    return;
}

int main()
{



    freopen("in.in","r",stdin);

    freopen("out.in","w",stdout);

    int T;

    scanf(" %d",&T);

    for(int tt=1; tt<=T; tt++)
    {
        xx=false; oo=false;

        bool not_com=false;

        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                scanf(" %c",&arr[i][j]);
                if(arr[i][j]=='.') not_com=true;
            }


        for(int i=0; i<4; i++)
            if(xx==false)    chk_row(i,'X');

        if(xx)
        {
            printf("Case #%d: X won\n",tt);
            continue;
        }

        for(int i=0; i<4; i++)
            chk_col(i,'X');

        if(xx)
        {
            printf("Case #%d: X won\n",tt);
            continue;
        }

        chk_diag('X');

        if(xx)
        {
            printf("Case #%d: X won\n",tt);
            continue;
        }




        for(int i=0; i<4; i++)
            if(oo==false)    chk_row(i,'O');

        if(oo)
        {
            printf("Case #%d: O won\n",tt);
            continue;
        }

        for(int i=0; i<4; i++)
            chk_col(i,'O');

        if(oo)
        {
            printf("Case #%d: O won\n",tt);
            continue;
        }

        chk_diag('O');

        if(oo)
        {
            printf("Case #%d: O won\n",tt);
            continue;
        }



        if(not_com)
        {
            printf("Case #%d: Game has not completed\n",tt);
            continue;
        }

        printf("Case #%d: Draw\n",tt);


    }

    return 0;
}
