#include <cstdio>
#include <algorithm>

using namespace std;

int z, n, m;
int t[109][109];
bool poz[109][109], pion[109][109];
bool dasie;

int main() {
	scanf("%d", &z);
	for(int casen = 1; casen <= z; casen++) {
		dasie = true;
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++) {
				scanf("%d", &t[i][j]);
				poz[i][j] = pion[i][j] = false;
			}
		for(int i = 0; i < n; i++) {
			int ma = -1;
			for(int j = 0; j < m; j++) if(t[i][j] > ma) ma = t[i][j];
			for(int j = 0; j < m; j++) if(t[i][j] < ma) pion[i][j] = true;
		}
		for(int i = 0; i < m; i++) {
			int ma = -1;
			for(int j = 0; j < n; j++) if(t[j][i] > ma) ma = t[j][i];
			for(int j = 0; j < n; j++) if(t[j][i] < ma) poz[j][i] = true;
		}
		for(int i = 0; i < n; i++) {
			int strz = 101;
			for(int j = 0; j < m; j++) if(poz[i][j]) strz = min(strz, t[i][j]);
			for(int j = 0; j < m; j++) if(strz < t[i][j]) dasie = false;
		}
		for(int i = 0; i < m; i++) {
			int strz = 101;
			for(int j = 0; j < n; j++) if(pion[j][i]) strz = min(strz, t[j][i]);
			for(int j = 0; j < n; j++) if(strz < t[j][i]) dasie = false;
		}
		printf("Case #%d: ", casen);
		if(dasie) printf("YES\n");
		else printf("NO\n");
	}
}
