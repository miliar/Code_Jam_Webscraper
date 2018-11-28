#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <map>
#include <stack>

#define fi first
#define se second
#define mp make_pair
#define ll long long
#define pii pair <int, int>
#define vi vector <int>
#define REP(a,b) for(int a = 0; a < b; ++a)
#define FORU(a,b,c) for(int a = b; a <= c; ++a)
#define FORD(a,b,c) for(int a = b; a >= c; --a)
#define MOD 1000000000
#define MODLL 1000007LL
#define INF 2123123123
#define pb push_back
using namespace std;

int main() {
	int a, row, T;
	
	scanf("%d", &T);
	
	FORU(tc, 1, T) {
		int temp1, temp2;
		temp1 = temp2 = 0;
		
		scanf("%d", &row);
		
		FORU(i, 1, 4) {
			FORU(j, 1, 4) {
				scanf("%d", &a);
				
				if (i == row)
					temp1 |= (1 << a);
			}
		}
		
		scanf("%d", &row);
		
		FORU(i, 1, 4) {
			FORU(j, 1, 4) {
				scanf("%d", &a);
				
				if (i == row)
					temp2 |= (1 << a);
			}
		}
		
		int temp = temp1 & temp2;
		
		printf("Case #%d: ", tc);
		
		if (temp == 0) {
			puts("Volunteer cheated!");
			continue;
		}
		
		int ans = -1;
		
		FORU(i, 1, 16) {
			if ((temp1 & (1 << i)) && (temp2 & (1 << i))) {
				if (ans == -1)
					ans = i;
				else
					ans = -2;
			}
		}
		
		if (ans == -2)
			puts("Bad magician!");
		else
			printf("%d\n", ans);
	}
}
