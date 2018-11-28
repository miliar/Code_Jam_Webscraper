#include <iostream>

using namespace std;

long long int numbers[20];

int is_seen_all_numbers()
{
	for (int i = 0 ; i < 10; i++)
	{
		if (numbers[i] == 0)
		{
			return 0;
		}
	}	
	return 1;
}

void seen_numbers(long long int N)
{
	// cout<<"N = "<<N<<endl;
	while (N > 0)
	{
		// cout<<"			"<<N%10<<endl;
		numbers[N%10] = 1;
		N = N /10;
	}
}

int main()
{
	long long int T,N,i,j,k,start,Case=1;;

	cin>>T;

	for (i = 0; i < T; i++)
	{	
		cin>>N;
		// numbers[20] = {0};
		// fill(numbers,numbers+20,0);
		// k = N;
		// seen_numbers(N);
		k = 0;
		start = N;
		memset(numbers,0,20*sizeof(long long int));
		if (N == 0)
		{
			cout<<"Case #"<<Case++<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			while (!is_seen_all_numbers())
			{
				N = start + k*start;
				seen_numbers(N);
				k++;
			}
			cout<<"Case #"<< Case++<<": "<<N<<endl;
		}
	}
	return 0;
}
