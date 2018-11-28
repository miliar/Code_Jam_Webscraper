#include <iostream>
#include <string>
#include <vector>
//#include <boost/multiprecision/cpp_int.hpp>
#include <math.h>
using namespace std;
typedef vector<int> vint;

vint readrow() 
{
	vint result;
	for(int i = 0;i<4;i++)
	{
		int n;
		cin >> n;
		result.push_back(n);
	}
	return result;
}
vint readmap() 
{
		int R1;
		cin >> R1;
		vint row1;
		for(int r = 1; r<= 4; r++)
		{
			vint row = readrow();
			if (r == R1)
				row1 = row;
		}

		return row1;
}
int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) 
	{
		vector<int> row;

		vint R1 = readmap();
		vint R2 = readmap();

		vint match;

		for(int i = 0; i< R1.size(); i++)
		for(int j = 0; j< R2.size(); j++)
			if (R1[i] == R2[j])
				match.push_back( R1[i] );
		// cout << match.size() << endl;

		cout << "Case #" << (t+1) << ": " ;
		switch(match.size())
		{
			case 1:
				cout << match[0];
				break;
			case 0:
				cout << "Volunteer cheated!";
				break;
			default:
				cout << "Bad magician!";
				break;
		}
		cout << endl;
	}
	return 0;
}


