#include <iostream>
#include <cmath>
using namespace std;

char aux[4];

int num_digits(int n)
{
	int cont = 0;
	while(n != 0)
	{
		n /= 10;
		cont++;
	}
	return cont;
}

void num_to_string(int n)
{
	int i, limit;
	limit = num_digits(n);
	for(i = 1; i <= limit; i++)
	{
		aux[limit-i] = (n%10)+'0';
		n /= 10;
	}
}

bool check_pal(int n)
{
	int i, limit, j;
	limit = num_digits(n);
	for(i = 0; i < (limit/2)+1; i++)
	{
		if(aux[i] != aux[limit-i-1])
			return false;
	}
	return true;
}

int main()
{
	int T, A, B, i, j, k, m, total;
	cin >> T;
	for(i = 1; i <= T; i++)
	{
		cin >> A >> B;
		total = 0;
		for(j = A; j <= B; j++)
		{
			num_to_string(j);
			if(check_pal(j))
			{
				k = sqrt(j);
				if((k*k) == j)
				{
					num_to_string(k);
					if(check_pal(k))
						total += 1;
				}
			}
		}
		cout << "Case #" << i << ": " << total << endl;
	}
	return 0;
}
