#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) ((x) * (x))
#define len(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'

#ifdef CUTEBMAING
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) ({})
#endif

using namespace std;

typedef long long int64;
typedef unsigned long long lint;
typedef long double ld;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);

int main(){
	int T; cin >> T;
	for (int t = 0; t < T; t++){
		printf("Case #%d: ", t + 1);
		int r1; cin >> r1; r1--;
		int a[4][4];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> a[i][j];
		int r2; cin >> r2; r2--;
		int b[4][4];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> b[i][j];
		int ans = -1, cnt = 0;
		for (int i = 0; i < 4; i++)
			if (find(b[r2], b[r2] + 4, a[r1][i]) != b[r2] + 4){
				ans = a[r1][i];
				cnt++;
			}
		if (cnt == 0)
			puts("Volunteer cheated!");
		else if (cnt > 1)
			puts("Bad magician!");
		else
			printf("%d\n", ans);
	}
    return 0;
}
