#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <climits>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>

#define PB push_back

#define PP pair<int, int>
#define MP make_pair
#define F first
#define S second

using namespace std;

typedef long long ll;

int main(){
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);	
		
		int r1;
		scanf("%d", &r1);
		vector<int> cards;
		for (int i = 1; i <= 4; i++){
			int a;
			for (int j = 1; j <= 4; j++){
				scanf("%d", &a);
				if (i == r1) cards.PB(a);
			}
		}
		
		int ans = -1, count = 0;
		scanf("%d", &r1);
		for (int i = 1; i <= 4; i++){
			int a;
			for (int j = 1; j <= 4; j++){
				scanf("%d", &a);
				if (i == r1)
					for (int k = 0; k < 4; k++) if (a == cards[k]){
						ans = a; count++; break;
					}
			}
		}
		

		if (count == 0) printf("Volunteer cheated!\n");
		else if (count == 1) printf("%d\n", ans);
		else printf("Bad magician!\n");
	}
	return 0;
}
