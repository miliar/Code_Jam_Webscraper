#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

#define INT_NUM 5

void main()
{
	int space=0;

	int t;
	int i,j,k;
	int n,m;
	int result,num;

	char s[17];
	char r[17];
	long long int p;

	printf("%d ", sizeof(p));

	for(i=0;i<=10000000;i++) {
	//for(i=0;i<=1;i++) {
		sprintf(s,"%d",i);
		//printf("%s\n",s);

		int len = strlen(s);
		char *ptr = s + len;
		char *ptr_r = r;
		while(ptr-- != s) {
			*ptr_r++ = *ptr;
		}
		*ptr_r = 0;		
		//printf("%s\n",r);
		if(strcmp(s,r)==0) {
			p=i*i;
                        printf("\n%d*%d=%I64d",i,i,p);                       

		}

	}
}
