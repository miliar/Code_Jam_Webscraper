#include <bits/stdc++.h>
using namespace std;
vector<int>v;
int main() 
{
	int i,j,k,l,n,m,t,du;
	scanf("%d",&t);
	for(int hg=1;hg<=t;hg++)
	{
		printf("Case #%d: ",hg);
		v.clear();
		scanf("%d",&du);
		for(i=0;i<du;i++)
		{
			scanf("%d",&l);
			v.push_back(l);
		}
		sort(v.begin(),v.end());
		int ans = 9;
		for(int i = 1; i <=9; ++i)
		{
			int curr = i;
			for(int j = 0; j < du; ++j)
			{
				if(v[j]>i)
				{
					curr+= v[j]/i;
					if(v[j]%i == 0)
						curr--;
				}
			}
			ans = min(ans, curr);
		}
		printf("%d\n",ans);
	}
	return 0;
}
