#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define N 1003

int v[N];
char sir[N];

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t, tst, n, i, j, x, d;
    int sum, s, mx, sm;
    
    scanf("%i", &tst);
    for (t = 0; t < tst; t++) {
        scanf("%i", &n);
        
        scanf("%s", sir);
        x = sir[0] - '0';
       	sum = x;
       	d = 0;
       
        for (i = 1; i < n+1; i++) {
        	x = sir[i] - '0';
        	//printf("%d %d\n", x, sum);
       		if (x && i > sum){
       			d += i - sum;
       			sum += i - sum;
       		}
       		//printf("%d %d %d\n", x, sum, d);	
       		sum += x;
        }
        
        printf("Case #%d: %d\n", t+1, d);
             
    }
    
    
    
    return 0;
}

