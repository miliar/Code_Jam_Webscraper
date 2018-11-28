#include <cstdio>

#define fo(x,y,z) for(int x = 0; x < y; x+=z)
#define fi(x) fo(i,x,1)
#define fj(x) fo(j,x,1)

int main(){
	bool ch[105][105];
	int t, n, m, map[105][105], maxr[105], maxc[105];
	scanf("%d", &t);
	for(int x = 1; x <= t; x++){
		bool pos = true;
		scanf("%d %d", &n, &m);
		fi(n) fj(m){
			scanf("%d", &map[i][j]);
			ch[i][j] = false;
		}

		fi(n){
			int max = -1;
			fj(m){
				if(max < map[i][j]) max = map[i][j];
			}
			maxr[i] = max;
		}
		fi(m){
			int max = -1;
			fj(n){
				if(max < map[j][i]) max = map[j][i];
			}
			maxc[i] = max;
		}
		fi(n){
			fj(m){
				if(maxr[i] > map[i][j] && maxc[j] > map[i][j]){
					pos = false;
				}
			}
		}

		printf("Case #%d: %s\n", x, pos?"YES":"NO"); 
	}
	return 0;
}