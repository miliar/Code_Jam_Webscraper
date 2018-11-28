#include<stdio.h>
#define fori(a,b) for(i=a;i<=b;i++)
#define forj(a,b) for(j=a;j<=b;j++)
#define scani(a) scanf("%d",&a);
int main()
{
    int t,dot,flag,fl,i,j,k,tx,ty;
    scani(t)
    char str[5][5];
    for(k=1;k<=t;k++)
    {
      dot=0;
      flag=0;
      fori(0,3)
        scanf("%s",str[i]);
      fori(0,3)
        forj(0,3)
        { 
         if(str[i][j]=='T')
          {
            tx=i;
            ty=j;
          }
         if(str[i][j]=='.')
           dot=1;
        }
      str[tx][ty]='X';
      flag=0;
      fori(0,3)
      {
        fl=0;
        forj(0,3)
          if(str[i][j]!='X')
          {
            fl=1;
            break;
          }
        if(fl==0)
        {
          flag=1;
          printf("Case #%d: X won\n",k);
          break;
        }
      }
      if(flag)
        continue;
      forj(0,3)
      {
        fl=0;
        fori(0,3)
          if(str[i][j]!='X')
          {
            fl=1;
            break;
          }
        if(fl==0)
        {
          flag=1;
          printf("Case #%d: X won\n",k);
          break;
        }
      }
        if(flag)
          continue;
      if(flag==0)
      {
      if(str[0][0]=='X' && str[1][1]=='X' && str[2][2]=='X' && str[3][3]=='X')
      {
         flag=1;
         printf("Case #%d: X won\n",k);
         continue;
      }
      else
        if(str[0][3]=='X' && str[1][2]=='X' && str[2][1]=='X' && str[3][0]=='X')
        {
           flag=1;
           printf("Case #%d: X won\n",k);
           continue;
        }
        }      
      if(flag==0)
      {
      str[tx][ty]='O';
      fori(0,3)
      {
        fl=0;
        forj(0,3)
          if(str[i][j]!='O')
          {
            fl=1;
            break;
          }
        if(fl==0)
        {
          flag=1;
          printf("Case #%d: O won\n",k);
          break;
        }
      }
      if(flag==1)
        continue;
      forj(0,3)
      {
        fl=0;
        fori(0,3)
          if(str[i][j]!='O')
          {
            fl=1;
            break;
          }
        if(fl==0)
        {
          flag=1;
          printf("Case #%d: O won\n",k);
          break;
        }
      }
      if(flag==1)
        continue;
      if(flag==0)
      {
      if(str[0][0]=='O' && str[1][1]=='O' && str[2][2]=='O' && str[3][3]=='O')
      {
         flag=1;
         printf("Case #%d: O won\n",k);
         continue;
      }
      else
        if(str[0][3]=='O' && str[1][2]=='O' && str[2][1]=='O' && str[3][0]=='O')
        {
           flag=1;
           printf("Case #%d: O won\n",k);
           continue;
        }
      }      
      }
      if(flag==0)
        if(dot==1)
          printf("Case #%d: Game has not completed\n",k);
        else
          printf("Case #%d: Draw\n",k);
      char ch=getchar();
    }
    return 0;
}
