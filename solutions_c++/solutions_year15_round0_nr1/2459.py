#include<bits/stdc++.h>
using namespace std;

char a[10000];

int main()
{
    freopen("nikki.in","r",stdin);
    freopen("nikki.out","w",stdout);
 int t;
 cin>>t;
 for(int kk=1;kk<=t;kk++)
 {
  int n,i,j,k,l,mneed,mstand;
  cin>>n;

  scanf("%s",a);

  mstand=0,mneed=0;

  for(i=0;i<n+1;i++)
  {
    if(i>mstand)
     {
      mneed+=(i-mstand);
      mstand+=(a[i]-'0')+(i-mstand);
     }
     else
     {
         mstand+=(a[i]-'0');
     }

  }
  cout<<"Case #"<<kk<<": "<<mneed<<endl;
 }
return 0;
}
