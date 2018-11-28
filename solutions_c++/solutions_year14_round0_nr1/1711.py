#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <utility>
#include <bitset>
#include <list>
#define FOR(i, a, b) 	for (i=a; i<b; i++)
#define REV(i, a, b) 	for (i=a; i>=b; i--)
#define TR(tipo, c, it) for (tipo::iterator it=(c).begin(); it!=(c).end(); it++)
#define SET(var, c)		memset(var, c, sizeof(var))
#define READ(file)		freopen(file, "r", stdin)
#define WRITE(file)		freopen(file, "w", stdout)
#define pb 				push_back
#define mp              make_pair
#define X				first
#define Y				second
#define PI				(acos(0.0)*2.0)
#define EPS             1e-10
#define INF 			1000000000
#define LIM             1000

using namespace std;
typedef long long 		ll;
typedef vector<int> 	vi;
typedef pair<int, int> 	ii;
typedef vector<ii> 		vii;

int m1[LIM][LIM], m2[LIM][LIM];

int main(void){
	int i, j, n, caso, ncasos;
	int r1, r2, res;
	bool unico;
	setvbuf(stdin, NULL, _IOFBF, 1<<18);
	setvbuf(stdout, NULL, _IOFBF, 1<<18);
	READ("A-small-attempt0.in");
	WRITE("A-small-attempt0.out");
	scanf("%d", &ncasos);
	FOR(caso, 0, ncasos){
		scanf("%d", &r1);
		FOR(i, 0, 4) FOR(j, 0, 4) scanf("%d", &m1[i][j]);
		scanf("%d", &r2);
		FOR(i, 0, 4) FOR(j, 0, 4) scanf("%d", &m2[i][j]);
		r1--; r2--;
		res=-1;
		unico=true;
		FOR(i, 0, 4)FOR(j, 0, 4){
			if (m1[r1][i]==m2[r2][j]){
				if (res<0) res=m2[r2][j];
				else unico=false;
			}
		}
		printf("Case #%d: ", 1+caso);
		if (res==-1){
			puts("Volunteer cheated!");
			fputs("Volunteer cheated!", stderr);
		}else{
			if (unico){
				printf("%d\n", res);
				fprintf(stderr, "%d\n", res);
			}else{
				puts("Bad magician!");
				fputs("Bad magician!", stderr);
			}
		}
	}
	return 0;
}

