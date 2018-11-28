//--BY--©--WA-
#include<iostream> //cout, cin, getline

#include<algorithm> //find, reaplce, swap, sort, lower_bound, uper_bound, binnary_search...
#include<vector> //push_back, size, resize, 
#include<string>
#include<queue> //empty, front, back, push
#include<stack> //push, top, empty
#include<map>
#include<set>
#include<list> //spajazny zoznam .. vsetko v O(1)

#include<stdio.h> //printf, scanf, getchar, putchar
#include<math.h> //cos, sin, exp, pow, sqrt,  flnoor, cell
#include<stdlib.h> //atio, atl, strtod, strtol, atof, abs, 
#include<ctype.h> //isalnum, isalpha, isdigit, islower, isupper, toupper, tolower, 
#include<string.h> //strcm, strstr, strlen,

using namespace std;

#define FOREACH(obj,it) for(__typeof(obj.begin()) it = (obj).begin(); it != (obj).end(); (it)++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--)
#define REP(i,a,b) for(int i=a; i<b; i++)
#define DEBUG(V,S) FOR(i,0,S-1){cout << i << ". " << V[i] << endl;}

#define PB push_back
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define MP make_pair
#define fi first
#define se second

#define SIZE(s) (int) (s).size()

#define INF 987654321
#define EPS 1e-9
#define ld long double // %Lf, double %lf
#define ll long long   // %llf

//--------------------------------------------------------------------------------------
//


int N;
char mat[4][4];

bool check_rows(char c) {
	FOR (i, 0, 3) {
		bool ok = true;
		FOR (j, 0, 3) {
			if (mat[i][j] != c && mat[i][j] != 'T') ok = false;
		}
		if (ok == true) return true;
	}
	return false;
}

bool check_cols(char c) {
	FOR (i, 0, 3) {
		bool ok = true;
		FOR (j, 0, 3) {
			if (mat[j][i] != c && mat[j][i] != 'T') ok = false;
		}
		if (ok == true) return true;
	}
	return false;
}

bool check_diags(char c) {
	bool ok = true;
	FOR (i, 0, 3)
		if (mat[i][i] != c && mat[i][i] != 'T') ok = false;
	if (ok == true) return true;

	ok = true;
	FOR (i, 0, 3)
		if (mat[i][3-i] != c && mat[i][3-i] != 'T') ok = false;
	if (ok == true) return true;

	return false;
}

bool filled() {
	FOR (i, 0, 3)
		FOR (j, 0, 3)
			if (mat[i][j] == '.') return false;

	return true;
}

int main()
{

	scanf("%d\n", &N);
	FOR (q, 1, N) {
		printf("Case #%d: ", q);

		FOR (y, 0, 3) {
			FOR (x, 0, 3) {
				scanf("%c", &(mat[x][y]));
			}
			scanf("\n");
		}
		scanf("\n");
		
		if (check_rows('X') || check_cols('X') || check_diags('X')) {
			printf("X won\n");
		} else if (check_rows('O') || check_cols('O') || check_diags('O')) {
			printf("O won\n");
		} else {
			if (filled()) printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}
	
	return 0;
}
