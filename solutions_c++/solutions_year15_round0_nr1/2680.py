#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;

int main()
{
	int tests;
	cin >> tests;

	for(int a=0; a<tests; a++)
	{
		int maxShy;
		cin >> maxShy;

		vector<int> levels(maxShy+1, 0);
		string shyLevels;
		cin >> shyLevels;
		for(size_t i=0; i<shyLevels.size(); i++)
		{
			levels[i] = shyLevels[i] - '0';
		}

//		cerr << "Case " << a << " got: " << shyLevels << endl;

		int retval = 0;

		int standing = 0;
		for(size_t i=0; i<levels.size(); i++)
		{
//			cerr << "Testing shyness: " << i << " with " << standing << " standing and invited: " << retval << endl;
			if(standing >= i)
			{
				standing += levels[i];
			}
			else if(levels[i])
			{
				retval += (i - standing);
				standing = i + levels[i];
			}
		}
		cout << "Case #" << (a+1) << ": " << retval << endl;
	}

	return 0;
}