#include<iostream>
#include<stdio.h>
int arr[5][5];
int won(int v)
{
    int x,t,i,j;
    for(i=0;i<4;i++)
    {
        x=0; t=0;
        for(j=0;j<4;j++)
        {
            if(arr[i][j]==v) x++;
            else if(arr[i][j]==3) t++;
        }
        if(x==3 && t==1) return 1;
        if(x==4) return 1;

        x=0; t=0;
        for(j=0;j<4;j++)
        {
            if(arr[j][i]==v) x++;
            else if(arr[j][i]==3) t++;
        }
        if(x==3 && t==1) return 1;
        if(x==4) return 1;
    }

    x=0; t=0;
    for(i=0;i<4;i++)
    {
       if(arr[i][i]==v) x++;
       else if(arr[i][i]==3) t++;
    }
    if(x==3 && t==1) return 1;
    if(x==4) return 1;
    
    x=0; t=0;
    for(i=0;i<4;i++)
    {
       if(arr[i][3-i]==v) x++;
       else if(arr[i][3-i]==3) t++;
    }
    if(x==3 && t==1) return 1;
    if(x==4) return 1;
    
    return 0;
}
int draw()
{
    int i,j;
    for(i=0;i<4;i++)
      for(j=0;j<4;j++)
        if(arr[i][j]==0) 
            return 0;
    return 1;
}
int main()
{
    freopen("inptictac.txt","r",stdin);
    freopen("outtictac.txt","w",stdout);
    int t,tc,i,j;
    char buf[10];
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        for(i=0;i<4;i++)
        {
            scanf("%s",buf);
            for(j=0;j<4;j++)
            {
               if(buf[j]=='X') arr[i][j]=1;
               else if(buf[j]=='O') arr[i][j]=2;
               else if(buf[j]=='T') arr[i][j]=3;
               else if(buf[j]=='.') arr[i][j]=0;
            }
        }
        if(won(1))
           printf("Case #%d: X won\n",tc);
        else if(won(2))
           printf("Case #%d: O won\n",tc);
        else if(draw())
           printf("Case #%d: Draw\n",tc);
        else 
           printf("Case #%d: Game has not completed\n",tc);
    }
    return 0;
}

    
