#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  scanf("%d",&t);
  for(int j=1;j<=t;j++)
  {
    int k;
    scanf("%d",&k);
    char a[1004];
    scanf("%s",a);
    int curr_add=0;
    int ans=a[0]-48;
    for(int i=1;a[i]!='\0';i++)
    {
      if(a[i]=='0')
	continue;
      if(ans>=i)
      {
	ans+=(a[i]-48);
      }
      else
      {
	curr_add+=abs(ans-i);
	ans+=(a[i]-48);
	ans+=curr_add;
      }
    }
    printf("Case #%d: %d\n",j,curr_add);
  }
  return 0;
}