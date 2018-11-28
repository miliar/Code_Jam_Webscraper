#include <iostream>
using namespace std;

int main ()
{
	int n,m;
	cin >> n >> m;
	int r = 0;
	for (int i = 1; i < n-m+1; i++)
	{
		r += n-i;
	}
	cout << r << endl;
}
