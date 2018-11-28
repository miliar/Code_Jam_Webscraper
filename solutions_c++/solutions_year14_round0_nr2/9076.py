#include <cstdio>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

double a[1000000];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases = 0;
	scanf("%d",&cases);
	for(int casenum = 1; casenum <= cases; casenum++) {
		double c,f,x;
		printf("Case #%d: ", casenum);
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=x/2.0;
		for(int i=1;i<1000000;i++){ 
			a[i]=a[i-1]+c/(2.0+(i-1)*f);
			ans=min(ans,a[i]+x/(2.0+i*f));
		}
		printf("%.9lf\n",ans);
	}
	return 0;
}