#include<stdio.h>
int Ans(int p[], int d){
	int ans, hite, i, max = *p;
	for(i=0; i<d; i++)
		if(p[i] > max) max = p[i];
	ans = max;
	for(hite = max; hite > 0; hite--){
		int splits = 0, newmax = 0;
		for(i=0; i < d; i++){
			int piles = (p[i]  +  hite - 1)/hite;
			int size = (p[i]  +  piles - 1)/piles;
			splits += piles - 1;
			if(size > newmax)
				newmax = size;
		}
		if(splits + newmax < ans)
			ans = splits + newmax;
	}
	return ans;
}
int main(){
	int t, i;
	scanf("%i",&t);
	for(i=1; i <= t; i++){
		int d, p[1024], j;
		scanf("%i",&d);
		for(j=0; j<d; j++)
			scanf("%i", p+j);
		printf("Case #%i: %i\n", i, Ans(p,d));
	}
}