#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int m;

int f(int a[], int N)
{
	m = 0;
	int s = 0;
	for(int i = 1; i < N; ++i)
	{
		int tmp = a[i - 1] - a[i];
		if(tmp > 0)
		{
			s += tmp;
			if(tmp > m) m = tmp;
		}
	}
	return s;
}

int g(int a[], int N)
{
	int s = 0;
	for(int i = 0; i < N - 1; ++i)
	{
		s += fmin(m, a[i]);
	}
	return s;
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for(int u = 1; u <= T; ++u)
	{
		int N;
		cin >> N;

		int a[1000] = {};
		for(int i = 0; i < N; ++i)
			cin >> a[i];

		int y = f(a, N), z = g(a, N);
		
		cout << "Case #" << u << ": " << y << ' ' << z << endl;
	}
	return 0;
}