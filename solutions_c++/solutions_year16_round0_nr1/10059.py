/*
 * @author:metastableB
 * counting_sheep.cpp
 * 
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <climits>
#include <ctime>

/* BEGIN Timer */
#define CLOCK clock()
#define BEGIN_CLOCK clock_t _bx_ = clock();
#define END_CLOCK clock_t _ex_ = clock();
#define TOTAL_C (double)(_ex_ - _bx_)
#define TOTAL_T (TOTAL_C/CLOCKS_PER_SEC)
#define PRINT_CLOCK (printf("%2.3f\n",TOTAL_T));
/* END Timer */
#define ULL unsigned long long
#define LL long long

using namespace std;
int main() {
	int T;
	unsigned long long int N, a, b,x;
	cin >> T;
	int c = 1;
	while(c <= T){
		cin >> a;
		int ar[10] = {0,0,0,0,0,0,0,0,0,0};
		int count = 0;
		int div = 10, i = 1;
		if(a == 0) {cout << "Case #"<< c << ": INSOMNIA\n";c++;continue;}

		while(a>0){
			b = a*i;
			x = b;
			while(b > 0){
				if(ar[b%10] == 0){count++; ar[b%10] = 1;}
				if(count == 10) break;
				b = b/10;
			}
			if(count == 10) break;
			i++;
		}
		if(a<0) cout << "Case #" << c << ": INSOMNIA\n";
		else cout << "Case #" << c << ": " << x << "\n";
		c++;
	}
    return 0;
}
