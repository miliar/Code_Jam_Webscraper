#include <cstdio>
#include <cstdlib>

int compare(const void *a, const void *b)
{
	if(*(double*)a > *(double*)b)
		return 1;
	return -1;
}

int main()
{
	int t, caseNum = 1, i, j, n, count1, count2;
	double w[2][1005];
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		for(i = 0;i < 2;i++)
			for(j = 0; j < n;j++)
				scanf("%lf", &w[i][j]);
		qsort(w[0], n, sizeof(double), compare);
		qsort(w[1], n, sizeof(double), compare);
		//for(j = 0; j < n;j++)
		//	printf("%lf ", w[0][j]);
		i = j = count2 = 0;
		while(i < n && j < n){
			if(w[0][i] < w[1][j]){
				i++;
				j++;
			}else{
				j++;
				count2++;
			}
		}
		i = j = count1 = 0;
		while(i < n && j < n){
			if(w[0][j] > w[1][i]){
				i++;
				j++;
			}else{
				j++;
				count1++;
			}
		}
		printf("Case #%d: %d %d\n", caseNum++, n - count1, count2);
	}
	return 0;
}
