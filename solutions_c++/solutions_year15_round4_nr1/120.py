#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue>
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

typedef long long ll; 
typedef pair<int, int> pii;

#define INF 1000000000
#define pb push_back 
#define itr iterator 
#define sz size() 
#define mp make_pair

int T, teste;
int r, c;
char bd[110][110];

char arr[]="v<^>";
int dx[]={1,0,-1,0};
int dy[]={0,-1,0,1};

bool inside(int x, int y) {
	return x >= 0 && x < r && y >= 0 && y < c;
}

int main() {
	for (scanf("%d", &T); T; T--) {
		printf("Case #%d: ", ++teste);
		scanf("%d %d", &r, &c);
		
		int ans = 0;

		for (int i = 0; i < r; i++) {
			scanf("%s", bd[i]);
		}

		bool imp = false;

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (bd[i][j] == '.') continue;

				bool ok[4] = {false, false, false, false};
				bool any = false;

				for (int d = 0; d < 4; d++) {
					int cx = i + dx[d], cy = j + dy[d];
					while (true) {
						if (!inside(cx,cy)) break;
						if (bd[cx][cy] != '.') {
							ok[d] = true;
							any = true;
							break;
						}
						cx += dx[d];
						cy += dy[d];
					}
				}

				int d;
				for (int k = 0; k < 4; k++) {
					if (bd[i][j] == arr[k]) d = k;
				}

				if (!ok[d]) {
					if (!any) imp = true;
					else ans++;
				}
			}
		}

		if (imp) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
}