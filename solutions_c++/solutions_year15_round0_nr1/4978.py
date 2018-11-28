#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
	int N;
	cin >> N;

	for (int n = 0; n < N; n++)
	{
		int max;
		cin >> max;
		int* guests = (int*)malloc(sizeof(int) * (max + 1));
		cin.ignore();
		for (int i = 0; i <= max; i++) {
			char c;
			cin >> c;
			guests[i] = c - '0';
		}

		int clapping = 0;
		int needed = 0;
		for (int i = 0; i <= max; i++)
		{
			if (guests[i] == 0) continue;
			if (clapping >= i) {
				clapping += guests[i];
			}
			else {
				int extra = i - clapping;
				needed += extra;
				clapping += extra + guests[i];
			}
		}
		cout << "Case #" << n + 1 << ": " << needed << endl;
	}

	return 0;
}