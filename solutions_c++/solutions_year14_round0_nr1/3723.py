#include <cstdio>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#define VAR(i,v) auto i = (v)
#define SIZE(x) ((int)(x).size())
#define ALL(x) (x).begin(), (x).end()
#define REP(i,b) for(int i=0; i<(b); ++i)
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

using namespace std;
typedef vector<int> VI;
typedef long long LL;

const int MAXN = 4;

int arr[MAXN][MAXN];
int arr2[MAXN][MAXN];
int n;

int is_in_vector(VI& V, int x) {
	for(int y: V) if (x==y) return x;
	return 0;
}

int main() {
	scanf("%d", &n);
	
	REP(i,n) {
		int ans_a = 0, ans_b = 0;
		scanf("%d", &ans_a);
		REP(i,4) REP(j,4) scanf("%d", &arr[i][j]);
		scanf("%d", &ans_b);
		REP(i,4) REP(j,4) scanf("%d", &arr2[i][j]);
		
		VI first_poss;
		REP(i,4) first_poss.PB(arr[ans_a-1][i]);

		int ans = 0;
		int val = 0;
		REP(i,4) {
			int val2 = is_in_vector(first_poss, arr2[ans_b-1][i]);
			if (val2!=0) {
				val = val2;
				ans++;
			}
		}


		printf("Case #%d: ", i+1);
		if (ans == 1) printf("%d\n", val);
		else if (ans == 0) printf("Volunteer cheated!\n");
		else if (ans > 1) printf("Bad magician!\n");

	}

	return 0;

}
