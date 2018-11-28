#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define INF	(int)1e9
#define EPS 1e-9
#define what_is(x) cerr << #x << " is " << x << endl;

int dir[8][2] = {{1,1},{1,0},{1,-1},{0,-1},   // NE,E,SE,S
			    {-1,-1},{-1,0},{-1,1},{0,1}}; // SW,W,NW,N

int dir2[4][2] = {{1,0}, {0,-1}, {-1, 0}, {0,1}};

int main(){
	int tc, casenum = 1;
	scanf("%d", &tc);
	while(tc--){
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		printf("Case #%d: ", casenum++);
		if(x == 1) {
			printf("GABRIEL\n");
		} else if(x == 2){
			if((r*c) & 1) printf("RICHARD\n");
			else printf("GABRIEL\n");
		} else if (x == 3){
			if(r == 1 || c == 1) printf("RICHARD\n");
			else if((r*c) % 3 == 0) printf("GABRIEL\n");
			else printf("RICHARD\n");
		} else if (x == 4){
			if(r == 1 || c == 1 || r == 2 || c == 2) printf("RICHARD\n");
			else if((r*c) % 4 == 0) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
	}
}