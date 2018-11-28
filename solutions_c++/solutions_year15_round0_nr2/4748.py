#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
using namespace std;

const int MAXN = 1000 + 10;
const int MAXM = 1000;  
int r, v, ar, br, av, top, ans, tests, test, Time, n, data; 
 
int a[MAXN]; 

bool desc(int i, int j) { return i > j; }

int main(){
    freopen("1.in","r",stdin); 
    freopen("1.out","w",stdout);

    scanf("%d\n",&tests);
    
    for (test = 1; test <= tests; ++test){
    	scanf("%d\n", &n); 
    	for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
    	}
    	sort(a, a+n, desc);
    	
		top = a[0];
		ans = top; 
		
		for (int i = 1; i <= top; ++i) {
			int minutes = i; 	// eat minutes
			for (int j = 0; j < n; ++j) if (a[j] > i) {
				minutes += a[j] / i - (int)(a[j] % i == 0); // special minutes
			}
            //printf("(%d)\t", minutes);
			ans = min(ans, minutes);
		}
    	printf("Case #%d: %d\n", test, ans);           
    }   
     
    return 0;  
}
