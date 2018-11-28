#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include <climits>
#include<cmath>
#include<string>
#include <functional>
#include<sstream>
#include<map>
#include<set>


#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug             cout<<"";
#define     EPS              1e-8
typedef long long ll;
typedef pair<int,int> pii;
double c, f, x;
bool check(double mid)
{
	double t=0, r=2;
	while (true)
	{
		if(mid-t<EPS) return 0; 
		if((x-(r*(mid-t)))<EPS) return 1;
		t+=c/r;
		r+=f;
	}
}
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, t=1;
	cin>>tc;
	while (tc--)
	{
		cin>>c>>f>>x;
		double ans, l=0, r=x+1;
		while(r-l>EPS)
		{
			double mid=(l+r)/2;
			if(mid<=526.1904762)
				Dbug;
			if(check(mid)) ans=r=mid;
			else l=mid;
		}
		PF("Case #%d: %.7lf\n", t++, ans);
	}
	return 0;
}