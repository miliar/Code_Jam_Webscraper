// Qualification Round 2013
// Problem A. Tic-Tac-Toe-Tomek
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

int main()
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);
	map<int, int> mas;
	mas[1] = 1;
	mas[4] = 2;
	mas[9] = 3;
	mas[121] = 4;
	mas[484] = 5;
    int T;
    cin >> T;
    for (int k = 0; k < T; k++)
    {
		int a, b;
		cin >> a >> b;
        int res = 0;
		for (int i = b; i >= a; i--)
			if (mas[i] != 0)
			{
				res = mas[i];
				break;
			}
		for (int i = a-1; i > 0; i--)
			if (mas[i] != 0)
			{
				res -= mas[i];
				break;
			}
        cout << "Case #" << k+1 << ": " << max(res, 0) << endl;
    }
    return 0;
}