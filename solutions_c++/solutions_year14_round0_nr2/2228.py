#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
using namespace std;
static int t,tt=1;
static double c,f,x,ans,start;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=x/2.0;start=2.0;
		double tmp=0.0;
		while(1){
		double tmp1=tmp;
		tmp1+=c/start;
		tmp=tmp1;
		start+=f;
		tmp1+=x/start;
		if(ans>tmp1) ans=tmp1;
		else break;
		}
		printf("Case #%d: %.7lf\n",tt,ans);
		++tt;
	}


	return 0;
}