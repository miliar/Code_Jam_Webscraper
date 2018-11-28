#include <iostream>
#include <vector>
#include <math.h>
#define ll long long
using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<ll int> vlli; 
typedef vector<vlli> vvlli; 

// return a^b % c
ll int modpow(ll int a, ll int b, ll int c)
{
	ll int ans = 1;
	while(b>0)
	{
		if(b%2==1)
			ans = (ans*a)%c;
		a = (a*a)%c;
		b /= 2;
	}
	return ans;
}

// return divisors, if prime return 1
ll int divisor_basen(vector<int>& number, int base)
{
	ll int divisor = 1;
	ll int rem, sqrtMax;
	int number_size = number.size();
	int k = 2;
	if (number_size >= 8 && number_size < 16) 
		k = 4;
	else if (number_size >= 16 && number_size < 24) 
		k = 6;
	else if (number_size >= 24) 
		k = 8;
	sqrtMax =(ll int) pow(base, (number_size/k));
	// verify if 2 is a divisor
	ll int i = 2;
	rem = 0;
	for (int j = 0; j < number_size; ++j)
	{
		if (number[j] == 1)
			rem = (rem + modpow(base, j, i)) % i;
	}
	rem = rem % i;

	if (rem == 0) {
		divisor = 2;
	} else  {
		i = 3;
		while(i < sqrtMax)
		{
			rem = 0;
			for (int j = 0; j < number_size; ++j)
			{
				if (number[j] == 1)
					rem = (rem + modpow(base, j, i)) % i;
			}
			rem = rem % i;
			if (rem == 0)
			{
				divisor = i;
				break;
			}
			i+=2;
			while ( (i!=3 && i%3==0) || (i!=5 && i%5==0) || (i!=7 && i%7==0) )
				i+=2;
		}
	}
	return divisor;
}

void print_number(vector<int>& number)
{
	for (int i = 0; i < number.size(); ++i)
	{
		cout << number[i];
	}
	cout << endl;
}

int main()
{
	int T, N, J, nt;
	cin >> T;
	nt = 0;
	while(nt < T)
	{
		cin >> N >> J;
		vi number(N, 0);
		
		number[0] = 1;
		number[N-1] = 1;
		int base, top, index_sum;
		base = 1;
		top = 1;
		int nfound = 0;
		
		vvlli divisors;
		vvi numbers;
		while(nfound < J && top < N-1 )
		{
			// verify number
			bool is_good = true;
			vlli divisors_basen(9);
			for (int i = 2; i <= 10; ++i)
			{
				ll int divisor = divisor_basen(number, i);
				divisors_basen[i-2] = divisor;
				if (divisor == 1)
				{
					is_good = false;
					break;
				}
			}
			if (is_good) {
				divisors.push_back(divisors_basen);
				numbers.push_back(number);
				nfound++;
			}
			
			// get next number
			index_sum = base;
			while (number[index_sum]==1 && index_sum < N-1)
			{
				number[index_sum] = 0;
				index_sum++;
			}
			number[index_sum] = 1;
			if (index_sum > top)
				top = index_sum;
		}

		nt++;
		
		cout << "Case #"<< nt << ":" << endl;
		for (int i = 0; i < nfound; ++i)
		{
			for (int j = 0; j < numbers[i].size(); ++j)
			{
				cout << numbers[i][numbers[i].size()-j-1];
			}
			cout << " ";
			for (int j = 0; j < 9; ++j)
			{
				cout << divisors[i][j] << " ";
			}
			cout << endl;
			
		}

	}
}