#include<cstdio>
int t,n,score,mx,now;
int tab[1010];
int div(int a,int b){
	int r = a/b;
	int c = a-(r*b);
	if(c)r++;
	return r;
	}
int main(){
	scanf("%d",&t);
	for(int q = 1; q <= t; ++q){
		scanf("%d",&n);
		mx = 0;
		score = 1000000000;
		for(int i = 0; i < n; ++i){
			scanf("%d",&tab[i]);
			if(tab[i]>mx)
				mx = tab[i];
			}
		for(int i = 1; i <= mx; ++i){
			now = i;
			for(int j = 0; j < n; ++j){
				now+= div(tab[j],i)-1;
				}
			if(now<score)score = now;
			}
		printf("Case #%d: %d\n",q,score);
		}
	}
