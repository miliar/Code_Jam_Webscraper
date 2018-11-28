#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		double C,F,X,temp=0.0000,curr=2.0000;
		scanf("%lf %lf %lf",&C,&F,&X);
		double mini=X/curr;
		for(int i=0;i<100000;i++)
		{
			curr+=F;
			temp+=(C/(curr-F));
			mini=min(mini,temp+X/curr);
		}
		printf("Case #%d: %.8lf\n",i,mini);
	}
	return 0;
}
