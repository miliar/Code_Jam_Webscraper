#include <iostream> 
using namespace std;

typedef unsigned long long ull;

bool arr[10];

void clear_tab()
{
	for (int i = 0; i < 10; i++)
		arr[i] = 0;
}

void update_digits(ull x)
{
	while (x > 0)
	{
		arr[x % 10] = 1;
		x /= 10;
	}
}

bool check()
{
	for (int i = 0; i < 10; i++)
		if (arr[i] == 0)
			return false;
	return true;
}

ull f(ull x)
{
	clear_tab();
	for (ull i = 1; true; i++)
	{
		update_digits(i * x);
		if (check())
			return i * x;
	}
}

int main()
{
//	ios_base::sync_with_stdio(0);

	int tests;
	cin >> tests;
	for (int i = 1; i <= tests; i++)
	{
		int n;
		cin >> n;
		cout << "Case #" << i << ": ";
		if (n == 0)
			cout << "INSOMNIA";
		else
			cout << f(n);
		cout << "\n";
	}

//	int a, b;
//	cin >> a >> b;

//	for (int i = a; i <= b; i++)
//		cout << i << ": " << f(i) << "\n";

	return 0;
}
