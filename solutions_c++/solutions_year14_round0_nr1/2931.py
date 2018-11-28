#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string s; 
const int MAXN = 4; 
char ch; 
int tests, test, n, m, x, y; 
int a[MAXN][MAXN], b[MAXN][MAXN]; 


int main(){
    freopen("1.in","r",stdin); 
    freopen("1.out","w",stdout);

    scanf("%d",&tests);
    n = 4; 
    m = 4; 

    for (test = 1; test <= tests; ++test){
        scanf("%d", &x); 

        for (int i = 0; i < n; ++i) {
        	for (int j = 0; j < m; ++j) {
        		scanf("%d", &a[i][j]); 
        	}
        }

		scanf("%d", &y);  

        for (int i = 0; i < n; ++i) {
        	for (int j = 0; j < m; ++j) {
        		scanf("%d", &b[i][j]); 
        	}
        }

        int count = 0; 
        int ans = 0; 
        --x; 
        --y; 

		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[x][i] == b[y][j]) {
					++count;
                    ans = a[x][i]; 
				}
			}
		}

		if (count == 0) {
	        printf("Case #%d: Volunteer cheated!\n", test); 
		} else
		if (count > 1) {
			printf("Case #%d: Bad magician!\n", test); 
		} else {
			printf("Case #%d: %d\n", test, ans);
		}
           
    }   
     
    return 0;  
}
