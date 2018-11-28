#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include <iomanip>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<stack>
#include<cstring>
#include<map>
#include<set>
using namespace std;
#define MOD 1000000007
struct data
{
	double r;
	double c;
}d[111];
bool cmp(data d1,data d2)
{
	return d1.c<d2.c;
}
int main()
{
	int t,T;
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B.out","wt",stdout);
	double v,x;
	int i,n;
	double vc1,vc2,vcsum;
	double v1,v2,vsum;
	double t2,tt;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cout<<"Case #"<<t<<": ";
		cin>>n;
		cin>>v>>x;
		for(i=0;i<n;i++)
		{
			cin>>d[i].r>>d[i].c;
			d[i].c-=x;
			d[i].c*=d[i].r;
		}
		sort(d,d+n,cmp);
		if((d[0].c<0&&d[n-1].c<0)||(d[0].c>0&&d[n-1].c>0))
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		v1=v2=vsum=0;
		vc1=vc2=vcsum=0;
		for(i=0;i<n;i++)
		{
			if(d[i].c<0)
			{
				vc1-=d[i].c;
				v1+=d[i].r;
			}
			else if(d[i].c>0)
			{
				vc2+=d[i].c;
				v2+=d[i].r;
			}
			vsum+=d[i].r;
			vcsum+=d[i].c;
		}
		if(vc1>vc2)
		{
			vc1=vc2;
			v1=v2;
		}
		if(vcsum<0)
			vcsum=-vcsum;
		if(vcsum==0)
		{
			tt=v/(vsum);
		}
		else if(vc1==0)
		{
			vsum=0;
			for(i=0;i<n;i++)
				if(d[i].c==0)
					vsum+=d[i].r;
			tt=v/(vsum);
		}
		else
		{
			t2=v/(vsum+v1*vcsum/vc1);
			tt=t2*(1+vcsum/vc1);
		}
		cout<<setiosflags(ios::fixed)<<setprecision(9)<<tt<<endl;
	}
	//system("pause");
    return 0;
}