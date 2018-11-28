#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	int n;
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>n;
	int i;

	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		int j;
		int a;
		cin>>a;
		int f[100]={0};
		int cnt=0;
		for(j=1;j<=200;j++)
		{
			int t=j*a;
			while(t)
			{
				if(f[t%10]==0)
				{
					cnt++;
					f[t%10]=1;
				}
				t/=10;
			}
			if(cnt==10)break ;
		}
		if(cnt==10)cout<<j*a<<endl;
		else cout<<"INSOMNIA"<<endl;
	}
	return 0;
}
