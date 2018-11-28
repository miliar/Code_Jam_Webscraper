#include <stdio.h>
#include <assert.h>
#include <vector>
#include <string>
#include <algorithm>
using std::vector;
using std::string;

double slove_small(const vector<unsigned long long>& rs,const vector<unsigned long long>& cs,unsigned long long vtotal,unsigned long long xtotal)
{
	if(rs.size() >= 3) return 0;
	if(1 == rs.size())
	{
		if(cs[0] != xtotal) return -1.0;
		return vtotal*1.0/rs[0];
	}
	if(xtotal > cs[0] && xtotal > cs[1]) return -1.0;
	if(xtotal < cs[0] && xtotal < cs[1]) return -1.0;
	if(cs[0] == cs[1])
	{
		if(xtotal != cs[0]) return -1.0;
		return (vtotal*1.0)/(rs[0]+rs[1]);
	}
	long double ret = 0;
	if(xtotal < cs[0])
	{
		long double v1 = vtotal*(cs[0]-xtotal)*1.0/(cs[0]-cs[1]);
		long double v0 = vtotal - v1;
		long double t1 = v1/rs[1],t0 = v0/rs[0];
		ret = t1 > t0?t1:t0;
	}
	else
	{
		long double v1 = vtotal*(xtotal-cs[0])*1.0/(cs[1]-cs[0]);
		long double v0 = vtotal - v1;
		long double t1 = v1/rs[1],t0 = v0/rs[0];
		ret = t1 > t0?t1:t0;
	}
	return (double)(ret);
}

int main()
{
	//freopen("E:\\GCJ2015\\R2_B_\\B-small-attempt0.in","r",stdin);
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		if(iCases == 42)
		{
			size_t debug = 0;
		}
		unsigned int n = 0;scanf("%d",&n);
		float vtotal = 0,xtotal = 0,rv = 0,cv = 0;
		scanf("%f%f",&vtotal,&xtotal);
		vector<unsigned long long> rs(n),cs(n);
		for(unsigned int i = 0;i < n;++i)
		{
			scanf("%f%f",&rv,&cv);
			rs[i] = (unsigned long long)(rv*10000+0.5);
			cs[i] = (unsigned long long)(cv*10000+0.5);
		}

		double ans = slove_small(rs,cs,(unsigned long long)(vtotal*10000+0.5),(unsigned long long)(xtotal*10000+0.5));
		if(ans < 0) printf("Case #%u: IMPOSSIBLE\n",iCases);
		else printf("Case #%u: %.9f\n",iCases,ans);
	}
	return 0;
}