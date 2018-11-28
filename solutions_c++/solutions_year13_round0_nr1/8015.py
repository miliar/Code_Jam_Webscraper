#include<conio.h>
#include<cstdio>
#include<iostream>
#include<math.h>
#include<process.h>
#include<cstdlib>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    char ch,a[4][4];
    int i,j,k,t,test_c;
    //scanf("%d",&t);
    cin>>t;
    for(test_c=1;test_c<=t;test_c++)
    {
       int counte=0;
       for(i=0;i<4;i++)
       {
          for(j=0;j<4;j++)
          {
             cin>>a[i][j];
             if(a[i][j]=='.')
             counte++;
          }
       }
       for(i=0;i<4;i++)
       {
          if(a[i][0]=='.')
          continue;
          ch=a[i][0];
          for(j=1;j<4;j++)
          {
              if(a[i][j]!=ch&&a[i][j]!='T')
              break;
          }
          if(j==4)
          break;
       }
       if(i!=4)
       {
          printf("Case #%d: %c won\n",test_c,ch);
          continue;
       }
       for(j=0;j<4;j++)
       {
          if(a[0][j]=='.')
          continue;
          ch=a[0][j];
          for(i=1;i<4;i++)
          {
              if(a[i][j]!=ch&&a[i][j]!='T')
              break;
          }
          if(i==4)
          break;
       }
       if(j!=4)
       {
          printf("Case #%d: %c won\n",test_c,ch);
          continue;
       }
       ch=a[0][0];
       if(ch!='.'){
       for(i=1,k=1;i<4;i++,k++)
       if(a[i][k]!=ch&&a[i][k]!='T')
       break;
       if(i==4)
       {
          printf("Case #%d: %c won\n",test_c,ch);
          continue;
       }}
       ch=a[0][3];
       if(ch!='.'){
       for(i=1,k=2;i<4;i++,k--) 
       if(a[i][k]!=ch&&a[i][k]!='T')
       break;   
       if(i==4)
       {
          printf("Case #%d: %c won\n",test_c,ch);
          continue;
       }}
       if(counte)
       printf("Case #%d: Game has not completed\n",test_c);
       else
       printf("Case #%d: Draw\n",test_c);
    }
    getch();
    return 0;
}    
