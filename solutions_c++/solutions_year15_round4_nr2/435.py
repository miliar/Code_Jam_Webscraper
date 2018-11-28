#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
double tmain()
{
	int N;
	double V,X;
	scanf("%d%lf%lf",&N,&V,&X);
	vector<pair<double, double> > v;
	bool vlarge=true;
	bool vsmall=true;
	for(int i=0;i<N;i++)
	{
		double x,y;
		scanf("%lf%lf",&x,&y);
		v.push_back(make_pair(y,x));// TEMP, FLOW
		if(y+1e-9>=X) vlarge=false;
		if(y<=X+1e-9) vsmall=false;
	}
	if(vlarge || vsmall) return 1e15;
	sort(v.begin(),v.end());
	double lo=0;
	double hi=1e11;
	double usable[300];
	for(int cnt__=0;cnt__<200;cnt__++)
	{
		double mi=(lo+hi)/2;
		double ryou=V;
		for(int i=0;i<N;i++)
		{
			usable[i]=mi*v[i].second;
			if(v[i].first-X<1e-9 && X-v[i].first <1e-9)
			{
				ryou-=usable[i];
				usable[i]=0;
			}
		}
		int st=0;
		int ed=N-1;
		while(v[st].first<X && v[ed].first>X)
		{
			double time=min(
			usable[st]/(v[ed].first-X),
			usable[ed]/(X-v[st].first) );
			double flowst=time*(v[ed].first-X);
			double flowed=time*(X-v[st].first);
			ryou-=flowst+flowed;
			usable[st]-=flowst;
			usable[ed]-=flowed;
			if(usable[st]<1e-9) st++;
			if(usable[ed]<1e-9) ed--;
		}
		//printf("%lf %lf\n",mi,ryou);
		if(ryou<=0)
			hi=mi;
		else
			lo=mi;
	}
	return lo;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		double v=tmain();
		if(v>1e10) 
			printf("Case #%d: IMPOSSIBLE\n",i);
		else
			printf("Case #%d: %.15lf\n",i,v);
	}
	return 0;
}