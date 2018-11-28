#include <iostream>
#include <vector>
using namespace std;

void test(int i)
{
	int smax;
	cin >> smax;
	vector<int> people(smax + 1);
	for (int i = 0; i <= smax; i++)
	{
		char c;
		cin >> c;
		people[i] = c - '0';
	}
	
	int standingpeople = 0, friends = 0;
	for (int i = 0; i <= smax; i++)
	{
		if (standingpeople < i)
		{
			friends += i - standingpeople;
			standingpeople = i;
		}
		standingpeople += people[i];
	}
		
	
	cout << "Case #" << i << ": " << friends << endl;
}

int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		test(i);
}