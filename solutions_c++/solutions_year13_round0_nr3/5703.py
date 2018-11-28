#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

bool isPrime(int index)
{
	for(int i = 2;i*i <= index;i++)
	{
		if(index % i == 0)
		return false;
	}
	return true;
}

bool isHui(int index)
{
	char string[100];
	itoa(index,string,10);
	int len = strlen(string);
	int mid = len / 2;
	for(int i = 0;i < mid;i++)
	{
		if(string[i] != string[len-i-1])
		return false;
	}
	return true;
}
bool tell(int index)
{
	if(!isPrime(index) || !isHui(index))
	return false;
	return true;
}
int main()
{
	FILE* input;
	FILE* output;
	
	input = fopen("C-small-attempt1.in","r");
	output = fopen("C-small-attempt1.out","w");
	
	int t;
	fscanf(input,"%d",&t);
	for(int i = 1;i <= t;i++)
	{
		int a,b;
		fscanf(input,"%d%d",&a,&b);
		int ans = 0;
		for(int j = a;j <= b;j++)
		{
			int tmp = (int)sqrt(j);
			if(tmp*tmp != j)
			continue;
			if(isHui(j) && isHui(tmp))
			{
				ans ++;
			}
		}
		fprintf(output,"Case #%d: %d\n",i,ans);
	}
	return 0;
}
