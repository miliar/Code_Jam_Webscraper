#include<iostream>
#include<algorithm>

using namespace std;

struct seg
{
	long long o, e, p;
};

long long MOD = 1000002013ll;

#define oi segs[i].o
#define oj segs[j].o
#define ei segs[i].e
#define ej segs[j].e
#define pi segs[i].p
#define pj segs[j].p

seg segs[10000000];
int sc;

long long n,m;
long long ans;

long long cost(long long o, long long e)
{
	long long k = e-o;
	return n*k-k*(k-1)/2;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		cin>>n>>m;
		sc = 0;

		for(int i=0;i<m;i++)
		{
			cin>>segs[sc].o>>segs[sc].e>>segs[sc].p;
			++sc;
		}

		ans = 0;

		for(int i=0;i<sc;i++)
		{
			int csc = sc;
			for(int j=0;j<csc;j++)
			{
				if (oi<=ej&&oj<=ei)
				{
					long long mp = min(pi,pj);
					seg s1, s2;
					s1.o = min(oi,oj);
					s1.e = max(ei,ej);
					s1.p = mp;
					s2.o = max(oi,oj);
					s2.e = min(ei,ej);
					s2.p = mp;

					ans += mp*(cost(oi,ei) + cost(oj,ej) - cost(s1.o, s1.e) - cost(s2.o, s2.e));

					if (pi!=mp)
					{
						segs[sc].o = oi;
						segs[sc].e = ei;
						segs[sc].p = pi-mp;
						++sc;
					}

					if (pj!=mp)
					{
						segs[sc].o = oj;
						segs[sc].e = ej;
						segs[sc].p = pj-mp;
						++sc;
					}

					segs[i] = s1;
					segs[j] = s2;
				}
			}
		}

		cout<< "Case #" << tt << ": " << (ans % MOD) << endl;
		//cerr<< "Case #" << tt << ": " << sc-m << endl;
	}
	return 0;
}
