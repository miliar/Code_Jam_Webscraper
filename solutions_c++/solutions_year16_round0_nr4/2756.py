#include<iostream>
#include<cstdio>
using namespace std;

int n,k,c;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		cin>>n>>k>>c;
		printf("Case #%d:",i);
		for(int j=1;j<=n;++j)
			cout<<' '<<j;
		cout<<endl;
	}
	return 0;
}
