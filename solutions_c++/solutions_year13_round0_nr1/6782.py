#include<stdio.h>
char s[5][5];
int solve()
{
    int i,j,k;
    int a=0,b=0,c=0;
    for(i=0;i<4;i++)
    {
      if(s[i][i]=='X')
      a++;
      if(s[i][i]=='O')
      b++;
      if(s[i][i]=='T')
      c++;
    }
    if(a==4||(a==3&&c==1))
    return 1;
    if(b==4||(b==3&&c==1))
    return 2;
    a=0,b=0,c=0;
    for(i=0;i<4;i++)
    {
      if(s[i][3-i]=='X')
      a++;
      if(s[i][3-i]=='O')
      b++;
      if(s[i][3-i]=='T')
      c++;
    }
    if(a==4||(a==3&&c==1))
    return 1;
    if(b==4||(b==3&&c==1))
    return 2;
    for(i=0;i<4;i++)
    {
       a=0,b=0,c=0;
       for(j=0;j<4;j++)
       {
           if(s[i][j]=='X')
           a++;
           if(s[i][j]=='O')
           b++;
           if(s[i][j]=='T')
           c++;
       }
    if(a==4||(a==3&&c==1))
    return 1;
    if(b==4||(b==3&&c==1))
    return 2;
    }
    for(i=0;i<4;i++)
    {
        a=0,b=0,c=0;
       for(j=0;j<4;j++)
       {
           if(s[j][i]=='X')
           a++;
           if(s[j][i]=='O')
           b++;
           if(s[j][i]=='T')
           c++;
       }
      if(a==4||(a==3&&c==1))
      return 1;
      if(b==4||(b==3&&c==1))
      return 2;
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(s[i][j]=='.')
              return 4;
        }
    }
    return 3;
}

int main()
{
   // freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int ii=1;
    while(t--)
    {
        printf("Case #%d: ",ii++);
        int i,j;
        for(i=0;i<4;i++)
            scanf("%s",s[i]);
        int ans=solve();
        if(ans==1)
        printf("X won\n");
        else if(ans==2)
        printf("O won\n");
        else if(ans==3)
        printf("Draw\n");
        else if(ans==4)
        printf("Game has not completed\n");
    }
    return 0;
}

