#include<stdio.h>
FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");
int A()
{
	long long x,i,t;
	int Visit[10] = { 0, }, cnt = 0;
	fscanf(in,"%lld", &x);
	if (x == 0) {
		fprintf(out,"INSOMNIA\n");
		return 0;
	}
	for (i = 1;; i++) {
		t = x* i;
		for (;t!=0;t/=10) {
			if (Visit[t % 10] == 0)  cnt++;
			Visit[t % 10] = 1;
		}
		if (cnt == 10)break;
	}
	fprintf(out,"%lld\n",x*i);
	return 0;
}

int main()
{
	int T,i=1; fscanf(in,"%d",&T);

	while (T--) {
		fprintf(out,"Case #%d: ",i++);
		A();
	}

	return 0;
}