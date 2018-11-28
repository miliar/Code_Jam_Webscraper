#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>

int is_pr(long long n)
{
	char str[100];
	sprintf(str,"%lld",n);
	int i,len;
	len=strlen(str);
	int ok=1;
	for (i=0;i<len;i++){
		if (str[i]!=str[len-1-i])ok=0;
	}
	return ok;
}

int main(int argc,char **argv)
{
	int t,T;
	long long A,B,As,Bs,n,n2;
	double A_,B_;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int ret=0;
		scanf("%lld %lld\n",&A,&B);
		A_=(double)A;B_=(double)B;
		As=sqrt(A_)-1;Bs=sqrt(B_)+1;
		if (As<1)As=1;
		for (n=As;n<=Bs;n++){
			n2=n*n;
			if (A<=n2 && n2<=B){
				if (is_pr(n) && is_pr(n2)){ret++;}
			}
		}
		printf("Case #%d: %d\n",t,ret);
	}
	return 0;
}
