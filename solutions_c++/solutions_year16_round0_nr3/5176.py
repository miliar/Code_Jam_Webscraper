#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *fin=fopen("C-large-practice.in","r");
	FILE *fout=fopen("C-large-practice.out","w");
	int t,i,j;
	int n,x,k;
	double a,b,c;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(fin,"%d%d%d",&n,&x,&k);
		fscanf(fin,"%lf%lf%lf",&a,&b,&c);
		a=a/100;
		b=b/100;
		c=c/100;
		map<int,double> newm;
		map<int,double> m;
		newm[x]=1.0;
		for(j=0;j<n;j++)
		{
			for(map<int,double>::iterator it=newm.begin();it!=newm.end();it++)
			{
				if(m.find(it->first&k)==m.end())
				m[it->first&k];
				m[it->first&k]+=it->second*a;
				if(m.find(it->first|k)==m.end())
				m[it->first|k];
				m[it->first|k]+=it->second*b;
				if(m.find(it->first^k)==m.end())
				m[it->first^k];
				m[it->first^k]+=it->second*c;
			}
			newm.clear();
			for(map<int,double>::iterator it=m.begin();it!=m.end();it++)
			{
				newm[it->first]=it->second;
			}
			m.clear();
		}
		double ans=0.0;
		for(map<int,double>::iterator it=newm.begin();it!=newm.end();it++)
		{
			if(it->second<=0.000000000001)
			continue;
			ans+=(it->first*it->second);
		}
		newm.clear();
		m.clear();
		fprintf(fout,"Case #%d: %.10lf\n",i,ans);
	}
	return 0;
}
