#include <cstdio>

char table[5][5];

void solve()
{
    int i;
    bool Tapear=false;
    bool incomplete=false;
    for(i=1;i<=4;i++)
    {
        char symbol;
        bool won=true;
        if(table[i][1]=='T' && Tapear==false)
        {
            Tapear=true;
            symbol=table[i][2];
        }
        else
            symbol=table[i][1];
        if(symbol=='.')
        {
            incomplete=true;
            won=false;
        }
        else
            {
                for(int j=2;j<=4;j++)
                if(table[i][j]!=symbol)
                    if(Tapear==false)
                        if(table[i][j]!='T')
                            won=false;
                        else{}
                    else
                        won=false;
            }
        if(won==true)
        {
            printf("%c won\n",symbol);
            return;
        }
    }
    Tapear=false;
    for(i=1;i<=4;i++)
    {
        char symbol;
        bool won=true;
        if(table[1][i]=='T' && Tapear==false)
        {
            Tapear=true;
            symbol=table[2][i];
        }
        else
            symbol=table[1][i];
        if(symbol=='.')
        {
            incomplete=true;
            won=false;
        }
        else
            {
                for(int j=2;j<=4;j++)
                if(table[j][i]!=symbol)
                    if(Tapear==false)
                        if(table[j][i]!='T')
                            won=false;
                        else{}
                    else
                        won=false;
            }
        if(won==true)
        {
            printf("%c won\n",symbol);
            return;
        }
    }

    char symbol;
    bool won=true;
    Tapear=false;
        if(table[1][1]=='T' && Tapear==false)
        {
            Tapear=true;
            symbol=table[2][2];
        }
        else
            symbol=table[1][1];
         if(symbol=='.')
        {
            incomplete=true;
            won=false;
        }
        else
        for(int i=2;i<=4;i++)
        {
             if(table[i][i]!=symbol)
                    if(Tapear==false)
                        if(table[i][i]!='T')
                            won=false;
                        else{}
                    else
                        won=false;
        }
         if(won==true)
        {
            printf("%c won\n",symbol);
            return;
        }
        Tapear=false;
        won=true;
        if(table[1][4]=='T' && Tapear==false)
        {
            Tapear=true;
            symbol=table[2][3];
        }
        else
            symbol=table[1][4];
         if(symbol=='.')
        {
            incomplete=true;
            won=false;
        }
        else
        for(int i=2;i<=4;i++)
        {
             if(table[i][4-i+1]!=symbol)
                    if(Tapear==false)
                        if(table[i][4-i+1]!='T')
                            won=false;
                        else{}
                    else
                        won=false;
        }
         if(won==true)
        {
            printf("%c won\n",symbol);
            return;
        }

    if(incomplete==true)
        printf("Game has not completed\n");
    else
        printf("Draw\n");
}

int main()
{
    int T;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&T);
     scanf("\n");
    for(int k=1;k<=T;k++)
    {
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%c",&table[i][j]);
            }
            scanf("\n");
        }
    printf("Case #%d: ",k);
    solve();



    scanf("\n");
    }
    return 0;
}
