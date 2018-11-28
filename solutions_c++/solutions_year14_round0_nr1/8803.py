#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string solve()
{
	int num[100] = {};

	int ans, table[4][4] = {};

	for(int t = 0 ; t < 2 ; ++t) {
		cin >> ans;
		for(int i = 0 ; i < 4 ; ++i)
			for(int j = 0 ; j < 4 ; ++j)
				cin >> table[i][j];

		for(int i = 0 ; i < 4 ; ++i)
			++num[table[ans-1][i]];
	}

	if(count(num, num + 100, 2) == 1)
		return to_string(find(num, num + 100, 2) - num);
	if(count(num, num + 100, 2) > 1)
		return "Bad magician!";
	return "Volunteer cheated!";
}

int main()
{
	int		T;

	cin >> T;
	for(int i = 1 ; i <= T ; ++i)
		cout << "Case #" << i << ": " <<  solve() << endl;
}

