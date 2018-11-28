#include<bits/stdc++.h>
using namespace std;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("kn","w",stdout);
  int t,flag,n,i,a,b,j,ctr,n1;
  cin>>t;
  for(i=1;i<=t;i++)
  {
    int s[10]={0};
    cin>>n;
    n1=n;
    if(n==0)
    {
      printf("Case #%d: INSOMNIA\n",i);
      continue;
    }
    ctr=2;
    while(1)
    {
      a=n;
      while(a!=0)
      {
        b=a%10;
        s[b]=1;
        a=a/10;
      }
      flag=0;
      for(j=0;j<=9;j++)
      {
        if(s[j]==0)
        {
          flag=1;
          break;
        }
      }
      if(flag==1)
      {
        n=n1*ctr;
        ctr++;
      }
      else
      {
        printf("Case #%d: %d\n",i,n);
        break;
      }
    }
  }
  return 0;
}
