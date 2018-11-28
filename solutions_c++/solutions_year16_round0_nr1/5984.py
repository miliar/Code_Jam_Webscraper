#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

set < int > dig;
void digits(long long int n)
{
	do
	{
		dig.insert(n%10);
		n/=10;
	} while (n!=0);
}
void countingsheep(long long int n)
{
	dig.clear();
	long long int i, cur;
	for (i=1; i<=100; ++i)
	{
		cur = n*i;
		digits(cur);
		if (dig.size() == 10)
		{
			cout << cur << endl;
			return;
		}
	}
	cout << "INSOMNIA" << endl;
}

int main()
{
	int t;
	cin >> t;
	long long int n;
	for (int i=1; i<=t; i++)
	{
		cin >> n;
		cout << "Case #" << i << ": "; 
		countingsheep(n);
	}
	return 0;
}