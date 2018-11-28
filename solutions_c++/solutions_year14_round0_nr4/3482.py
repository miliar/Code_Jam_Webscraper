#include <bits/stdc++.h>
using namespace std;

#define fileName "D-large"
int caseNum = 0;

double naomi[1005];
double ken[1005];

void readBlocks(int n) {
	for(int i = 0; i < n; i++) {
		scanf("%lf", &naomi[i]);
	}
	for(int i = 0; i < n; i++) {
		scanf("%lf", &ken[i]);
	}
}

int nWins(int nn) {
	int offset = 0, res = 0;
	nn--;
	for(int i = nn; i >= 0 && i - offset >= 0; i--) {
		if(naomi[i] > ken[i - offset])
			res++;
		else {
			offset++; i++;
		}
	}
	return res;
}

int kWins(int nn) {
	int offset = 0, res = 0;
	nn--;
	for(int i = nn; i >= 0 && i - offset >= 0; i--) {
		if(ken[i] > naomi[i - offset])
			res++;
		else {
			offset++; i++;
		}
	}
	return res;
}

void solve() {
    printf("Case #%d: ", ++caseNum);
	int n;
	
	scanf(" %d", &n);
	readBlocks(n);
	
	sort(naomi, naomi + n);
	sort(ken, ken + n);
	
    printf("%d %d\n", nWins(n), n - kWins(n));
}

int main() {
    freopen(fileName ".in", "r", stdin);
    freopen(fileName ".txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
	while(T--) {
        solve();
    }
    return 0;
}