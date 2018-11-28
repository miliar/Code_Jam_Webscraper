#include <iostream>
#include <cstdio>
using namespace std;

long long int count(long long int n)
{
	int k = 0;
	long long int i = 0;
	long long int curr;
	long long int a[10] = { 0 };
	int j = 0;
	while (k == 0)
	{
		i++;
		curr = n * i;
		while (curr != 0)
		{
			a[curr % 10]++;
			curr = curr / 10;
		}
		k = 1;
		for (j = 0; j < 10; j++)
			if (a[j] == 0)
				k = 0;
	}
	return i*n;
}



int main() {
	long long int n;
	int i;
	int t;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%lld",&n);
        printf("Case #%d: ",i);
		if (n == 0) printf("INSOMNIA");
		else
		{
			printf("%lld",count(n));
		}
        printf("\n");
	}
	
}
