#include <iostream>
#include<string.h>
#include<cstdio>
using namespace std;

int main() {
	// your code goes here
	int t,n,len,c=1;
	scanf("%d",&t);
	while(t--)
	{
	 scanf("%d",&n);
	 char str[n+2];
	 scanf("%s",str);
	 int ans=0;
	 int s=(str[0]-'0');
	 for(int i=1;i<=n;i++)
	 {
	  if(i>s)
	  {
	      ans+= i-s;
	      s+=i-s;
	  }
	  s+=str[i]-'0';
	 }
	 printf("Case #%d: %d\n",c,ans);
	 c++;
	}
	return 0;
}
