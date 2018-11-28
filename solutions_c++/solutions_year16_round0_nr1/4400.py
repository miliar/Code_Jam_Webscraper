#include <stdio.h>

FILE *in=fopen("A-large.in", "r");
FILE *out=fopen("output.txt", "w");

long long int n;
int A[10], cnt;

int main()
{
	int t;
	fscanf(in, "%d", &t);
	for (int tt=1; tt<=t; tt++){
		fscanf(in, "%lld", &n);
		fprintf(out, "Case #%d: ", tt);
		for (int i=0; i<10; i++) A[i]=0;
		cnt=0;
		for (int i=1; i<=100; i++){
			long long int k=n*i;
			for (; k!=0; k/=10){
				if (A[k%10]==0) cnt++;
				A[k%10]=1;
			}
			if (cnt==10){
				fprintf(out, "%lld\n", n*i);
				break;
			}
		}
		if (cnt!=10) fprintf(out, "INSOMNIA\n");
	}
	return 0;
}
