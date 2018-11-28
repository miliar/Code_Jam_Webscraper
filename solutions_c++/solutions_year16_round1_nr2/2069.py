#include<bits/stdc++.h>
using namespace std;
long long int a[100][100],i,j,k,l,m,n,T,t=1,b[2510];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ggB.out","w",stdout);
  cin >>T;
  while(T--)
  {

      cin >> n;
      for(i=0;i<2*n-1;i++)
      {
          for(j=0;j<n;j++)
          {

              cin >> a[i][j];
              k=a[i][j];
              b[k]++;

          }
      }
     // Case #1: 3 4 6
      cout <<"Case #" <<t <<": ";
      for(i=0;i<=2500;i++)
      {

          if((b[i]!=0)&&(b[i]%2!=0))
          {

              cout << i <<" " ;
          }
      }
      cout <<endl;
      memset(b,0,sizeof(b));
      t++;
  }

    return 0;
}
