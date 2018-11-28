#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
int main()
{
 int t,cnt=0;
cin>>t;
while(t--)
{
 cnt++;vector <string> v,w;int i,j,f=0;string s,win=" ";
for(i=0;i<4;i++)
{
 v.push_back("    ");
 w.push_back("    ");
}
v.push_back("");w.push_back("");
 for(i=0;i<4;i++)
 { 
 cin>>s;
 v[i]=s;
 }

 for(i=0;i<5;i++)
   {
  for(j=0;j<5;j++)
   {
    w[i][j]=v[j][i];if(v[j][i]=='.') f=1;
   }
  }

for(i=0;i<=3;i++)
{
 v[4]+=v[i][i];
 w[4]+=v[i][3-i];
}
//cout<<"SS"<<v[4]<<"SS"<<"\n"<<"SS"<<w[4]<<"SS";
for(i=0;i<5;i++)
 { 
  if(v[i][0]=='X')
  {
   if(v[i]=="XXXX" || v[i]=="XXXT" || v[i]=="XXTX" || v[i]=="XTXX" || v[i]=="TXXX")
    {
    win="X";
     break;
    }
  }
  else if(v[i][0]=='O')
  {
   if(v[i]=="OOOO" || v[i]=="OOOT" || v[i]=="OOTO" || v[i]=="OTOO" || v[i]=="TOOO")
    {
      win="O";
     break;
    }
  }
  if(w[i][0]=='X')
  {
   if(w[i]=="XXXX" || w[i]=="XXXT" || w[i]=="XXTX" || w[i]=="XTXX" || w[i]=="TXXX")
    {
     win="X";
     break;
    }
  }
  else if(w[i][0]=='O')
  {
   if(w[i]=="OOOO" || w[i]=="OOOT" || w[i]=="OOTO" || w[i]=="OTOO" || w[i]=="TOOO")
    {
     win="O";
     break;
    }
  }
}
cout<<"Case #"<<cnt<<":"<<" ";
if(win==" " && f==0)
cout<<"Draw"<<"\n";
else if(win==" ")
cout<<"Game has not completed"<<"\n";
else
{
cout<<win<<" "<<"won"<<"\n";
}
}
return 0;
}

