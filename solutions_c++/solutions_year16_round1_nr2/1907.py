#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int caseno=1;
	while(t--)
	{
		int n;
		scanf("%d",&n);
		int h[2501]={0};
		for(int i=0;i<2*n-1;i++)
		{
			for(int j=0;j<n;j++)
			{
				int integer;
				scanf("%d",&integer);
				h[integer]++;
			}
			
		}
		vector <int> result;
		for(int i=0;i<2501;i++)
		{
			if(h[i]%2!=0)
				result.push_back(i);
		}
		sort(result.begin(),result.end());
		printf("Case #%d: ",caseno++);
		for(int i=0;i<result.size();i++)
			printf("%d ",result[i]);
		printf("\n");
		memset(h,0,2501);

	}

	return 0;
}