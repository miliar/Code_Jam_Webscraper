#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double cur=2,tim=0,ans=x/2;
		for(int i=0;tim<=ans;i++){
			double res = tim+x/cur;
			//printf("%lf %lf\n",tim,res);
			if(res<ans) ans = res;
			tim += c/cur;
			cur += f;
		}
		
        printf("Case #%d: %.7lf\n", tt,ans);
    }
    return 0;
}

