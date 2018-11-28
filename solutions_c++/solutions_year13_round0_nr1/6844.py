#include<cstdio>
using namespace std;

char a[5][5];

int main()
{
    int t,sum;
    bool flag,ans,dot;
    scanf("%d\n",&t);
    for(int caseno=1; caseno<=t; caseno++)
    {
        dot=false;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                scanf("%c",&a[i][j]);
                if(a[i][j]=='.') dot=true;
            }
            getchar();
        }
        getchar();

        ans=false;

        for(int i=0; i<4; i++)
        {
            sum=0;
            flag=false;
            for(int j=0; j<4; j++)
            {
                if(a[i][j]=='X') sum+=1;
                else if(a[i][j]=='O') sum-=1;
                else if(a[i][j]=='T') flag=true;
            }
            if(sum==4 || (sum==3 && flag==true))
            {
                ans=true;
                printf("Case #%d: X won\n",caseno);
                break;
            }
            else if(sum==-4 || (sum==-3 && flag==true))
            {
                ans=true;
                printf("Case #%d: O won\n",caseno);
                break;
            }
        }
        if(ans) continue;

        for(int i=0; i<4; i++)
        {
            sum=0;
            flag=false;
            for(int j=0; j<4; j++)
            {
                if(a[j][i]=='X') sum+=1;
                else if(a[j][i]=='O') sum-=1;
                else if(a[j][i]=='T') flag=true;
            }
            if(sum==4 || (sum==3 && flag==true))
            {
                ans=true;
                printf("Case #%d: X won\n",caseno);
                break;
            }
            else if(sum==-4 || (sum==-3 && flag==true))
            {
                ans=true;
                printf("Case #%d: O won\n",caseno);
                break;
            }
        }

        if(ans) continue;

        sum=0;
        flag=false;
        for(int i=0; i<4; i++)
        {
            if(a[i][i]=='X') sum+=1;
            else if(a[i][i]=='O') sum-=1;
            else if(a[i][i]=='T') flag=true;
        }
        if(sum==4 || (sum==3 && flag==true))
        {
            ans=true;
            printf("Case #%d: X won\n",caseno);
            continue;
        }
        else if(sum==-4 || (sum==-3 && flag==true))
        {
            ans=true;
            printf("Case #%d: O won\n",caseno);
            continue;
        }

        sum=0;
        flag=false;
        for(int i=0,j=3; i<=3; i++,j--)
        {
            if(a[i][j]=='X') sum+=1;
            else if(a[i][j]=='O') sum-=1;
            else if(a[i][j]=='T') flag=true;

        }
        if(sum==4 || (sum==3 && flag==true))
        {
            ans=true;
            printf("Case #%d: X won\n",caseno);
            continue;
        }
        else if(sum==-4 || (sum==-3 && flag==true))
        {
            ans=true;
            printf("Case #%d: O won\n",caseno);
            continue;
        }

        if(ans==false && dot==false)
        {
            printf("Case #%d: Draw\n",caseno);
            continue;
        }
        else
        {
            printf("Case #%d: Game has not completed\n",caseno);
            continue;
        }
    }
    return 0;
}
