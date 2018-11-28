#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int i,j,k,n,t,cases,ans;
	string s;
	scanf("%d",&cases);
	for(t = 1;t<=cases;t++)
	{
		scanf("%d",&n);
		cin >> s;
		int cnt = 0;
		ans = 0;
		for(i = 0;i<n+1;i++)
		{
			int d = s[i]-'0';
			if(d > 0)
			{
				if(cnt < i)
				{
					ans+=(i-cnt);
					cnt+=(i-cnt);
				}

				cnt+=d;
			}
		}

		printf("Case #%d: %d\n",t,ans);
	}

	return 0;
}
