#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;
main()
{
  freopen("A-small-attempt1.in", "r", stdin); freopen("a.out", "w", stdout);
  int t;
  scanf("%d",&t);
  for(int w=1;w<=t;w++)
  {
      char ma[4][4];
      for(int i=0;i<4;i++)
      {
          for(int j=0;j<4;j++)
          {
              cin>>ma[i][j];
          }
      }
      char s[100]; gets(s);
      bool x=false,o=false,ficha=false;
      for(int i=0;i<4;i++)
      {
          int contx1=0,contx2=0,conto1=0,conto2=0,cx1=0,cx2=0,co1=0,co2=0;

          for(int k=0;k<4;k++)
          {
              if(ma[k][i]=='X'||ma[k][i]=='T'){contx1++;}
              if(ma[k][i]=='O'||ma[k][i]=='T'){conto1++;}
              if(ma[i][k]=='X'||ma[i][k]=='T'){contx2++;}
              if(ma[i][k]=='O'||ma[i][k]=='T'){conto2++;}
              if(ma[k][i]=='.'){ficha=true;}
              if(ma[i][k]=='.'){ficha=true;}
          }
          int k=0;int i=3;
          for(;k<4;k++,i--)
          {
              if(ma[k][k]=='X'||ma[k][k]=='T'){cx1++;}
              if(ma[k][i]=='O'||ma[i][k]=='T'){co1++;}
              if(ma[k][i]=='X'||ma[i][k]=='T'){cx2++;}
              if(ma[k][k]=='O'||ma[k][k]=='T'){co2++;}
          }
          if(contx1==4||contx2==4||cx1==4||cx2==4)x=true;
          else if(conto1==4||conto2==4||co1==4||cx2==4)o=true;
      }
      if(x)printf("Case #%d: X won\n",w);
      else if(o)printf("Case #%d: O won\n",w);
      else if(!ficha)printf("Case #%d: Draw\n",w);
      else printf("Case #%d: Game has not completed\n",w);

  }
}
