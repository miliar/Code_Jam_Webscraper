#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
long long a[1000001];
int arcnt[1000001];
int check(long long st, long long val)
{
	int cnt = 0;
	while(true)
	{
		if(st > val)
			return cnt;
		else
		{
			st = 2*st - 1;
			cnt++;
		}
	}
}
int main()
{
	freopen("Alarge.in","r",stdin);
	freopen("Alargeout.out","w",stdout);
	int t,n,i,cnt,x;
	long long st, ans;
	cin>>t;
	for(int z = 1;z <= t;z++)
	{
		cin>>st>>n;
		for(i = 0;i < n;i++)
		{
			cin>>a[i];
		}
		if(st == 1)
		{
			cout<<"Case #"<<z<<": "<<n<<endl;
			continue;
		}
		sort(a,a+n);
		ans = 0;
		cnt = 0;
		for(i = 0;i < n;i++)
		{
			if(a[i] < st)
			{
				st += a[i];
				arcnt[i] = 0;
				continue;
			}
			else
			{
				x = check(st,a[i]);
				arcnt[i] = x;
				cnt += x;
				while(x--)
				{
					st = 2*st -1;
				}
				st += a[i];
			}
		}
		for(i = 0;i < n;i++)
		{
			if(arcnt[i] != 0)
			{
				if(cnt > n-i)
				{
					ans += n-i;
					break;
				}
				else
				{
					ans += arcnt[i];
					cnt -= arcnt[i];
				}
					
			}
		}
		cout<<"Case #"<<z<<": "<<ans<<endl;
	}
	return 0;
}
