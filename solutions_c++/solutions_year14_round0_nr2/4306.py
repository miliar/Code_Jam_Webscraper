#include<stdio.h>

//FILE *input=freopen("B-large.in","r",stdin);
//FILE *output=freopen("B-large.out","w",stdout);

int main(){
	int t;
	int rt=1;
	int cnt;
	double c,f,x;
	double s;
	double ans;
	double k;
	scanf("%d",&t);

	for(;t>0;t--){
		scanf("%lf%lf%lf",&c,&f,&x);

		s=0;
		ans=x/2;
		cnt=1;
		while(1){
			s+=c/(2+f*(cnt-1));
			if(s+x/(2+f*cnt)>ans)
				break;
			ans=s+x/(2+f*cnt);
			cnt++;
		}
		printf("Case #%d: ",rt++);
		printf("%.7lf\n",ans);
	}
	return 0;
}