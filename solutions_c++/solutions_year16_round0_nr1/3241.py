#include <stdio.h>
#define maxn 202

using namespace std;

int digit[10];
FILE *fp, *fp2;
	
bool test(long long int num, long long int n)
{
	int s;
	long long int t=num;
	while(t>0)
	{
		s=t%10;
		digit[s]=1;
		t=t/10;
	}
	
	for(int i=0;i<10;i++)
	{
		if(digit[i]==0)
			return test(num+n, n);
	}
	fprintf(fp2, "%lld\n", num);
	return true;
}

int main()
{
	fp = fopen("A-large.in", "r");
	fp2 = fopen("output2.txt", "w");
	int test_case;
	fscanf(fp, "%d", &test_case);
	long long int n;
	for(int i=1;i<=test_case; i++)
	{
		for(int j=0;j<10;j++)
			digit[j]=0;
		fprintf(fp2, "Case #%d: ", i);
		fscanf(fp, "%lld", &n);
		if(n==0)
			fprintf(fp2, "INSOMNIA\n");
		else
			test(n, n); 
	}
	
	fclose(fp);
	fclose(fp2);
	return 0;
}
