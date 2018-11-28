#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	freopen("Dsm.txt","r",stdin);
	freopen("Dout.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int k,c,s;
		cin>>k>>c>>s;
		printf("Case #%d:",t);
		for(int i=1;i<=s;i++)
		{
			printf(" %d",i);
		}
		printf("\n");
	}
	return 0;
}