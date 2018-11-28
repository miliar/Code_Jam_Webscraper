#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
	int cases, c;
	cin >> cases;

	for(int c=1; c <= cases; c++) {
		int max, total, added, qnt;
		cin >> max;
		total = 0;
		added = 0;

		for(int shin = 0; shin <= max; shin++) {
			scanf("%1d", &qnt);

			if (total < shin && qnt) {
				added += shin - total;
				total += added;
			}
			total += qnt;
			if (total >= max && shin != max) {
				cin.ignore(6, '\n');
				break;
			}
		}

		printf("Case #%d: %d\n", c, added);

	}
  return 0;
}

