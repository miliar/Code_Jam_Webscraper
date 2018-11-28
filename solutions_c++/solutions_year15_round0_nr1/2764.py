#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
//	freopen("in","r",stdin);
  //  freopen("out","w",stdout);
	int T;
	cin>>T;
	int k=1;
	while(T--)
	{
	int n,ans=0,cou=-1;
	char a[1005];
	cin>>n;
	for(int i=0;i<=n;i++)
		cin>>a[i];
	cou=a[0]-'0';
	for(int i=1;i<=n;i++)
	{
		if(a[i]!='0'&&i>cou)
		{
			ans+=i-cou;
			cou+=ans+a[i]-'0';
		}
		else
			cou+=a[i]-'0';
	}		
	printf("Case #%d: ",k++);
	printf("%d\n",ans);
	}
	return 0;
}


