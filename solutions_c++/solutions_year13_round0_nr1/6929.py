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

int main() {
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		bool won[2];
		memset(won, 0, sizeof(won));
		for(int j = 0; j < 4; j++) {
			scanf("%s", b[j]);
		}
		printf("Case #%d: ", i+1);
		char d[2];
		memset(d, -1, sizeof(d));
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 2; j++) {
				int r = i;
				int c = j == 0 ? i : 3 - i;
				if( b[r][c] == 'T' )
					continue;
				if( b[r][c] == '.' )
					d[j] = -2;
				if(d[j] == -1) {
					d[j] = b[r][c];
				} else if(d[j] == -2) {

				} else {
					if( d[j] != b[r][c] ) {
						d[j] = -2;
					}
				}
			}
		}
		if( d[0] > 0 ) {
			printf("%c won\n", d[0]);
			continue;
		}
		if( d[1] > 0 ) {
			printf("%c won\n", d[1]);
			continue;
		}
		char x;
		for(int i = 0; i < 4; i++) {
			x = -1;
			for(int j = 0; j < 4; j++) {
				if( b[j][i] == 'T' )
					continue;
				if( b[j][i] == '.' )
					x = -2;
				if( x == -1 ) {
					x = b[j][i];
				}
				else if( x == -2 ) {

				}
				else {
					if( x != b[j][i] )
						x = -2;
				}
			}
			if( x > 0 ) {
				break;
			}
		}
		if( x > 0 ) {
			printf("%c won\n", x);
			continue;
		}
		for(int i = 0; i < 4; i++) {
			x = -1;
			for(int j = 0; j < 4; j++) {
				if( b[i][j] == 'T' )
					continue;
				if( b[i][j] == '.' )
					x = -2;
				if( x == -1 ) {
					x = b[i][j];
				}
				else if( x == -2 ) {

				}
				else {
					if( x != b[i][j] )
						x = -2;
				}
			}
			if( x > 0 ) {
				break;
			}
		}
		if( x > 0 ) {
			printf("%c won\n", x);
			continue;
		}
		bool unc = false;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(b[i][j] == '.') {
					unc = true;
					break;
				}
			}
			if( unc ) break;
		}
		if( unc ) {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}
	}
	return 0;
}