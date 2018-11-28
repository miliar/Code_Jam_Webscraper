#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
 
int main()
{
	int t, i, j, k, n, m, cases;
	int answ, ansdw;
	
    double ken[1002], naomi[1002];
	
    scanf("%d", &t);
	
    while (t--) {
        cases++;
        answ = ansdw = 0;
        
        scanf("%d", &n);
        
        for (i = 0; i < n; i++) {
            scanf("%lf", &naomi[i]);
        }
        for (i = 0; i < n; i++) {
            scanf("%lf", &ken[i]);
        }
        
        sort(naomi, naomi+n);
        sort(ken, ken+n);
        
        i = j = 0;
        
        while (i < n && j < n) {
              if (naomi[i] > ken[j]) {
                 ansdw++;
                 i++;
                 j++;
              } else {
                 i++;
              }
        }
        
        i = j = 0;
        answ = n;
        
        while (i < n && j < n) {
              if (naomi[i] < ken[j]) {
                 answ--;
                 i++;
                 j++;
              } else {
                 j++;
              }
        }
        printf("Case #%d: %d %d\n", cases, ansdw, answ);
    }
	return 0;
}
