#include <iostream>
#include <stdio.h>
using namespace std;;
int main()
{
	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; c++)
	{
		int N;
		cin >> N;
		if (N == 0) printf("Case #%d: INSOMNIA\n", c);
		else {
			int i = 1;
			bool alldigits[10] = { false };
			while (true) {
				int v = i * N;
				while (v) {
					alldigits[v % 10] = true;
					v /= 10;
				}
				bool allseen = true;
				for (int p = 0; p < 10; p++)
					if (alldigits[p] == false) allseen = false;
				if (allseen) {
					printf("Case #%d: %d\n", c, i * N);
					break;
				}
				i++;
			}
		}
	}
	return 0;
}