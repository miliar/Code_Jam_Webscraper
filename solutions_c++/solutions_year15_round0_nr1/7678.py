
/**Bismillahir Rahmanir Rahim
   In the name of ALLAH, most gracious, most merciful */
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  long j,tc;
  cin>>tc;
  for(j=1;j<=tc;j++)
  {
      long l,r=0,d,x,i;
      string a;
      cin>>l>>a;
      x=a[0]-48;
      for(i=1;i<=l;i++)
      {
          if(x<i)
          {
              d=i-x;
              r=r+d;
              x=i;
          }
            x=x+a[i]-48;
      }
      cout<<"Case #"<<j<<": "<<r<<endl;
  }

    return 0;
}
