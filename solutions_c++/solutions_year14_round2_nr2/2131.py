#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>
#include <iostream>
#define mp make_pair
#define pb push_back

#define s second
#define f first

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int test;
	scanf("%d", &test);

	for ( int ii = 0; ii < test; ii++)
	{
		int a, b, k, res = 0;
		scanf("%d%d%d", &a, &b, &k);
		for ( int i = 0; i < a; i++)
			for ( int j = 0; j < b; j++)
			{
				if ( (i & j) < k)
					res++;
				//cout << "____________________" << i << " " << j << "  " << (i & j) << " < " <<  k << endl;
			}
		printf("Case #%d: %d\n", ii + 1, res);
	}

	return 0;
}
