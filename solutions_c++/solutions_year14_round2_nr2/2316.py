#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%i", &t);
	for (int l = 0; l < t; l++) {
		int a, b, k;
		scanf("%i%i%i", &a, &b, &k);
		int c = 0;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i & j) < k) c++;
			}
		}
		printf("Case #%i: %i\n", l +1, c);
	}
	return 0;
}

