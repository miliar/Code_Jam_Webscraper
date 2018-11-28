
#include<bits/stdc++.h>
#define debug(args...){dbg,args; cerr<<endl;}args
#define sqr(x) ( (x)*(x) )
#define Size(a) int((a).size()) 
#define pb push_back
#define mset(x,v) memset(x,v,sizeof(x))
#define all(c) (c).begin(),(c).end() 
#define SORT(x) sort(all(x))
#define tr(c,i) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
typedef long long int ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long int ull;	
using namespace std;
typedef vector<int> VI;
typedef set<int> SI;
typedef map<int,int> MII;
typedef pair<int,int> PII;
struct debugger
{
template<typename T> debugger& operator , (const T& v)
{	
	cerr<<v<<" ";	
	return *this;	
}
} dbg;
int main()
{
	int T;scanf("%d",&T);
	double c,f,x;
	for (int t = 1; t<=T; t++) 
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double time=0;
		double r=2.0;
		double p=x/r;
		double q=(c/r)+(x/(r+f));
		while(q<p) // what abt =?
		{
			time+=c/r;
			r+=f;
			p=x/r;
			q=(c/r)+(x/(r+f));
		}
		time+=p;
		printf("Case #%d: %.7lf\n",t,time);
	}
	return 0;
}

