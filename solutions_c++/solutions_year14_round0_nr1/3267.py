// Omair Ali
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

#define SCS(s) assert(scanf("%s", s));
#define SCI(i) assert(scanf("%d", &i));
#define PRI(i) printf("%d\n", i);
#define PRM(s) printf("%s\n", s);
#define PRN printf("\n");
#define PRIM(s,i) printf("%s%d\n", s, i);
#define FOR(a,b) for(int a = 0; a < b; a++)
#define FORC(a,b,c) for(int a = b; a < c; a++)
#define OOB(a,b) (a < 0 || a > b)

int cards[4][4];

int main() {
	int scenarios = 0;
	SCI(scenarios);
	for(int s = 1; s <= scenarios; s++){
		int first,second,count,card;
		count = 0;
		SCI(first);
		first--;
		FOR(i,4){
			FOR(j,4){
				SCI(cards[i][j]);
			}
		}
		SCI(second);
		second--;
		FOR(i,4){
			FOR(j,4){
				int num;
				SCI(num);
				if (i == second){
					FOR(k,4){
						if (num == cards[first][k]){
							card = num;
							count++;
						}
					}
				}
			}
		}

		printf("Case #%d: ", s);
		if (count == 0){
			printf("Volunteer cheated!\n");
		} else if (count == 1){
			printf("%d\n", card);
		} else {
			printf("Bad magician!\n");
		}
	}	
	return 0;
}