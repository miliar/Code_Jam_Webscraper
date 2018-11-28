#include <stdio.h>

long long ar[50];
int t, n, j, cnt;

long long make_number(int k)
{
	long long h=1, sum=0;
	for(int i=16;i>=1;i--)
	{
		sum+=h*ar[i];
		h*=k;
	}
	return sum;
}

long long jam(long long p)
{
	int i=2;
	for(;i<=1000;i++)
	{
		if(i==p)break;
		if(p%i==0)break;
	}
	if(i<p&&i!=1001)return i;
	else return -1;
}

void printnum()
{
	for(int i=1;i<=16;i++)
	{
		printf("%d", ar[i]);
	}
	//printf(" ");
}

void adjust()
{
	for(int i=16;i>1;i--)
	{
		if(ar[i]>1)
		{
			ar[i]-=2;
			ar[i-1]+=1;
		}
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C_large_result.txt", "w", stdout);
	scanf("%d", &t);
	scanf("%d %d", &n, &j);
	puts("Case #1:");
	ar[1]=1;
	ar[16]=1;
	//printf("%lld\n", make_number(3));
	while(1)
	{
		long long c=0, w[15], p[15];
		for(int i=2;i<=10;i++)
		{
			p[i] = make_number(i);
			w[i] = jam(p[i]);
			if(w[i]>0)c++;
		}
		if(c==9)
		{
			cnt++;
			//for(int i=2;i<=10;i++)printf("%lld ", p[i]);
			//puts("");
			printnum();
			printnum();
			printf(" ");
			for(int i=2;i<=10;i++)printf("%lld ", w[i]);
			puts("");
		}
		ar[16]+=2;
		adjust();
		if(cnt>=500)break;
	}
	
	
	return 0;
}
