#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
const int oo=1073741819;
using namespace std;
int T;
double C,F,X;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for (int Case=1;T;T--,Case++) {
		printf("Case #%d: ",Case);
		scanf("%lf%lf%lf\n",&C,&F,&X);
		double ans=oo;
		double tot=0;
		for (int i=0;;i++) {
			double sum=0;
			//for (int j=1;j<=i;j++)
			//	sum+=C/(2+(j-1)*F);
			sum+=tot,tot+=C/(2+i*F);
			sum+=X/(2+i*F);
			if (sum>ans) break;
			ans=sum;
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}
