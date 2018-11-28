#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
struct node{
int st, nu;
}a[1200], b[1200];
long long int modnum = 1000002013;
bool cmp(node a, node b)
{
	return a.st<b.st;
}
int main()
{
	int T, n, m, s, t, p;
	scanf("%d", &T);
	for (int I=1;I<=T;++I)
	{
		scanf("%d%d", &n, &m);
		long long orig = 0;
		for (int i=0;i<m;++i)
		{
			scanf("%d%d%d", &s, &t, &p);
			a[i].st=s;
			a[i].nu=p;
			b[i].st=t;
			b[i].nu=p;
			orig = orig + 1LL*(n+(n-(t-s)+1))*(t-s)/2LL%modnum*p;
			orig = orig % modnum;
		//	cout<<orig<<endl;
		}
		//cout<<orig<<endl;
		sort(a, a+m, cmp);
		sort(b, b+m, cmp);
		int ta=0, tb=0;
		long long newval = 0;
		for (int i=0;i<m;++i)
		{
			for (int j=m-1;b[i].nu>0 && j>=0;--j)
				if (a[j].nu>0 && a[j].st<=b[i].st)
				{
					int tn = min(a[j].nu, b[i].nu);
					a[j].nu-=tn;
					b[i].nu-=tn;
					newval = newval + 1LL*(n+(n-(b[i].st-a[j].st)+1))*(b[i].st-a[j].st)/2LL%modnum*tn;
					newval = newval % modnum;
					
				}
		}
		//cout<<newval<<endl;
		cout<<"Case #"<<I<<": "<< (orig+modnum-newval)%modnum <<endl;
	}
}
