#include <iostream>
#include <algorithm>
#include <math.h>
#include <stdlib.h>

using namespace std;

long long int T,N,J,coin[1000],binary,no_of_output;

void add_coin(long long int no_of_digit);
void find_jam_coin(long long int no_of_digit);
long long int find_no_of_digit(long long int number);
int is_coin_jam(long long int no_of_digit);
int is_not_prime(long long int number);
void print_coin(long long int N);	
long long int to_base(long long int *number,long long int base_no,long long int no_of_digit);

long long int find_no_of_digit(long long int number)
{
	long long int no_of_digit;

	if (number > 0)
	{
		no_of_digit = (long long int )log10((double) number) + 1;
	}
	else
	{
		no_of_digit = 1;
	}
	return no_of_digit;
}

long long int to_base(long long int *number,long long int base_no,long long int no_of_digit)
{
	long long int in_base = 0,i;

	// no_of_digit = find_no_of_digit(number[]);

	// cout<<"no_of_digit = "<<no_of_digit<<endl;
	for (i = 0; i < no_of_digit; ++i)
	{
		in_base = in_base + number[no_of_digit - 1 - i]*pow(base_no,i);
	}

	return in_base;
}
int is_not_prime(long long int number)
{
	long long int sqrt_number,i,random;
	sqrt_number = sqrt(number);

	// cout<<"number = "<<number<<endl;
	for (i = 2; i <= sqrt_number; i++)
	{
		random = (long long int)(rand() % sqrt_number) + 2;
		// cout<<"random = "<<random<<endl;
		if (number % (i)== 0)
		{
			// cout<<"i = "<<random<<endl;
			return i;
		}
	}
	return 0;
}

int is_coin_jam(long long int no_of_digit)
{
	long long int j;

	for (j = 2; j <= 10; j++)
	{
		if (!is_not_prime(to_base(coin,j,no_of_digit)))
		{
			return 0;
		}
	}
	return 1;
}
void add_coin(long long int no_of_digit)
{
	long long int i,j;
	j = binary;
	for ( i = no_of_digit - 2; i >= 0; i--)
	{
		coin[i] = j%2;
		// cout<<"i = "<<i<<endl;
		j = j/2;		
		if(j == 0)
		{
			break;
		}	
	}
	// cout<<"binary = "<<binary<<endl;
	binary++;
	//print_coin(no_of_digit);
	//cout<<endl;

}

void find_jam_coin(long long int no_of_digit)
{
	long long int i,j;
	// to_base(coin,j,no_of_digit)

	for ( i = 0; i < (no_of_digit - 2)*(no_of_digit -2); i++)
	{
			// cout<<"base = "<<i<<" "<<to_base(coin,i,no_of_digit)<<endl;
		if (is_coin_jam(no_of_digit) && no_of_output != J)
		{
			print_coin(N);
			//cout<<endl;
			for (j = 2; j <= 10; j++)
			{
			
				cout<<is_not_prime(to_base(coin,j,no_of_digit))<<" ";
			}
			cout<<endl;
			no_of_output++;
		}
		add_coin(no_of_digit);
	}

}
void initialize_coin(long long int N)
{
	long long int i;

	coin[0] = 1;
	coin[N-1] = 1;
}
void print_coin(long long int N)
{
	long long int i;

	for (i = 0; i < N; i++)
	{
		cout<<coin[i];
	}
	cout<<" ";
}
int main()
{
	long long int i,j,k;

	cin>>T;

	for (i = 1 ; i <= T; i++)
	{
		memset(coin,0,1000*sizeof(long long int));
		binary = 1;
		no_of_output = 0;
		cin>>N>>J;

		cout<<"Case #"<<i<<":"<<endl;
		initialize_coin(N);		
		find_jam_coin(N);
		// for (int j = 0; j < (N - 2)*(N -2); j++)
		// {
		// 	add_coin(N);
		// }
		// coin[0] = 1;
		// coin[1] = 1;
		// coin[2] = 0;
		// coin[3] = 1;
		// coin[4] = 1;
		// coin[5] = 1;
		// }
		// coin[0] = 1;
		// coin[1] = 0;
		// coin[2] = 0;
		// coin[3] = 1;
	
		// cout<<"prime = "<<is_not_prime(to_base(coin,2,4))<<endl;
		// for ( j = 2; j <= 10; j++)
		// {
		// 	cout<<is_not_prime(to_base(coin,j,4))<<" ";
		// }
		// cout<<endl;
	}
	return 0;
}