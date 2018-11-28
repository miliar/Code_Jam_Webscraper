#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <map>

using namespace std;

const int MAX = 1001;
int ate = sqrt(MAX) + 1;

int grid[200][220];
int n, m;

int acu[MAX];
bool fairsquare[MAX];

bool isPalin( int pal ) {
	char aux[30];
	sprintf(aux, "%d", pal);
	for (int i = 0, j = strlen(aux)-1; i < j; ++i, --j) {
		if (aux[i] != aux[j]) return false;
	}
	return true;
}

int main() {
	
	int casos, caso = 0;
	scanf("%d", &casos);
	for (int i = 1; i < ate; ++i) {
		if (isPalin(i)) {
			int ii = i * i;
			if (isPalin(ii)) {
				fairsquare[ii] = true;
			}
		}
	}
	for(int i = 1; i < MAX; ++i) {
		acu[i] = acu[i-1];
		if(fairsquare[i]) ++acu[i];
	}
	int a, b;
	while(casos--){ 
		caso++;
		scanf("%d%d", &a, &b);
		
		printf("Case #%d: %d\n", caso, acu[b] - acu[a-1]);
		
		
	}
	
	return 0;
}