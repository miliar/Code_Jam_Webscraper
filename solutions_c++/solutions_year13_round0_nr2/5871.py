#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <vector>
using namespace std;

const int MAXN = 300;

int a[MAXN][MAXN];
int N, M;
bool flag1[MAXN], flag2[MAXN];

void solve()
{
	scanf("%d%d", &N, &M);
	memset(flag1, false, sizeof(flag1));
	memset(flag2, false, sizeof(flag2));
	map<int,vector<pair<int,int> > > all;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M;j++)
		{
			scanf("%d", a[i]+j);
			all[-a[i][j]].push_back(make_pair(i,j));
		}
	for(auto i =all.begin(); i != all.end(); i++)
	{
		for(auto j = i->second.begin(); j != i->second.end(); j++)
			if (flag1[j->first] && flag2[j->second])
			{
				printf("NO\n");
				return ;
			}
		for(auto j = i->second.begin(); j != i->second.end(); j++)
		{
			flag1[j->first] = true;
			flag2[j->second] = true;
		}
	}
	printf("YES\n");
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		solve();
	}
	return 0;
}
