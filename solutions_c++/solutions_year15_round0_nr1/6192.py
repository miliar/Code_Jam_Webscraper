#include<bits/stdc++.h>
using namespace std;
int main()
{
   freopen("kk.in","r",stdin);
    freopen("kk.out","w",stdout);
 int t,p;
 cin>>t;
 for( p=1;p<=t;p++)
 {
  int n,i,c1,c2;
  cin>>n;
string s;
cin>>s;

  c2=0,c1=0;

  for(i=0;i<=n;i++)
  {

    if(i>c2)
     {

      c1+=(i-c2);
      c2+=(i-c2);


     }
      c2+=(s[i]-'0');


  }
  cout<<"Case #"<<p<<": "<<c1<<endl;
 }
return 0;
}

