#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){
	if((*(double *)a) == (*(double *)b))
		return 0;
	else if((*(double *)a) > (*(double *)b))
		return 1;
	else
		return -1;
}

void solve(){
	int i, j, n, nken;
	int countDW=0, countW=0;
	double naomi[1024], ken[1024];

	scanf("%d", &n);
	for(i=0;i<n;i++)
		scanf("%lf", &naomi[i]);
	for(i=0;i<n;i++)
		scanf("%lf", &ken[i]);

	qsort(naomi, n, sizeof(double), compare);
	qsort(ken, n, sizeof(double), compare);

	for(i=j=0;i<n;j++){
		while(i<n && naomi[i++] < ken[j]);
		if(i<n)
			countDW++;
		else if(naomi[n-1] >= ken[j])
			countDW++;
	}
	for(i=j=0;i<n;j++){
		while(i<n && ken[i++] < naomi[j]);
		if(i<n)
			countW++;
		else if(ken[n-1] >= naomi[j])
			countW++;
	}
	printf("%d %d", countDW, n-countW);
}

int main(int argc, char *argv[]){
	int i, t;
	scanf("%d", &t);
	for(i=0;i<t;i++){
		printf("Case #%d: ", i+1);
		solve();
		printf("\n");
	}
	return 0;
}


