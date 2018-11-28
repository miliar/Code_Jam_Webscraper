#include <iostream>
#include <iomanip>
using namespace std;
int y[10];

bool check()
{
	int i, p;
	for(i = 0; i < 10; i++)
		p *= y[i];
	return p == 0;
}

void count(int n)
{
	while(n > 0)
	{
		y[n % 10]++;
		n /= 10;
	}
}

int sheep(int n)
{
	if(n == 0) return -1;
	int x = 0, m, i, j = 1;
	for(i = 0; i < 10; i++)
		y[i] = 0;
	count(n);
	while(check() || j > 100)
	{
		m = n * ++j;
		count(m);
	}
	return m;
}

int main( )
{
	int t, i;
  cin >> t;
  for(i = 1; i <= t; i++)
  {
  	int n, s;
  	cin >> n;
  	s = sheep(n);
  	cout << "Case #" << i << ": ";
  	if(s < 0) cout << "INSOMNIA";
  	else cout << s;
  	cout << endl;
  }
}

