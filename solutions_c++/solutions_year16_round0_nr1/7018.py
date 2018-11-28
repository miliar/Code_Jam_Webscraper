#include <iostream>
# include <cstdio>
using namespace std;
int main()
{

   int t;
   cin>>t;
   for (int j=1;j<=t;j++)
   {
      int temp=0,a[10]={0},c=0,ans=0,m;
      cin>>m;
      int n=m;
      if (n==0)
        {
          printf("Case #%d: INSOMNIA\n",j);
          continue;
        }
        int i=2;
      while (c!=10)
      {
        temp=n%10;
        if (a[temp]==0)
        {
            a[temp]=1;
            c++;
        }
        n=n/10;
        if (c==10)
      {
          printf("Case #%d: %d\n",j,ans);break;
      }
        if (n==0)
        {
            n=i*m;
            i++;
            ans=n;
        }
      }
   }
	return 0;
}
