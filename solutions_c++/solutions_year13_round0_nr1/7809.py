#include<cstdio>
using namespace std;
int main()
{
    int t,i,j,k=0,o,x,f,f1,f2;
    char arr[4][4];
    scanf("%d",&t);
    for(;t;t--)
    {
        k++;
        o=x=f2=f1=f=0;
        for(i=0;i<4;i++)
                scanf("%s",arr[i]);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr[i][j]!='X'&&arr[i][j]!='T')
                    f1=1;
                if(arr[i][j]!='O'&&arr[i][j]!='T')
                    f2=1;
            }
            if(f1==0)
                x=1;
            if(f2==0)
                o=1;
            f1=f2=0;
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr[j][i]!='X'&&arr[j][i]!='T')
                    f1=1;
                if(arr[j][i]!='O'&&arr[j][i]!='T')
                    f2=1;
            }

            if(f1==0)
                x=1;
            if(f2==0)
                o=1;
            f1=f2=0;
        }
        for(i=0;i<4;i++)
        {
            if(arr[i][i]!='O'&&arr[i][i]!='T')
                f2=1;
            if(arr[i][i]!='X'&&arr[i][i]!='T')
                f1=1;
        }
            if(f1==0)
                x=1;
            if(f2==0)
                o=1;
        f1=f2=0;
        for(i=0;i<4;i++)
        {
            if(arr[3-i][i]!='O'&&arr[3-i][i]!='T')
                f2=1;
            if(arr[3-i][i]!='X'&&arr[3-i][i]!='T')
                f1=1;
        }
            if(f1==0)
                x=1;
            if(f2==0)
                o=1;
        f1=f2=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(arr[i][j]=='.')
                    f=1;
        if(x==1)
            printf("Case #%d: X won",k);
        else if(o==1)
            printf("Case #%d: O won",k);
        else if(f==1)
            printf("Case #%d: Game has not completed",k);
        else
            printf("Case #%d: Draw",k);
        printf("\n");
    }
    return 0;
}

