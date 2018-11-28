#include <stdio.h>
#include <string.h>
#include <math.h>

int del(char a[], char temp[], int nu[])
{
	int len = strlen(a);
	int i;
	int k = 0;
	for (i = 0; i < len; i++) {
		int j=i;
		for (j = i; j<len; j++){
		  if (((j != len -1) && a[j] != a[j+1]) || j == len-1) {
		  	temp[k] = a[j];
		  	nu[k++] = j - i+1;
		  	break;
		  }
		}
		i = j;
	}
	temp[k]='\0';
	return k;
}
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int c = 0,t,n;
	scanf("%d", &t);
	while (c++ < t)
	{
		char a[105][105];
		char temp[105][105];
		int  nu[105][105];
		scanf("%d", &n);
		int i;
		int k;
		int an[105];
		for (i = 0; i < n; i++) {
			scanf("%s", a[i]);
			k = del(a[i], temp[i], nu[i]);
			
		}
		int flag = 0;
		for (i = 0; i < n-1; i++) {
			if ( strcmp(temp[i], temp[i+1]) != 0) {
				flag = 1;break;
			}
		}
		if (flag == 1) {
			printf("Case #%d: Fegla Won\n", c);
			continue;
		}
		
		int ans = 100000000;
		int tmp = 0;
		int l= 0;
		int j= 0;
		for (j = 0; j<k;j++) an[j] = 0;
		for(i = 0; i < k; i++) {
		for(j = 0; j< n; j++)
		 an[i] += nu[j][i];
		 an[i] = an[i]/n;
		}
		

		for(i = 0; i < n; i++) {
			for (j = 0; j < k; j++) {
				tmp += fabs(nu[i][j]-an[j]);
		}		
	}
	
	printf("Case #%d: %d\n",c, tmp);
	}
 return 0;
}