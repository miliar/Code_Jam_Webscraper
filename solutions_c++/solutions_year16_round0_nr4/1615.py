#include <iostream>
using namespace std;

int main()
{
	// Solution for Fractiles (small)
	// When an artwork begins with a lead tile, the next iteration of it
	// will begin with the original artwork. When an artwork begins with
	// a gold tile, the next iteration of it will begin with K gold tiles.
	// So either way, if an artwork contains any gold tiles, any of its
	// iterations will contain a gold tile among the first K tiles.
	// Thus, the trivial solution when S = K is to examine the first K tiles.
	
	int cases;
	int k;
	int c;
	int s;
	
	cin >> cases;
	for (int t = 1; t <= cases; t++)
	{
		cin >> k >> c >> s;
		printf("Case #%d:", t);
		for (int h = 1; h <= k; h++)
			printf(" %d", h);
		printf("\n");
	}
	return 0;
}