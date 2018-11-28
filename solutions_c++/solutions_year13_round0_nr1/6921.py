#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
using namespace std;

struct data
{
    int X,O,T;
};

data rows[5],cols[5],diag1,diag2;
int dots;

void init()
{
    dots=0;
    diag1.X=0;
    diag1.O=0;
    diag1.T=0;
    diag2.X=0;
    diag2.O=0;
    diag2.T=0;
    for(int i=0;i<=4;i++)
    {
        rows[i].X=0;
        rows[i].O=0;
        rows[i].T=0;
        cols[i].X=0;
        cols[i].O=0;
        cols[i].T=0;
    }
}

void scan()
{
    char xs[1000];
    string s;
    for(int i=0;i<4;i++)
    {
        scanf("%s",xs);
        s=xs;
        for(int j=0;j<4;j++)
        {
            if(s[j]=='X')
            {
                rows[i].X++;
                cols[j].X++;
                if(i==j)
                    diag1.X++;
                else if(i+j==3)
                    diag2.X++;
            }
            else if(s[j]=='O')
            {
                rows[i].O++;
                cols[j].O++;
                if(i==j)
                    diag1.O++;
                else if(i+j==3)
                    diag2.O++;
            }
            else if(s[j]=='T')
            {
                rows[i].T++;
                cols[j].T++;
                if(i==j)
                    diag1.T++;
                else if(i+j==3)
                    diag2.T++;
            }
            else if(s[j]=='.')
            {
                dots++;
            }
        }
    }
}

bool checkR(int k)
{
    for(int i=0;i<4;i++)
    {
        if(rows[i].X+rows[i].T==4)
        {
            printf("Case #%d: X won\n",k);
            return true;
        }
        if(rows[i].O+rows[i].T==4)
        {
            printf("Case #%d: O won\n",k);
            return true;
        }
    }
    return false;
}

bool checkC(int k)
{
    for(int i=0;i<4;i++)
    {
        if(cols[i].X+cols[i].T==4)
        {
            printf("Case #%d: X won\n",k);
            return true;
        }
        if(cols[i].O+cols[i].T==4)
        {
            printf("Case #%d: O won\n",k);
            return true;
        }
    }
    return false;
}

bool checkD(int k)
{
    if(diag1.X+diag1.T==4 || diag2.X+diag2.T==4)
    {
        printf("Case #%d: X won\n",k);
        return true;
    }
    if(diag1.O+diag1.T==4 || diag2.O+diag2.T==4)
    {
        printf("Case #%d: O won\n",k);
        return true;
    }
    return false;
}

int main()
{
    int K;
    freopen("A-large.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    scanf("%d",&K);
    for(int k=1;k<=K;k++)
    {
        init();
        scan();
        if(checkR(k))
            continue;
        if(checkC(k))
            continue;
        if(checkD(k))
            continue;
        if(dots==0)
            printf("Case #%d: Draw\n",k);
        else
            printf("Case #%d: Game has not completed\n",k);

    }
}
