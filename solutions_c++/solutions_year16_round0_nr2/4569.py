#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
  string str;
  char now;
  int test,tests,len,ans;
  freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>tests;
	for (int test=1;test<=tests;test++)
	{
	printf("Case #%d: ",test);
  cin>>str;
  len=str.length();
  ans=0;
  now=str[0];
  for (int i=1;i<len;i++)
  	if (now!=str[i]) {ans++;now=str[i];}
  if (now=='-') ans++;
  cout<<ans<<endl;
  }
  return 0;
}
