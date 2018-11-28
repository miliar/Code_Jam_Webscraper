#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T,TT,i,num;
double cnt,c,f,x,t,ans;
int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&TT);
	for(T=1;T<=TT;T++){
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=1e10;
		t=0;num=0;cnt=0;
		while(t<ans){
			ans=min(ans,t+(x-cnt)/(num*f+2));
			t=t+c/(2+num*f);num++;cnt=0;
		}
		printf("Case #%d: %.7f\n",T,ans);
	}
}