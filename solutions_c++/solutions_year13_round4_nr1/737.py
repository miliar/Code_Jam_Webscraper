#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <assert.h>

using std::vector;
using std::map;
using std::set;

struct data_t
{
	unsigned long long incount;
	unsigned long long outcount;
public:
	data_t():incount(0),outcount(0) { ; }
};

struct travel_t
{
	unsigned long long	startpoint;
	unsigned long long	endpoint;
	unsigned long long	count;
};

unsigned int calc_cost(unsigned int n,const vector<travel_t>& data)
{
	static const unsigned int module = 1000002013;
	unsigned int s = 2*n + 1;
	unsigned long long ret = 0;
	for(size_t i = 0,size = data.size();i < size;++i)
	{
		unsigned int t = data[i].endpoint - data[i].startpoint;
		unsigned long long z = t;z *= (s - t);z /= 2;
		z %= module;z *= data[i].count;z %= module;
		ret += z;ret %= module;
	}
	return (unsigned int)(ret);
}

void get_stations(const set<unsigned int>& table,vector<unsigned int>& i2station,map<unsigned int,size_t>& station2i)
{
	size_t p = 0;
	for(set<unsigned int>::const_iterator it = table.begin();it != table.end();++it,++p)
	{
		i2station.push_back(*it);
		station2i[*it] = p;
	}
}

int main()
{
	static const unsigned int module = 1000002013;
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int n = 0,m = 0;scanf("%d%d",&n,&m);
		vector<travel_t> travels(m);
		unsigned int o = 0,e = 0,p = 0;
		set<unsigned int> stations_table;
		for(unsigned int i = 0;i < m;++i)
		{
			scanf("%d%d%d",&o,&e,&p);
			travels[i].startpoint = o;
			travels[i].endpoint = e;
			travels[i].count = p;
			stations_table.insert(o);
			stations_table.insert(e);
		}
		unsigned int expect = calc_cost(n,travels);

		vector<unsigned int> i2station;
		map<unsigned int,size_t> station2i;
		get_stations(stations_table,i2station,station2i);

		vector<data_t> datas(i2station.size());
		for(unsigned int i = 0;i < m;++i)
		{
			size_t u = station2i[travels[i].startpoint];
			size_t v = station2i[travels[i].endpoint];
			datas[u].incount += travels[i].count;
			datas[v].outcount += travels[i].count;
		}

		vector<travel_t> opts;
		for(size_t i = 0,size = datas.size();i < size;++i)
		{
			data_t& r = datas[i];
			if(r.incount > r.outcount) { r.incount -= r.outcount;r.outcount = 0; }
			else { r.outcount -= r.incount;r.incount = 0; }

			if(r.outcount > 0)
			{
				assert(i > 0);
				for(size_t k = i - 1;k != (size_t)(-1);--k)
				{
					if(datas[k].incount == 0) continue;
					if(datas[k].incount >= r.outcount)
					{
						datas[k].incount -= r.outcount;
						travel_t zz;
						zz.startpoint = i2station[k];
						zz.endpoint = i2station[i];
						zz.count = r.outcount;
						opts.push_back(zz);

						break;
					}
					else
					{
						r.outcount -= datas[k].incount;
						travel_t zz;
						zz.startpoint = i2station[k];
						zz.endpoint = i2station[i];
						zz.count = datas[k].incount;
						opts.push_back(zz);
						datas[k].incount = 0;
					}
				}
			}
		}

		unsigned int real = calc_cost(n,opts);
		//printf("%d %d\n",expect,real);

		unsigned long long ans = module + expect;ans -= real;
		ans %= module;
		printf("Case #%u: %u\n",iCases,(unsigned int)(ans));
	}
	return 0;
}