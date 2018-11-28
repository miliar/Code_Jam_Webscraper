// Problem B. Cookie Clicker Alpha

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cmath>
using namespace std;
#define ll int
#define INF 1000000000
#define debug puts("DEBUUGG")
#define vi vector<ll>
#define pii pair<ll,ll>
#define vii vector<pii>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define rep(a,b,c) for(a=b;a<c;a++)
#define repe(a,b,c) for(a=b;a<=c;a++)
#define repd(a,b,c) for(a=b-1;a>=c;a--)
#define ALL(a) a.begin(),a.end()

int solve(int tc){
	double c,f,t,cps,temp,ret;
	cps = 2.0;
	temp = 0.0;
	scanf("%lf %lf %lf",&c,&f,&t);
	do {
		ret = t/cps+temp;
		temp+=c/cps;
		cps+=f;
	} while(t/cps+temp<ret);

	printf("Case #%d: %.7lf\n",tc,ret);

}
int main(int argc, char const *argv[])
{
	/* code */
	int tc;
	scanf("%d",&tc);
	for (int i = 1; i <= tc; ++i)
	{
		solve(i);
	}
	
	return 0;
}
