#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
    char a[4][4];
    ofstream fout;
    fout.open("C:\codejam_tictac.txt",ios::trunc);
    int t,i,j,no_X=0,no_O=0,no_T=0,no_d=0,flag=1,cnt=1;
  std::cin>>t;
  while(t)
  {
      for(i=0;i<4;i++)
      for(j=0;j<4;j++)
      std::cin>>a[i][j];

     for(i=0;i<4;i++)
     {
      for(j=0;j<4;j++)
      {if(a[i][j]=='X') no_X++;
      else if(a[i][j]=='O') no_O++;
      else if(a[i][j]=='T') no_T++;
      else no_d++;
      }
      if(no_X+no_T == 4 && (no_T==1||no_T==0)) {fout<<"Case #"<<cnt<<": X won"<<"\n"; cnt++;flag=0;break;}
      if(no_O+no_T == 4 && (no_T==1||no_T==0)) {fout<<"Case #"<<cnt<<": O won"<<"\n"; cnt++;flag=0;break;}
      no_X=0;no_O=0;no_T=0;
     }
     if(flag==1)
     {no_X=0;no_O=0;no_T=0;
     for(i=0;i<4;i++)
     {
      for(j=0;j<4;j++)
      {if(a[j][i]=='X') no_X++;
      else if(a[j][i]=='O') no_O++;
      else if(a[j][i]=='T') no_T++;
      else no_d++;
      }
      if(no_X+no_T == 4 && (no_T==1||no_T==0) ){fout<<"Case #"<<cnt<<": X won"<<"\n"; cnt++; flag=0;break;}
      if(no_O+no_T == 4 && (no_T==1||no_T==0)) {fout<<"Case #"<<cnt<<": O won"<<"\n"; cnt++; flag=0;break;}
      no_X=0;no_O=0;no_T=0;
     }
     }
     if(flag==1)
     { no_X=0;no_O=0;no_T=0;
         for(i=0;i<4;i++)
         {
             if(a[i][i]=='X') no_X++;
          else if(a[i][i]=='O') no_O++;
          else if(a[i][i]=='T') no_T++;
          else no_d++;

         }
      if(no_X+no_T == 4 && (no_T==1||no_T==0)) {fout<<"Case #"<<cnt<<": X won"<<"\n"; cnt++; flag=0;}
      if(no_O+no_T == 4 && (no_T==1||no_T==0)) {fout<<"Case #"<<cnt<<": O won"<<"\n"; cnt++; flag=0;}
     }
     if(flag==1)
     { no_X=0;no_O=0;no_T=0;
         for(i=0;i<4;i++)
         {
             if(a[i][3-i]=='X') no_X++;
          else if(a[i][3-i]=='O') no_O++;
          else if(a[i][3-i]=='T') no_T++;
          else no_d++;

         }
      if(no_X+no_T == 4 && (no_T==1||no_T==0)) {fout<<"Case #"<<cnt<<": X won"<<"\n"; cnt++; flag=0;}
      if(no_O+no_T == 4 && (no_T==1||no_T==0)) {fout<<"Case #"<<cnt<<": O won"<<"\n"; cnt++; flag=0;}
     }
     if(flag==1)
     {

         if(no_d==0) {fout<<"Case #"<<cnt<<": Draw"<<"\n";cnt++;}
         else {fout<<"Case #"<<cnt<<": Game has not completed"<<"\n"; cnt++;}
     }
     --t;
     std::cout<<"\n";
     no_X=0;no_O=0;no_T=0;no_d=0;flag=1;
  }
}
