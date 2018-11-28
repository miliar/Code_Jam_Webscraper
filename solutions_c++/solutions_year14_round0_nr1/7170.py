/**********
rudra101 : The crownless again shall be the King !
**********/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;

int main()
{
  int Case=1,r,t,i,j,n;
freopen("A-small-attempt0.in","r",stdin);
freopen("OUTPUT.txt","w",stdout);
vector<int> v;
bool a[17]; 
  cin>>t;
while(t--)
{
  for(i=1;i<=16;i++) a[i]=false;
  cin>>r;
 for(i=1;i<=4;i++)
for(j=1;j<=4;j++)
{
 cin>>n;
if(i==r) a[n]=true;
}
cin>>r;
 for(i=1;i<=4;i++)
for(j=1;j<=4;j++)
{
 cin>>n;
if(i==r) {if(a[n]) v.push_back(n);}
}
cout<<"Case #"<<Case++<<": ";
if(v.empty()) cout<<"Volunteer cheated!\n";
else if(v.size()==1) cout<<v[0]<<"\n";
else cout<<"Bad magician!\n";
v.clear();
}
 return 0;
}


