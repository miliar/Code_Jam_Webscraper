#include <vector>
#include <map>
#include <numeric>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
#define REP(i,n) for(int i=0;i<(n);i++)
const double EPS=1e-7;
int bitcnt(int n)
{
	int res=0;
	while(n)
	{
		res+=n&1;
		n>>=1;
	}
	return res;
}

int testbit(int n, int m)
{
	return (n>>m)&1;
}

double dp[300][600];
int used[300][600];

double getProb(int n, int bal, const vector<double> &v)
{
	if(n==v.size()) return bal==300;
	if(!used[n][bal])
	{
		used[n][bal]=true;
		dp[n][bal]=0;
		dp[n][bal]=v[n]*getProb(n+1, bal-1, v)+(1-v[n])*getProb(n+1, bal+1, v);
	}
	return dp[n][bal];
}

double countProbability(const vector<double> &v)
{
	memset(used,0,sizeof(used));
	return getProb(0,300,v);
}

vector<double> w;

double greedy(vector<double> v, int k)
{
	sort(v.begin(), v.end());
	double res=0;

	for(int l=0;l<=k;l++)
	{
		w.clear();
		REP(i,l)
			w.push_back(v[i]);
		REP(i,k-l)
			w.push_back(v[v.size()-1-i]);
//		w.insert(w.end(),v.begin(), v.begin()+l);
//		w.insert(w.end(),v.rbegin(), v.rbegin()+(k-l));
		res=max(res, countProbability(w));
	}

	return res;
}

double solve()
{
	int n,k;
	scanf("%d%d",&n,&k);
//	n=rand()%16+1;
//	k=rand()%n+1;
//	if(k%2!=0) k^=1;

	vector<double> v(n);
	REP(i,n)
		scanf("%lf",&v[i]);
//		v[i]=rand()%100/100.0;
//	printf("%d %d\n",n,k);
//	sort(v.begi n(), v.end());
//	REP(i,n)
//		printf("%.2lf ",v[i]);
//	puts("");
//		scanf("%lf",&v[i]);
//	double res=0;
//	vector<double> w;
//	w.reserve(k);
//	REP(i,(1<<n))
//	{
//		if(bitcnt(i)!=k) continue;
//		w.clear();
//		REP(j,n)
//			if(testbit(i,j))
//				w.push_back(v[j]);
//		res=max(res,countProbability(w));
//	}
//	REP(i,(1<<n))
//	{
//		if(bitcnt(i)!=k) continue;
//		w.clear();
//		REP(j,n)
//			if(testbit(i,j))
//				w.push_back(v[j]);
//		if(fabs(res-countProbability(w))<EPS)
//		{
//			REP(j,n)
//				if(testbit(i,j))
//					printf("%.2lf ",v[j]);
//			puts("");
//		}
//	}
//	assert(fabs(res-greedy(v,k))<EPS);
	return greedy(v,k);
}

int main()
{
	freopen("/home/knightl/B-large.in","rt",stdin);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: %.10lf\n",test,solve());
	}
	return 0;
}
