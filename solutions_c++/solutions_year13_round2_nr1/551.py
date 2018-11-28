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
long long l[1010];
long long a;
int n;
int main()
{
	
	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);
	int T;	
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		cin >> a >> n;
		for (int i=1;i<=n;++i)
		{
			cin>>l[i];
		}
		long long sum=a;
		int nn=0;
		int ans=1<<30;
		sort(l+1,l+1+n);
		int ok=1;
		for (int i=1;i<=n;++i)
		{
			if (l[i]<sum)
			{
				sum+=l[i];
			}
			else
			{
				ans=min(ans,nn+(n+1-i));
				if (sum==1)
				{
					ok=0;
					break;
				}
				while (sum<=l[i])
				{
					nn++;
					sum+=(sum-1);
				}
				sum+=l[i];
			}
		}
		if (ok)
		{
			ans=min(ans,nn);
		}		
		printf("Case #%d: %d\n",kk,ans);
	}
	return 0;
}