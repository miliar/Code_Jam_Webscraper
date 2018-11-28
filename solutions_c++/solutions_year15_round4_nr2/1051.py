#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
double v,x;
double r[110],c[110];
tuple<double,double> s_cr[110];
bool possible()
{
	double mn=*min_element(c,c+n), mx=*max_element(c,c+n);
	if(mn<=x && mx>=x)
		return 1;
	return 0;
}
double has_equal()
{
	double rtn=0;
	for(int i=0;i<n;i++)
	{
		if(c[i]==x)
			rtn+=r[i];
	}
	// cout<<"test"<<rtn<<endl;
	return rtn;
}
int main()
{
	int T,no=1;
	cin>>T;
	while(no<=T)
	{
		cin>>n>>v>>x;
		for(int i=0;i<n;i++)
			cin>>r[i]>>c[i];
		for(int i=0;i<n;i++)
			s_cr[i]=make_tuple(c[i],r[i]);
		sort(s_cr,s_cr+n);
		for(int i=0;i<n;i++)
			tie(c[i],r[i])=s_cr[i];
		
		if(!possible())
		{
			printf("Case #%d: IMPOSSIBLE\n",no++);
			continue;
		}

		double hseql=has_equal();
		if(hseql!=0)
		{
			double ans=v/hseql;
			printf("Case #%d: %.10lf\n",no++,ans);
			continue;
		}

		double ans;
		if(n==1)
		{
			ans=v/r[0];
		}
		else if(n==2)
		{
			double temp=(r[0]*c[0]+r[1]*c[1])/(r[0]+r[1]);
			double ncc=(r[0]*c[0]-r[0]*x)/(x-c[1]);
			if(ncc>r[1])
			{
				r[0]*=r[1]/ncc;
				ncc=r[1];
			}
			ans=v/(ncc+r[0]);
		}

		printf("Case #%d: %.10lf\n",no++,ans);
	}
}
