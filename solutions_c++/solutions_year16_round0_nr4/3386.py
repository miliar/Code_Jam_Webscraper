#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int tests,k,c,s;
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	cin>>tests;
	for (int test=1;test<=tests;test++)
	{
		printf("Case #%d: ",test);
		cin>>k>>c>>s;
		for (int i=1;i<=k;i++)
		  printf("%d ",i);
		cout<<endl;
	}
	return 0;
}
	
	
