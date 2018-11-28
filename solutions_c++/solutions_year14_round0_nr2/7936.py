#include <stdio.h>
int main(){
	int t;
	double c, f, x;
	scanf("%d", &t);
	for(int i=1;i<=t;++i){
		scanf("%lf%lf%lf", &c, &f, &x);
		double reward_pre = x/2.0f, reward_nxt;
		int cnt = 0;
		do{
			++cnt;
			reward_nxt = 0;
			for(int j=0;j<cnt;++j){
				reward_nxt += c/(2.0f+(double)(f*j));
			}
			reward_nxt += x/(2.0f+(double)(f*cnt));
			if(reward_pre < reward_nxt) break;
			reward_pre = reward_nxt;
		}while(true);
		printf("Case #%d: %.7f\n", i, reward_pre);
	}
}