#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";

		int n;
		cin >> n;

		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}

		bool digitsSeen[10] = { false, false, false, false, false, false, false, false, false, false };
		int index = 1;
		unsigned long long call;
		while (true)
		{
			call = n * index;
			index++;
			unsigned long long temp = call;

			do {
				int digit = temp % 10;
				digitsSeen[digit] = true;
				temp /= 10;
			} while (temp > 0);

			bool done = true;
			for (int i = 0; i < 10; i++)
			{
				if (!digitsSeen[i])
				{
					done = false;
					break;
				}
			}

			if (done)
			{
				break;
			}
		}	

		cout << call << endl;
	}
	
	return 0;
}