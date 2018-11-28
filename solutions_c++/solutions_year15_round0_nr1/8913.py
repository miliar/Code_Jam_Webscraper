#include <iostream>
#include <fstream>
#include <assert.h>

using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin >> t;
	for (int l = 1; l <= t; ++l)
	{
		int smax;
		cin >> smax;

		char temp;
		int tempInt;

		int standing = 0;
		int friends = 0;
		cin.get(temp); // get space
		for (int i = 0; i <= smax; ++i)
		{
			cin.get(temp);
			tempInt = temp - 48;

			if (tempInt != 0 && standing < i)
			{
				friends += i - standing;
				standing += i - standing;
			}
			standing += tempInt;
		}
		assert(friends <= 1001 && friends >= 0);
		cout << "Case #" << l << ": " << friends << endl;
	}
}