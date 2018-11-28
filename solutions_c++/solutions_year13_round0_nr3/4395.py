#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

bool palindrome(unsigned long long int n)
{
	char a[20], b[20];
	unsigned long long int temp = n, m = 0;
	while (temp / 10 != 0)
	{
		m = m * 10 + temp % 10;
		temp /= 10;
	}
	m = m * 10 + temp;
	sprintf(a, "%d", n);
	sprintf(b, "%d", m);
	string as = a, bs = b;
	return as.compare(bs) == 0;
}

bool square(unsigned long long int n)
{
	unsigned long long int root = sqrt(n);
	return root * root == n;
}

unsigned long long int squareVal(unsigned long long int n)
{
	return sqrt(n);
}

int main()
{
	//freopen("C:\\Users\\wayne\\Downloads\\input.txt", "r", stdin);
	//freopen("C:\\Users\\wayne\\Downloads\\output.txt", "w", stdout);
	freopen("C:\\Users\\wayne\\Downloads\\C-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\wayne\\Downloads\\Small-output.out", "w", stdout);
	//freopen("C:\\Users\\wayne\\Downloads\\C-large.in", "r", stdin);
	//freopen("C:\\Users\\wayne\\Downloads\\Large-output.out", "w", stdout);
	int t;
	unsigned long long int a, b, count;

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		count = 0;
		cin >> a >> b;
		for (unsigned long long int j = a; j <= b; j++)
			if (square(j) && palindrome(j) && palindrome(squareVal(j)))
				count++;
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}