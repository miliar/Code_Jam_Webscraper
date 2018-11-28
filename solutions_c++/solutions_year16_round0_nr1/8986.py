#include <iostream>

using namespace std;

long long int solve(int N);
void test();

int main()
{
	int T;
	int N;
	int cse = 1;
	long long int ans;

	cin>>T;
	while(T--)
	{
		cin>>N;
		ans = solve(N);
		cout<<"Case #"<<cse<<": ";
		if(ans == -1)
		{
			cout<<"INSOMNIA";
		}
		else
		{
			cout<<ans;
		}
		cout<<endl;
		cse++;
	}

	return 0;
}

long long int solve(int N)
{
	bool seen[10];
	int unseen = 10;
	long long int number;
	long long int lastnumber;
	long long int i = 1;

	if(N == 0)
	{
		return -1;
	}

	for(int i=0; i<10; i++)
	{
		seen[i] = false;
	}

	do
	{
		lastnumber = number = N*i;

		while(number)
		{
			if(seen[number%10] == false)
			{
				seen[number%10] = true;
				unseen--;
			}
			number = number/10;
		}
		i++;
	}while(unseen);

	return lastnumber;
}

void test()
{
	for(int i=1; i<=1000000; i++)
	{
		cout<<i<<" "<<solve(i)<<endl;
	}
}
