#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;

typedef long long ll;

char a[110][110];

int rsum[110];
int csum[110];

int main() {
	
	int T;
	scanf("%d", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		int R,C;
		scanf(" %d %d", &R,&C);
		
		memset(rsum, 0, sizeof(rsum));
		memset(csum, 0, sizeof(csum));
		
		int count = 0;
		
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				scanf(" %c", &a[i][j]);
				if(a[i][j] != '.') {
					count++;
					rsum[i]++;
					csum[j]++;
				}
			}
		}
		
		bool pos = true;
		
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(rsum[i] == 1 && csum[j] == 1 && a[i][j] != '.') pos = false;
			}
		}
		
		if(!pos) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		
			
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				switch(a[i][j]) {
					case '^': 
						for(int ri = i-1; ri >= 0; ri--) {
							if(a[ri][j] != '.') {
								count--;
								break;
							}
						}	
						break;
					
					case 'v': 
						for(int ri = i+1; ri < R; ri++) {
							if(a[ri][j] != '.') {
								count--;
								break;
							}
						}	
						break;
						
					case '>': 
						for(int ci = j+1; ci < C; ci++) {
							if(a[i][ci] != '.') {
								count--;
								break;
							}
						}	
						break;
						
					case '<': 
						for(int ci = j-1; ci >= 0; ci--) {
							if(a[i][ci] != '.') {
								count--;
								break;
							}
						}
						break;
						
					case '.':
						break;
						
					default:
						break;
				}
			}
		}
		
		printf("%d\n", count);
	}
	
	return 0;
}
