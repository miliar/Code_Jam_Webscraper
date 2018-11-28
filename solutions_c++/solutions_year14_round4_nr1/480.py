#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;
const int maxn=10010;
int n,x,a[maxn];
multiset<int> S;
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&x);
		S.clear();
		for(int i=0;i<n;i++)
		{
			int x1;scanf("%d",&x1);
			S.insert(-x1);
		}
		int cnt=0;
		while(!S.empty())
		{
			int x1=*S.begin();
			S.erase(S.begin());
			multiset<int>::iterator p=S.lower_bound(-x1-x);
			if(p!=S.end()) S.erase(p);
			++cnt;
		}
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}
