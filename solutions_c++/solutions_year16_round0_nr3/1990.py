#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
long long pow(long long base,long long fac)
{
	long long ans = 1;
	for (int i = 0; i < fac; ++i)
	{
		ans *= base;
	}
	return ans;
}
char baseStr[100];
bool getInit(char *a,int base)
{
	a[base] = '\0';
	for(int i = 0; i < base; i++)
	{
		a[i] = '0';
	}
	a[0] = a[base -1] = '1';
	return true;
}
bool getNext(char *a)
{
	int len = strlen(a);
	int ptr = 1;
	int endFlag = len - 2;
	while(ptr <= endFlag)
	{
		if(a[ptr] == '0')
		{
			a[ptr] = '1';
			for(int i = 1; i < ptr; i++)
			{
				a[i] = '0';
			}
			break;
		}
		ptr++;
	}
	return false;
}
int main()
{
	int T;cin>>T;
	for(int TT = 1; TT <= T; TT++)
	{
		int N,J;cin>>N>>J;
		printf("Case #%d:\n",TT);	
		long long divisors[11];
		for (int i = 2; i < 11; i++)
		{
			divisors[i] = pow(i, N / 2) + 1;
		}
		getInit(baseStr,N / 2);
		// cout<<baseStr<<endl;
		for (int i = 0; i < J; i++)
		{
			printf("%s%s",baseStr,baseStr);
			getNext(baseStr);
			for(int j = 2; j < 11; j++)
			{
				printf(" %lld",divisors[j]);
			}
			printf("\n");
		}
	}
	return 0;
}