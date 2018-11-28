#include <iostream> 
using namespace std;

int f(string x)
{
	int result = 1;
	for (int i = 1; i < x.size(); i++)
		if (x[i] != x[i - 1])
			result++; 
			
	if (x[x.size() - 1] == '+')
		result--;
	return result;
}

int main()
{	
	int tests;
	cin >> tests;
	for (int i = 1; i <= tests; i++)
	{
		string x;
		cin >> x;
		cout << "Case #" << i << ": " << f(x) << "\n";
	}

	return 0;
}
