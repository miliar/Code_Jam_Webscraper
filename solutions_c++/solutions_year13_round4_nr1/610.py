#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <cmath>

using namespace std;
int casenum,T;
long long mod=1000002013;
struct rec
{
	long long st;
	long long num;
};
const int size=1100;
rec up[size];
rec down[size];
rec cur[size];
long long n,ans;
int x,y;
int m;
inline long long calc(long long x)
{
	return (n*x-x*(x-1)/2)%mod;
}
bool cmp(rec x,rec y)
{
	return x.st<y.st;
}
int main()
{
	freopen("gcj.in","r",stdin);
	freopen("gcj.out","w",stdout);

	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>n>>m;
		ans=0;
		for (int i=1;i<=m;i++)
		{
			cin>>up[i].st>>down[i].st>>up[i].num;
			down[i].num=up[i].num;
			ans=(ans+calc(down[i].st-up[i].st)*up[i].num)%mod;
		}
		sort(up+1,up+m+1,cmp);
		sort(down+1,down+m+1,cmp);
		memset(cur,0,sizeof(cur));
		x=y=1;
		while (y<=m)
		{
			if (x<=m&&up[x].st<=down[y].st)
			{
				cur[x].st=up[x].st;
				cur[x].num=up[x].num;
				x++;
			}
			else
			{
				long long tmp=down[y].num;
				for (int i=x-1;i>=1;i--)
				{
					long long delta=min(tmp,cur[i].num);
					ans=(ans-calc(down[y].st-cur[i].st)*delta)%mod;
					cur[i].num-=delta;
					tmp-=delta;
					if (tmp==0) break;
				}
				y++;
			}
		}
		cout<<(ans%mod+mod)%mod<<endl;
	}
	return 0;
}
