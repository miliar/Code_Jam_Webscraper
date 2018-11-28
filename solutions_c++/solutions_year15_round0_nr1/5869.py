#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void count_friends(int current,int si, long *standing, int *friends);

int main(){
	int T;				//Number of cases
	int n_T=0;			//Current case
	int n_friends=0;	//Number of friends required
	long standing=0; 	//People currently standing
	char c_num[10];

	fflush(stdin);
	gets(c_num);
	T = atoi(c_num);

	while(n_T < T){
		
		int smax = 0; 
		int i=0;
		char c_si = '\0';
		int n_si = 0;
		standing = 0;
		n_friends = 0;

		printf("Case #%d: ",n_T+1);
		scanf("%d",&smax);

#ifdef DEBUG
		printf("MAXIMO: %d",smax);
#endif
		while(i < smax+1){
			scanf("%c",&c_si);
			if(c_si == ' ' || c_si== '\n')
				continue;
			else{
				c_si -= 48;
				count_friends(i,(int)c_si,&standing,&n_friends);
				i++;
			}
		}

		printf("%d\n",n_friends);

		n_T ++;
	}
}

void count_friends(int current,int si, long *standing, int *friends){
	(*standing) += si;
#ifdef DEBUG
	printf("Parametros %d, %d, %d, %d",current,si,(*standing),(*friends));
#endif
	if((*standing) < current +1){
#ifdef DEBUG
		printf(", friends++, standing++");
#endif
		(*friends)++;
		(*standing)++;
	}
#ifdef DEBUG
	printf("\n");
#endif
}

