#include<iostream>
#include<vector>
#include<cstdio>
#include<climits>

using namespace std;

vector<unsigned long int> Prime;

bool isPrime(unsigned long long n)
{
	for(int i=0;Prime[i] * Prime[i] <= n;++i)
		if(n%Prime[i] == 0)	return false;
	return true;
}

void makePrime()
{
	Prime.push_back(2);
	Prime.push_back(3);

	for(unsigned long long i=5,gap = 2;i<100000000;i+=gap,gap = 6-gap)
	{
		if(isPrime(i))
		{
			Prime.push_back(i);
		}
	}
}

int digit,number,now;
unsigned long long answer[500][33];

void backtrack(int d,int ans[33])
{
	if(d == digit)
	{
		if(ans[digit-1] == 1 && now < number)
		{
			bool check = true;
			unsigned long long factor[9];
			for(int i=2;i<=10;++i)
			{
				unsigned long long temp = 0;
				for(int j=0;j<digit;++j)
				{
					temp*=i;
					temp = temp + ans[j];
				}
				if(isPrime(temp))
				{
					check = false;
					break;
				}
				else
				{
					for(int j=0;j<10000000;++j)
					{
						if(temp%Prime[j] ==0)
						{
							factor[i-2] = Prime[j];
							break;
						}
					}
				}
			}
			if(check)
			{
				for(int j=0;j<digit;++j)
				{
					printf("%d",ans[j]);
				}
				for(int j=0;j<9;++j)
					printf(" %llu",factor[j]);
				puts("");
				now++;
			}
			return;
		}
		else
			return;
	}
	else
	{
		for(int i=0;i<2;++i)
		{
			ans[d] = i;
			backtrack(d+1, ans);
		}
	}
}


int main()
{
	int test;
	scanf("%d",&test);
	
	makePrime();

	for(int i=1;i<=test;++i)
	{
		scanf("%d %d",&digit,&number);
	
		int temp[33];
		now = 0;

		temp[0] = 1;
		printf("Case #%d:\n",i);
		backtrack(1,temp);	
	}
	
	return 0;
}
