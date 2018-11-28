#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

int main()
{
	int casses;
	cin >> casses;
	for(int caseNum = 1; caseNum <= casses; caseNum++)
	{
		int x, y, z;
		cin >> x >> y >> z;
		cout << "Case #" << caseNum << ":";
		for(int i = 1; i <= x; i++)
		{
			cout << " " << i;
		}
		cout << endl;
	}
	return 0;
}
