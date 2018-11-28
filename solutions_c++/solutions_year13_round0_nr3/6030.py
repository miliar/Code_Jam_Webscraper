#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char buff[100];
long int vet[100000];

int eh_pal(long int n){
	int i, size;
	sprintf(buff, "%ld", n);
	for(i=0; buff[i]!='\0'; i++){
		size=i;
	}
	for(i=0; i<=size; i++){
		if(buff[i]!=buff[size-i])
			return 0;
	}
	return 1;
}

int main(){

	int n, i, aux, help, j;
	long int ans, inf, sup;

	scanf("%d" ,&n);
	
	for(i=1; i<=n; i++){
		ans=0;
		scanf("%ld %ld" ,&inf ,&sup);

		for(j=inf; j<=sup; j++){
			help=sqrt(j);
			if(help*help!=j)
				continue;
			if(eh_pal(j) && eh_pal(help))
				ans++;
		}

		printf("Case #%d: %ld\n" ,i ,ans);
	}

	return 0;
}
