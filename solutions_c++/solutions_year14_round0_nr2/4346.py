#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<vector>
#include<iostream>
using namespace std;


int main()
{
	int tc,i;
	scanf("%d",&tc);
	for(i=1;i<=tc;i++)
	{
		double C,X,F,ans,t1,t2,r=2;
		scanf("%lf %lf %lf",&C,&F,&X);
		
		ans=0;
		
		t1=X/r;
		t2=C/r+X/(r+F);
		while(t1>t2)
		{
			ans+=C/r;
			r=F+r;
			t1=X/r;
			t2=(C/r)+X/(r+F);
		}
		ans+=X/r;
		printf("Case #%d: %.7lf\n",i,ans);
		
	}
	return 0;
}

