#include<cstdio>
int t,n,added,now,act;
char s;
int tab[1001000];
int main(){
	freopen("t.in","r",stdin);
	freopen("wb.out","w",stdout);
	scanf("%d",&t);
	for(int q = 1; q <= t; ++q){
		scanf("%d",&n);
		now = 0;
		added = 0;
		for(int i = 0; i <= n; ++i){
			scanf(" %c",&s);
			act = (int)(s-'0');
			if(act>0 && now<i){
				added+= i-now;
				now+= i-now;
				}
			now+= act;
			}
		printf("Case #%d: %d\n",q,added);
		}
	}
