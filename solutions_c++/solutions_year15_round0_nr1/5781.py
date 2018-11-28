#include <iostream>
#include <cstdio>
using namespace std;

int n,all;
int s[1005];

int f(int caseID) {
    scanf("%d ", &n); all = 0;
    for (int i = 0; i<=n; i++) {
    	char c; scanf("%c", &c);
    	s[i] = c-48;
    	all+=s[i];
    }
    scanf("\n");
    
    int x = s[0];
    int needed = 0;
    int tart = 1;
    
    while (x < all) {
    	while (tart <= x && tart <= n) { x+=s[tart++]; }
    	//printf("tart %d  x %d\n", tart, x);
    	if (x < all) { x++; needed++; all++; }
    }
    
    printf("Case #%d: %d\n", caseID, needed);
}


int main()
{
    int db; scanf("%d\n", &db); for (int i = 1; i<=db; i++) f(i);
    
    //printf("\n");
    return 0;
}
