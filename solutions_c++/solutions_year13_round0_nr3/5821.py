#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

typedef long long ll; 
#define SQR(x) ((x)*(x))
const double EPS = 1e-8;
const double PI  = acos(-1.0);

char b[4][5];

bool isPal(int n) {
	char x[10];
	bool pal = true;
	sprintf(x, "%d", n);
	string s = x;
	for(int j = 0; j <= s.size() / 2; j++) {
		if(s[j] != s[(int)s.size()-1-j]) {
			pal = false;
			break;
		}
	}
	return pal;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		int A, B;
		int c = 0;
		scanf("%d %d", &A, &B);
		for(int x = A; x <= B; x++) {
			bool pal = isPal(x);
			
			bool sq = false;
			int rt = (int)sqrt((long double)x);
			int t = -1;
			if( SQR(rt-1) == x ) {
				t = rt - 1;
			} else if( SQR(rt) == x ) {
				t = rt;
			} else if( SQR(rt+1) == x ) {
				t = rt + 1;
			}
			if( t > 0 && isPal(t) ) {
				sq = true;
			}
			if( sq && pal ) {
				c++;
			}
		}
		printf("Case #%d: %d\n", i + 1, c);
	}
	return 0;
}