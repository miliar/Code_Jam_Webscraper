#include <iostream>
#include<string>
#include<algorithm>
#include<cstdio>
using namespace std;
char map[4][4];
bool flag1,flag2;
bool f1(int k)
{
  int a=0,b=0,c=0;
  for(int i=0;i!=4;++i)
   if(map[k][i]=='X') a++;
     else if(map[k][i]=='O') b++;
     else if(map[k][i]=='T') c++;
     if(a+c==4) flag1=true;
     if(b+c==4) flag2=true;
     if(a+c==4||b+c==4) return true;
     else return false;

}
bool f2(int k)
{
  int a=0,b=0,c=0;
  for(int i=0;i!=4;++i)
   if(map[i][k]=='X') a++;
     else if(map[i][k]=='O') b++;
    else if(map[i][k]=='T') c++;
     if(a+c==4) flag1=true;
     if(b+c==4) flag2=true;
     if(a+c==4||b+c==4) return true;
     else return false;
}
int main()
{
    //freopen("d://A-small-attempt3.in","r",stdin);
    //freopen("d://1.txt","w",stdout);
     int T;
     cin>>T;
     int ans;
     bool flag;
    for(int k=1;k<=T;++k)
     {
         ans=0;
         flag=false;flag1=false;flag2=false;
         getchar();
         for(int i=0;i!=4;++i)
          {
              for(int j=0;j!=4;++j)
              {
                  cin>>map[i][j];
                  if(map[i][j]=='.') ans++;
              }
               getchar();
          }
          for(int i=0;i!=4;++i)
          {
              if(f1(i)) {flag=true;break;}
              if(f2(i)){flag=true;break;}
          }
          if(ans>=13){printf("Case #%d: Game has not completed\n",k);continue;}
          if(!flag)
          {

           int a=0,b=0,c=0;
              for(int i=0;i!=4;++i)
                 {
                     if(map[i][i]=='X') a++;
                      else if(map[i][i]=='O') b++;
                      else if(map[i][i]=='T') c++;
                 }
            if(a+c==4) flag1=true;
            if(b+c==4) flag2=true;
                 a=0;b=0,c=0;
             for(int i=0;i!=4;++i)
               {
                  if(map[i][3-i]=='X') a++;
                 if(map[i][3-i]=='O') b++;
                 else if(map[i][3-i]=='T') c++;
                 }

            if(a+c==4) flag1=true;
            if(b+c==4) flag2=true;
          }

            if(flag1)printf("Case #%d: X won\n",k);
            else if(flag2) printf("Case #%d: O won\n",k);
            else {
                 if(ans==0) printf("Case #%d: Draw\n",k);
                 else   printf("Case #%d: Game has not completed\n",k);
               }
               }return 0;
}


