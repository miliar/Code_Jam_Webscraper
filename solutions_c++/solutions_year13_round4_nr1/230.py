#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>
#include <functional>
#include <queue>
#include <set>
#include <map>
using namespace std;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
#define SIZE(x) ((int)(x).size())
#define for0(i,n) for(int i=0;i<(n);i++)
#define for1(i,n) for(int i=1;i<=(n);i++)
#define for0r(i,n) for(int i=(n)-1;i>=0;i--)
#define for1r(i,n) for(int i=(n);i>=1;i--)
typedef long long ll;
typedef pair<int,int> pii;

const int MOD = 1000002013;

int cal(int n, int x,int p)
{
	int n1=2*n-x+1;
	if(n1%2==0)n1/=2;
	else x/=2;
	ll t = (ll)n1*x%MOD;
	return t*p%MOD;
}

void solve()
{
	int n,m;
	scanf("%d %d",&n,&m);
	map<int,int> E;
	map<int,int> L;
	set<int> S;
	int ans1=0;
	while (m--)
	{
		int o,e,p;
		scanf("%d %d %d",&o,&e,&p);
		E[o]=(E[o]+p)%MOD;
		L[e]=(L[e]+p)%MOD;
		S.insert(o);
		S.insert(e);
		ans1=(ans1+cal(n,e-o,p))%MOD;
	}

	priority_queue<pii> Q;
	int ans2=0;
	for(set<int>::iterator it=S.begin();it!=S.end();it++)
	{
		int i=*it;
		if(E[i])
		{
			Q.push(make_pair(i,E[i]));
		}
		while(L[i])
		{
			pii &t = Q.top();
			int t1=t.first;
			int t2=t.second;
			if(L[i]<t.second)
			{
				t.second -=L[i];
				t2=L[i];
			}
			else
			{
				Q.pop();
			}
			L[i]-=t2;
			ans2=(ans2+cal(n,i-t1,t2))%MOD;
		}
	}
	printf("%d\n",(ans1+MOD-ans2)%MOD);
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,TC=0;
	scanf("%d",&T);
	while (++TC<=T)
	{
		printf("Case #%d: ",TC);
		solve();
	}
	return 0;
}
