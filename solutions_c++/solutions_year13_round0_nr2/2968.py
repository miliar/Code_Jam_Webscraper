#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int mp[110][110];
int f[110][110];
int T,n,m;
int findmin()
{
	int mi=1<<30;
	for (int i=0;i<n;++i)
	{
		for (int j=0;j<m;++j)
		{
			if (!f[i][j])
			{
				mi=min(mi,mp[i][j]);
			}
		}
	}
	if (mi==(1<<30))
	{
		return -1;
	}
	return mi;
}
int findline(int k)
{
	for (int i=0;i<n;++i)
	{
		int ok=2;
		for (int j=0;j<m;++j)
		{
			if (mp[i][j]==k || f[i][j])
			{
				if (!f[i][j] && mp[i][j]==k)
				{
					ok=1;
				}
			}
			else
			{
				ok=0;
				break;
			}
		}
		if (ok==1)
		{
			for (int j=0;j<m;++j)
			{
				f[i][j]=1;
			}
			return 1;
		}
	}
	for (int j=0;j<m;++j)
	{
		int ok=2;
		for (int i=0;i<n;++i)
		{
			if (mp[i][j]==k || f[i][j])
			{
				if (!f[i][j] && mp[i][j]==k)
				{
					ok=1;
				}
			}
			else
			{
				ok=0;
				break;
			}
		}
		if (ok==1)
		{
			for (int i=0;i<n;++i)
			{
				f[i][j]=1;
			}
			return 1;
		}
	}
	return 0;
}
int main()
{
	
	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		cin >> n >> m;
		for (int i=0;i<n;++i)
		{
			for (int j=0;j<m;++j)
			{
				cin >> mp[i][j];
			}
		}
		memset(f,0,sizeof(f));

		while (1)
		{
			int mi=findmin();
			if (mi<0)
			{
				printf("Case #%d: YES\n",kk);
				break;
			}
			int res=findline(mi);
			if (!res)
			{
				printf("Case #%d: NO\n",kk);
				break;
			}
		}
	}

	
	return 0;

}