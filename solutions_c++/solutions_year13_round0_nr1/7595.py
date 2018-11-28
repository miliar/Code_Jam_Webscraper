#include<stdio.h>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>

using namespace std;

int main()
{
//    freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
    
    string a[4];
    int  T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
      int i,x=0,o=0,d=0;
      for(i=0; i<4; i++)
        cin>>a[i];
      for(i=0; i<4; i++)
      {
        if( ((a[i][0]=='X')+(a[i][1]=='X')+(a[i][2]=='X')+(a[i][3]=='X')+(a[i][0]=='T')+(a[i][1]=='T')+(a[i][2]=='T')+(a[i][3]=='T') )== 4) x++;
        if( ((a[0][i]=='X')+(a[1][i]=='X')+(a[2][i]=='X')+(a[3][i]=='X')+(a[0][i]=='T')+(a[1][i]=='T')+(a[2][i]=='T')+(a[3][i]=='T') )== 4) x++;
        if( ((a[i][0]=='O')+(a[i][1]=='O')+(a[i][2]=='O')+(a[i][3]=='O')+(a[i][0]=='T')+(a[i][1]=='T')+(a[i][2]=='T')+(a[i][3]=='T') )== 4) o++;
        if( ((a[0][i]=='O')+(a[1][i]=='O')+(a[2][i]=='O')+(a[3][i]=='O')+(a[0][i]=='T')+(a[1][i]=='T')+(a[2][i]=='T')+(a[3][i]=='T') )== 4) o++;
        d=d+(a[0][i]=='.')+(a[1][i]=='.')+(a[2][i]=='.')+(a[3][i]=='.');
      }
      if( ((a[0][0]=='X')+(a[1][1]=='X')+(a[2][2]=='X')+(a[3][3]=='X')+(a[0][0]=='T')+(a[1][1]=='T')+(a[2][2]=='T')+(a[3][3]=='T') )== 4) x++;
      if( ((a[0][3]=='X')+(a[1][2]=='X')+(a[2][1]=='X')+(a[3][0]=='X')+(a[0][3]=='T')+(a[1][2]=='T')+(a[2][1]=='T')+(a[3][0]=='T') )== 4) x++;
      if( ((a[0][0]=='O')+(a[1][1]=='O')+(a[2][2]=='O')+(a[3][3]=='O')+(a[0][0]=='T')+(a[1][1]=='T')+(a[2][2]=='T')+(a[3][3]=='T') )== 4) o++;
      if( ((a[0][3]=='O')+(a[1][2]=='O')+(a[2][1]=='O')+(a[3][0]=='O')+(a[0][3]=='T')+(a[1][2]=='T')+(a[2][1]=='T')+(a[3][0]=='T') )== 4) o++;
      if(x) printf("Case #%d: X won\n",t);
      else if(o) printf("Case #%d: O won\n",t);
      else if(d) printf("Case #%d: Game has not completed\n",t);
      else printf("Case #%d: Draw\n",t);
    }
    
    return 0;
}
