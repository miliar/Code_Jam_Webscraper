#include<iostream>
#include<fstream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>

using namespace std;

long long int n,m,a[128],ans,minn;

void read ()
{
  int i;
  scanf ("%lld%lld",&m,&n);
  for(i=0;i<n;i++)
  scanf ("%lld",&a[i]);
}

void solve ()
{
  long long int i,sum=m,ansp=0;
  sort (a,a+n);
  if(m==1){ans=n;return ;}
  for (i=0;i<n;i++)
  {
    ///printf ("%d\n",sum);
    ansp=0;
    while (1)
    {
      if (sum>a[i]){sum+=a[i];break;}
      sum+=(sum-1);
      ansp++;
    }
    if(ans+(n-i)<minn)minn=ans+(n-i);
    ///if(ansp>=(n-i)){ans+=(n-i);break;}
    ans+=ansp;
  }
}

int main ()
{
  long long int t,t1;
	///freopen("input.txt", "r", stdin);
  ///freopen("output.txt", "w", stdout);
  scanf ("%lld",&t);
  for(t1=0;t1<t;t1++)
  {
    ans=0;
    read ();
    minn=n;
    solve ();
    if (ans>minn)ans=minn;
    printf ("Case #%lld: %lld\n",t1+1,ans);
  }
	return 0;
}