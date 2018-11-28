#include <stdio.h>
#include <map>
using namespace std;

int main()
{
	int n,k;
	scanf("%d",&n);
	for(int I=1; I<=n; ++I)
	{
		std::map<int, int> m;
		scanf("%d",&k);
		for(int i=0; i<(k*2-1)*k; ++i)
		{
			int r;
			scanf("%d",&r);
			if(m.find(r)==m.end())
				m[r]=1;
			else
				++m[r];
		}
		printf("Case %d :", I);
		for(std::map<int, int>::iterator it = m.begin(); it!=m.end(); ++it)
		{
			if(it->second%2==1)
				printf(" %d", it->first);
		}
		printf("\n");
	}
	return 0;
}