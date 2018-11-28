#include <cstdio>
int cnt=0;
double fc,fp,w,t,tt;
double f=0,cps=2;
double ans;
int r;
void solve(){
	ans=0;
	cnt++;
	cps=2;
	f=0;
	scanf("%lf %lf %lf",&fc,&fp,&w);
	while(1){
		cps=2+f*fp;
		t=w/cps;
		tt=fc/cps+w/(cps+fp);
		//printf("%lf %lf\n",t,tt);
		if(tt<t){
			ans+=fc/cps;
			f++;
			continue;
		}
		else{
			ans+=t;
			break;
		}
	}
	printf("Case #%d: %.7lf\n",cnt,ans);
	return;
}
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&r);
	while(r--) solve();
	return 0;
}