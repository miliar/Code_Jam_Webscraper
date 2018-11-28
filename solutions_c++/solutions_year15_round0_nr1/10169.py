#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int j=0; j<t; j++)
	{
		int smax;
		cin >> smax;
		getchar();
		int shy[smax+1];
		for (int i=0; i<=smax; i++)
		{
			shy[i] = getchar() - '0';
		}
		int count = shy[0], friends = 0;
		for (int i=1; i<=smax; i++)
		{
			if (i > count && shy[i] > 0)
			{
				friends = friends + i - count;
				count = count + shy[i] + friends;
			}
			else
				count = count + shy[i];
		}
		cout << "Case #" << j+1 << ": " << friends << endl;
	}
	return 0;
}