#include <iostream>

using namespace std;

int main()
{
	int T;
	int K, C, S;

	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cin >> K >> C >> S;
		cout << "Case #" << t << ":";
		for(int i = 1; i <= S; i++)
			cout << " " << i;
		cout << endl;
	}

	return 0;
}