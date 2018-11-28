#include <cstdio>
#include <algorithm>
#include <vector>
#include<set>
#include<iostream>
#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;
const int MAXN = 15813;
const int T=1024;

vector<int> drz(2*T);
vector<pii> V;
void zazn(int a)
{
	a+=T;
	drz[a]=1;
	a/=2;
	while(a)
	{
		drz[a]=drz[2*a]+drz[2*a+1];
		a/=2;
	}
}
int sum(int a,int b)
{
	a+=T;b+=T;
	int wyn=0;
	while(a<=b)
	{
		if(a%2){wyn+=drz[a];a++;}
		if(b%2==0){wyn+=drz[b];b--;}
		a/=2;b/=2;
	}
	return wyn;
}
int solve()
{
	int n,a;
	V.clear();
	drz.clear();
	drz.resize(2*T,0);
	scanf("%d",&n);	
	fru(i,n){scanf("%d",&a);V.push_back(pii(a,i));}
	sort(V.begin(),V.end());
	int ans=0;
	fru(i,n)
	{
		int p1=sum(0,V[i].y),p2=sum(V[i].y,T);
	//	printf("mam %d %d %d\n",V[i].y,p1,p2);
		ans+=min(V[i].y-p1,n-V[i].y-p2-1);
	//	printf("ans %d\n",ans);
		zazn(V[i].y);
	}
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	fru(i,t)printf("Case #%d: %d\n",i+1,solve());
    return 0;
}
