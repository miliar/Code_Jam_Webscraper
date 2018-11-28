#include<cstdio>
#include<string.h>
int main()
{
    int t,x,r,c,i,j,a,b,temp;
    char ans[20];
    bool arr[5][5][5];
    for(x=1;x<=4;x++)
    {
        for(r=1;r<=4;r++)
        {
            for(c=1;c<=4;c++)
            {
                arr[x][r][c]=false;
                if((r*c)%x==0)
                {
                    if(x==1)
                        arr[x][r][c]=true;
                    else if(x==2&&(r>=2||c>=2))
                        arr[x][r][c]=true;
                    else if(x==3&&(r>=2&&c>=2))
                        arr[x][r][c]=true;
                    else if(x==4&&((r==4&&c>=3)||(c==4&&r>=3)))
                        arr[x][r][c]=true;
                }
            }
        }
    }
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(arr[x][r][c])
            printf("Case #%d: GABRIEL\n",i);
        else
            printf("Case #%d: RICHARD\n",i);
    }
    return 0;
}
