#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<iostream>
#include<map>
using namespace std;
const int N = 1005;
map<int,int>lzs;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int n,i,m;
		scanf("%d%d",&n,&m);
		lzs.clear();
		for(i=1;i<=n;i++)
		{
			int v;
			scanf("%d",&v);
			lzs[v]++;
		}
		int ret=0,le=n;
		while(le>0)
		{
			int v=lzs.rbegin()->first;
			le--;
			//printf("v:%d \n",v);
			lzs[v]--;
			if(!lzs[v])lzs.erase(v);
			map<int,int>::iterator it=lzs.lower_bound(m-v+1);
			if(it!=lzs.begin())
			{
				it--;
				int vv=it->first;
				//printf("vv:%d \n",vv);
				lzs[vv]--;
				if(!lzs[vv])lzs.erase(vv);
				le--;
			}
			ret++;
		}
		printf("%d\n",ret);
	}
	return 0;
}