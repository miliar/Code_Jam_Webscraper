#include<iostream>
#include<fstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool markCovered(long long int number, vector<bool> &isCovered, int &toCover)
{
	while (number)
	{
		int digit = number % 10;
		number /= 10;

		if (!isCovered[digit])
		{
			isCovered[digit] = true;
			toCover--;
		}
	}

	return toCover == 0;
}

int main() {
	/*ifstream cin;
	ofstream cout;
	cin.open("countingSheep.in");
	cout.open("countingSheep.out");*/

    long long int testCases;
	cin >> testCases;

	long long int tc = 0;
    while (++tc <= testCases)
    {
		cout << "Case #" << tc << ": ";

        long long int n;
		cin >> n;

		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}

		vector<bool> isCovered(10, false);
		int toCover = 10;
		long long int i = n;

		while (!markCovered(i, isCovered, toCover))
		{
			i += n;
		}

		cout << i << endl;
    }

	/*cin.close();
	cout.close();*/
    
    return 0;
}
