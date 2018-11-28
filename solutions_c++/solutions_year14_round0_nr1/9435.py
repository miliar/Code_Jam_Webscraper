
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <queue>
#include <climits>
#include <cstdlib>
#include <sstream>
#include <stack>

using namespace std;

int main()
{
		int test;
		int cout[17];
		int ans, val; 
		int arr[4][4];

		scanf("%d", &test);

		for (int tst = 1; tst <= test; tst++) {
			scanf("%d", &ans);
			ans--;
			memset(cout, 0, sizeof(cout));
			for (int i = 0; i < 4; i++) {
					for (int j = 0; j < 4; j++) {
						scanf("%d", &arr[i][j]);
					}
			}
			for (int i = 0; i < 4; i++) {
				val = arr[ans][i];
				cout[val]++;
			}

			scanf("%d", &ans);
			ans--;
			for (int i = 0; i < 4; i++) {
					for (int j = 0; j < 4; j++) {
						scanf("%d", &arr[i][j]);
					}
			}
			for (int i = 0; i < 4; i++) {
				val = arr[ans][i];
				cout[val]++;
			}
			int cou = 0;
			for (int i = 1; i <= 16; i++) {
				if (cout[i] == 2) {
						cou++;
						val = i;
				}
			}
			if (cou == 0)
					printf("Case #%d: Volunteer cheated!\n", tst);
			else if (cou == 1) {
					printf("Case #%d: %d\n", tst, val);
			}else
				printf("Case #%d: Bad magician!\n", tst);
					
		}

		return 0;
}

