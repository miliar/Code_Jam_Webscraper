//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)
#define FOREACH(IT, CON) for(__typeof(CON.begin()) IT=CON.begin(); IT!=CON.end(); ++IT)
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
const int INF=1000000000;
const LL INFLL=1000000000000000000LL;

char t[4][4];

int wy;	// 0 - niedok.,  1 - X,  2 - O,  3 - remis

bool check(const char c){
	REP(I, 4){
		bool czy=true;
		REP(i, 4)
			if (t[I][i]!='T' && t[I][i]!=c){
				czy=false;
				break;
			}
		if (czy) return true;
	}
	REP(I, 4){
		bool czy=true;
		REP(i, 4)
			if (t[i][I]!='T' && t[i][I]!=c){
				czy=false;
				break;
			}
		if (czy) return true;
	}
	bool czy=true;
	REP(i, 4)
		if (t[i][i]!='T' && t[i][i]!=c){
			czy=false;
			break;
		}
	if (czy) return true;
	czy=true;
	REP(i, 4)
		if (t[i][3-i]!='T' && t[i][3-i]!=c){
			czy=false;
			break;
		}
	if (czy) return true;
	return false;
}
int make(){
	if (check('X'))
		return 1;
	if (check('O'))
		return 2;
	REP(i, 4)
		REP(j, 4)
			if (t[i][j]=='.')
				return 0;
	return 3;
}

int main()
{
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		//wej
		REP(i, 4)
			REP(j, 4)
				scanf(" %c", &t[i][j]);
		//prog
		wy=make();
		//wyj
		printf("Case #%d: ", lpt);
		if (wy==0)
			printf("Game has not completed\n");
		else if (wy==1)
			printf("X won\n");
		else if (wy==2)
			printf("O won\n");
		else
			printf("Draw\n");
	}
	return 0;
}

