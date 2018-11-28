#include <stdio.h>
#include <string.h>
#include <stdlib.h>

double naomi[1001], ken[1001];
int n, mark[1001];

int war(){
	memset(mark,0,sizeof(mark));
	int count = 0, i, j = 0;
	for(i=0; i<n; i++){
		while(j < n){
			if(mark[j] == 0 && ken[j] > naomi[i]){
				count++;
				mark[j] = 1;
				break;
			}
			j++;
		}
	}
	return n - count;
}

int dewar(){
	memset(mark,0,sizeof(mark));
	int count = 0, i = 0, j, p;
	while(naomi[i]<ken[0] && i<n)mark[i++] = 1;
	p = i; j = n-1;
	for(i=n-p-1; i>=0; i--){
		//for(j=n-1; j>=p; j--){
		if(ken[i] < naomi[j]){
			count++;
			j--;
		}
		//}
	}
	return count;
}

int cmp( const void *a , const void *b ){
	return *(double *)a > *(double *)b ? 1 : -1;
}

double min(double a, double b){return a<b?a:b;}

int main(){

  freopen("D-large.in", "r", stdin);
  freopen("test.txt", "w", stdout);
	
//	qsort(map,n,sizeof(map[0]),cmp);
//	memset(map,0,sizeof(map));
	int i, j, t;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		scanf("%d", &n);
		for(j=0; j<n; j++)scanf("%lf",&naomi[j]);
		for(j=0; j<n; j++)scanf("%lf",&ken[j]);
		qsort(naomi,n,sizeof(naomi[0]),cmp);
		qsort(ken,n,sizeof(ken[0]),cmp);
		
/*		for(j=0; j<n; j++)printf("%lf ",naomi[j]);
		printf("\n");
		for(j=0; j<n; j++)printf("%lf ",ken[j]);
		printf("\n");
*/
		printf("Case #%d: %d %d\n", i+1, dewar(), war());
	}
	return 0;
}