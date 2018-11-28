#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int p[1024];
int N;

int bina()
{
	int ret = p[N-1];
	for (int i=1; i<p[N-1]; i++) {
		int cur = i;
		for (int j=0; j<N; j++) {
			if (p[j] > i) {
				cur += (p[j]-1) / i;
			}
			if (cur > ret) {
				break;
			}
		}
		ret = min(ret, cur);
	}
	return ret;
}

void work()
{
	int T;
	
	scanf("%d",&T);
	
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%d",&N);
		for (int i=0;i<N;i++)
		{
			scanf("%d", &p[i]);
		}
		sort(p, p+N);
		
		
		
		printf("Case #%d: %d\n",cas, bina());
	
	}
}

int main()
{
	//int i;
	
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	work();

	
	return 0;
}
