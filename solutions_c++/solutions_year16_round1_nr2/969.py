#include <iostream>
using namespace std;
const int MAX_HEIGHT = 2500;
int used[MAX_HEIGHT + 1];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, n, j, k, temp;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		for(j = 1; j <= MAX_HEIGHT; j++)
			used[j] = 0;
		cin >> n;
		for(j = 1; j < n << 1; j++)
			for(k = 0; k < n; k++)
			{
				cin >> temp;
				used[temp]++;
			}
		cout << "Case #" << i << ": ";
		for(j = 1; j <= MAX_HEIGHT; j++)
			if(used[j] % 2 == 1)
				cout << j << " ";
		cout << endl;
	}
}
