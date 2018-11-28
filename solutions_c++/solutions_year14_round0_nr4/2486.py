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

int n,T;
int a[1111], b[1111];
double f;

int main()
{
	freopen("D:\\D-large.in","r",stdin);
	freopen("D:\\out.txt","w",stdout);

	int cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(int i=1; i<=n; i++)
		{
			scanf("%lf",&f);
			f += 0.000005;
//			cout<<f<<endl;
			a[i] = (int)(f * 100000);
		}
		for(int i=1; i<=n; i++)
		{
			scanf("%lf",&f);
			f += 0.000005;
//			cout<<f<<endl;

			b[i] = (int)(f * 100000);
		}

		sort(a+1,a+1+n);
		reverse(a+1,a+1+n);
		sort(b+1,b+1+n);
		reverse(b+1,b+1+n);

		int ans1 = 0, ans2 = 0;

		deque<int> ta, tb;
		for(int i=1; i<=n; i++)
		{
			ta.push_back(a[i]);
			tb.push_back(b[i]);
		}

		for(int i=1; i<=n; i++)
		{
			int sz = n + 1 - i;
			if(ta[sz-1] <= tb[sz-1])
			{
				ta.pop_back();
				tb.pop_front();
			}
			else
			{
				ans1++;
				ta.pop_back();
				tb.pop_back();
			}
		}

		bool vis[1111];
		clr(vis, false);
		for(int i=1; i<=n; i++)
		{
			bool fd = false;
			for(int j=n; j>=1; j--)
				if(b[j] > a[i] && vis[j] == false)
				{
					b[j] = true;
					fd = true;
					break;
				}

			if(fd == false)
			{
				ans2++;
				for(int j=n; j>=1; j--)
					if(vis[j] == false)
					{
						vis[j] = true;
						break;
					}
			}
		}

		printf("Case #%d: %d %d\n",cas++,ans1,ans2);

	}

	return 0;
}
