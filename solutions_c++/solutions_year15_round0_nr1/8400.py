#include<bits/stdc++.h>
#define loop(i, n) for(int i=0; i<n; i++)
#define loop1(i, n) for(int i=1; i<=n; i++)
#define scan(k) scanf("%lld",&k)
#define scanstr(s) scanf("%s",&s)
#define print(k) printf("%lld",k)
#define println(k) printf("%lld\n",k)
#define printsp(k) printf("%lld ",k)
#define ll long long int
#define mod 1000000007
using namespace std;

int main()
{
  ll t,i,j;
  scan(t);
  for(i=1;i<=t;i++)
  {
      ll m,ans=0,count=0;
      scan(m);
      char s[m+2];
      scanf("%s",s);
      for(j=0;j<=m;j++)
      {
      	  if(j==0)
      	  {
      	  	count+=s[j]-'0';
      	  }
      	  else
      	  {
      	  	if(s[j]=='0')
      	  	{
      	  	}
      	  	else
      	  	{
      	  	
      	  	  if(count>=j)
      	  	  {
      	  	  	 count+=s[j]-'0';
      	  	  }
      	  	  else
      	  	  {
      	  	  	ans+=j-count;
      	  	  	count+=j-count;
      	  	  	count+=s[j]-'0';
      	  	  }
      	     }
      	  }
      }
      printf("Case #%d: %lld\n",i,ans);
  }


  return 0;
}

