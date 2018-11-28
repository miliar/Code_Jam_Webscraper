#include <iostream>
#include <cmath>

using namespace std;

bool isPalindrome(int nombre)
{
	int nb, nbInverse;

	nb = nombre;
	nbInverse = 0;
	while(nb > 0)
	{
		nbInverse = nbInverse * 10 + (nb % 10);
		nb /= 10;
	}
	return nombre == nbInverse;
}

int main()
{
	int n, start, end, total, test;

	cin >> n;

	for(int i = 0; i < n; i++)
	{
		total = 0;
		cin >> start >> end;
		test = ceil(sqrt(start));

		while(pow(test, 2) <= end)
		{
			if(isPalindrome(test) && isPalindrome (pow(test, 2)))
			{
				total++;
			}
			test++;
		}

		cout << "Case #" << i+1 << ": " << total << "\n";
	}
	return 0;
}
