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
long long E,R,N;
long long v[10100];
/*long long calc(long long pre,int l,int r,long long aft)
{
	if (l>r)
	{
		return 0;
	}
	int mxid=-1;
	long long maxnum=0;
	for (int i=l;i<=r;++i)
	{
		if (v[i]>maxnum)
		{
			mxid=i;
			maxnum=v[i];
		}
	}
	long long l=pre+1LL*(r-mxid+1)*R;
	long long canuse=min(pre+(mxid-l)*R,E);
	long long yl=aft-(r-mxid+1)*R;
	if (yl<0)
	{
		yl=0;
	}
	if (canuse<yl)
	{
		canuse=yl;
	}

	if (l>=aft)
	{
		return calc(pre,l,mxid-1,canuse)+canuse*v[mxid]+calc(R,mxid+1,r,aft);
	}

}*/
long long go(int now,long long pre)
{
	if (now==N)
	{
		return 0;
	}
	long long ans=0;
	for (int i=0;i<=pre;++i)
	{
		ans=max(ans,go(now+1,min(pre+R-i,E))+v[now]*i);
	}
	return ans;
}
int main()
{
	
	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);	
	int T;
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		cin >> E >> R >> N;
		for (int i=0;i<N;++i)
		{
			cin>>v[i];
		}

		long long ans=go(0,E);
		printf("Case #%d: %lld\n",kk,ans);
	}
	
	return 0;
}