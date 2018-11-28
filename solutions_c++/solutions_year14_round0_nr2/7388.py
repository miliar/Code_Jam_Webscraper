#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <sstream>

using namespace std;

void solve()
{
	double c,f,x;
	scanf("%lf%lf%lf",&c,&f,&x);
	double t=0;
	double ans=x/2;
	for(int i=1;;i++)
	{
		t+=c/((i-1)*f+2);
		ans=min(ans,t+x/(i*f+2));
		if(t>ans+1e-8)break;
	}
	printf("%.7f\n",ans);
}
int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		solve();
	}
	return 0;
}
