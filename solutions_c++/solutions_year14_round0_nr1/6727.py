#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

#define sf(a) scanf("%d", &a)
#define sfl(a) scanf("%lld", &a)
#define pf(a) printf("%d", a)
#define pfl(a) printf("%lld", a)
#define pln() printf("\n")
#define FOR(i,a,b) for(i=a; i<b; i++)
#define pb push_back

typedef long long int LL;

int main(void){
	int t;
	sf(t);
	int i;
	FOR(i,1,t+1){
		int a1;
		sf(a1);
		int arr1[4][4];
		int j, k;
		FOR(j,0,4){
			FOR(k,0,4){
				sf(arr1[j][k]);
			}
		}
		int a2;
		sf(a2);
		int arr2[4][4];
		FOR(j,0,4){
			FOR(k,0,4){
				sf(arr2[j][k]);
			}
		}
		a1--; a2--;
		int x = 0;
		int c = 0;
		FOR(j,0,4){
			FOR(k,0,4){
				if(arr1[a1][j] == arr2[a2][k]){
					c++;
					x = arr1[a1][j];
					break;
				}
			}
		}
		printf("Case #%d: ", i);
		if(c == 0) printf("Volunteer cheated!\n");
		else if(c == 1) printf("%d\n", x);
		else printf("Bad magician!\n");
	}

	//system("pause");
	return 0;
}
