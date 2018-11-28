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

#define ULL unsigned long long
#define LL long long

using namespace std;
int main() {
	int T;
	ULL N, a, b,x;
	cin >> T;
	int c = 1;
	while(c <= T){
		cin >> a;
		int ar[10] = {0,0,0,0,0,0,0,0,0,0};
		int count = 0;
		int i = 1;
		if(a == 0) {cout << "Case #"<< c << ": INSOMNIA\n";c++;continue;}
		while(1){
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
		if(a < 0) cout << "Case #" << c << ": INSOMNIA\n";
		else cout << "Case #" << c << ": " << x << "\n";
		c++;
	}
    return 0;
}
