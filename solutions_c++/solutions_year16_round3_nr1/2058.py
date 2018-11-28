#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#define FOR(i,a,b) for (int i = a; i <= b; i++)
#define FORN(i,N) for (int i = 0; i < N; i++)
#define FORD(i,a,b) for (int i = a; i >= b; i--)


using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

int temp[30];

int main() {
	int T;
	scanf("%d",&T);

	FOR(c,1,T) {
		int N;
		scanf("%d",&N);
		int sum = 0;
		FORN(i,N) {
			scanf("%d",&temp[i]);
			sum+= temp[i];
		}
		printf("Case #%d: ",c);
		while (sum > 0) {
			printf(" ");
			int maxValue = -1;
			int indexOne = -1;
			FORN(i,N) {
				if(temp[i] > maxValue) {
					maxValue = temp[i];
					indexOne = i;
				}
			}
			if(indexOne != -1) {
				printf("%c",indexOne+'A');
				sum--;
				temp[indexOne]--;
			}

			maxValue = -1;
			int indexTwo = -1;
			FORN(i,N) {
				if(temp[i] > maxValue) {
					maxValue = temp[i];
					indexTwo = i;
				}
			}

			int countMax = 0;
			FORN(i,N) {
				if(temp[i] == maxValue) countMax++;
			}
			if(countMax != 2) {
				if(indexTwo != -1) {
					printf("%c",indexTwo+'A');
					sum--;
					temp[indexTwo]--;
				}
			}

		}
		printf("\n");
	}

	return 0;
}
