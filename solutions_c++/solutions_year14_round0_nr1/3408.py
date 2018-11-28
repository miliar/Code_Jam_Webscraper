#include <bits/stdc++.h>
#include <cassert>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define FOR(i,a,b)   for(int(i)=int(a);(i)<int(b);(i)++)
#define FOREQ(i,a,b) for(int(i)=int(a);(i)<=int(b);(i)++)
#define RFOR(i,a,b)  for(int(i)=(a),_b(b);(i)>=_b;--(i))
#define FOREACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define FILL(arr,val) memset((arr),(val),sizeof(arr))
#define CLR(a)        memset((a),0,sizeof(a))
#define CPY(dest,src) memcpy((dest),(src),sizeof(dest))

#define ALL(a)       (a).begin(),(a).end()
#define SZ(a)        ((int)(a).size())
#define UNIQ(a)      sort(ALL(a)); (a).erase(unique(ALL(a)),(a).end())
#define IDX(arr,ind) (lower_bound(ALL(arr),ind)-arr.begin())

#define fst first
#define snd second
#define pb  push_back
#define mp  make_pair

static int T;

int main()
{
	scanf("%d", &T);
	FOREQ(t,1,T)
	{
		int first = -1;
		scanf("%d", &first);
		first--;

		int grid1[4][4] = {0};
		FOR(i,0,4) {
			FOR(j,0,4) {
				scanf("%d", &grid1[i][j]);
			}
		}
		bool act1[16];
		FOR(i,0,16) act1[i] = false;
		FOR(i,0,4) {
			act1[ grid1[first][i]-1 ] = true;
		}

		int second = -1;
		scanf("%d", &second);
		second--;

		int grid2[4][4] = {0};
		FOR(i,0,4) {
			FOR(j,0,4) {
				scanf("%d", &grid2[i][j]);
			}
		}
		bool act2[16];
		FOR(i,0,16) act2[i] = false;
		FOR(i,0,4) {
			act2[ grid2[second][i]-1 ] = true;
		}

		int cnt = 0, guess = -1;
		FOR(i,0,16) {
			if (act1[i] && act2[i]) {
				cnt++;
				guess = i+1;
			}
		}

		if (cnt == 0) {
			printf("Case #%d: Volunteer cheated!\n", t);
		} else if (cnt == 1) {
			printf("Case #%d: %d\n", t, guess);
		} else {
			printf("Case #%d: Bad magician!\n", t);
		}

	}
	return 0;
}
