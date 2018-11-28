#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int T,k=1;
	scanf("%d",&T);
	while(T--){
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=0.0,v=2.0;
		while(x/v>c/v+x/(v+f)){
			ans+=c/v;
			v+=f;
		}
		ans+=x/v;
		printf("Case #%d: %.7lf\n",k++,ans);
	}
	return 0;
}