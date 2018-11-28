#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int t;
ll a, x, y, b, one = 1LL;

int main(){
	scanf("%d", &t);
	for (int jj=1; jj<=t; jj++){
		scanf("%lld", &x);
		a = 0;
		printf("Case #%d: ", jj);
		if (x == 0){
			printf("INSOMNIA\n");
		} else {
			b = 0;
			do {
				a += x;
				y = a;
				while (y > 0){
					b |= (one << (y % 10));
					y /= 10;
				}
			} while (b != ((one << 10)-1));
			printf("%lld\n", a);
		}
	}
	return 0;
}
