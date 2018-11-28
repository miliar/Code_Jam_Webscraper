#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define PB push_back
#define MP make_pair
#define clr(a,b)	(memset(a,b,sizeof(a)))
#define rep(i,a)	for(int i=0; i<(int)a.size(); i++)

const int INF = 0x3f3f3f3f;
const double eps = 1E-8;

int T, cas;
int num[20000];
bool vis[20000];

int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\out.txt","w",stdout);

	cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		int n, cap;
		scanf("%d%d",&n,&cap);
		for(int i=1; i<=n; i++)
			scanf("%d",&num[i]);
		sort(num+1, num + 1 + n);
		reverse(num+1 , num + 1 + n);

		clr(vis, false);

		int ans = 0;
		for(int i=1; i<=n; i++)
		{
			if(vis[i] == true)
				continue;

			int cur = num[i];
			vis[i] = true;

			for(int j=i+1; j<=n; j++)
				if(vis[j] == false && cur + num[j] <= cap)
				{
					vis[j] = true;
					break;
				}

			ans ++;
		}
		printf("Case #%d: %d\n",cas++,ans);
	}





	return 0;
}
