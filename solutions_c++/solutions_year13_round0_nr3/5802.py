#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long int64; 

const int MAXN = 100000 + 10;  
int tests, test, total, n, sum, ans1, ans2; 
int a[14], al, ji; 
int64 c[MAXN] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 
100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111,
2000002, 2001002,
10000001, 10011001, 10100101, 10111101, 11000011, 11011011, 11100111, 11111111, 
20000002, 
100000001};
int64 L, R;
int64 sh[15]; 
int l, r, mid, p, lid; 

int main(){
    freopen("3.in","r",stdin); 
    freopen("3.out","w",stdout);

    n = 49; 
    for (int i = 0; i < n; ++i) c[i] = c[i] * c[i]; 
    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        scanf("%d %d", &L, &R); 
        int64* ans1 = lower_bound(c, c + n, L);
		int64* ans2 = upper_bound(c, c + n, R);
		if (ans2 - ans1 > 0)
			printf("Case #%d: %d\n", test, ans2 - ans1);
		else  
			printf("Case #%d: %d\n", test, 0);
    }   
     
    return 0;  
}
