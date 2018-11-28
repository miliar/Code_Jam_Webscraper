#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int n,t,m;
typedef long long ll;
int array[101][101];
bool pode[101][101];
bool ja[201];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		memset(pode, 0, sizeof pode);
		memset(ja, 0, sizeof ja);
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				scanf("%d", &array[i][j]);
				
		for(int k = 1; k < 100; ++k){
			for(int i = 0; i < m; ++i) if(!ja[i] && array[0][i] <= k){
				for(int j = 1; j < n; ++j)
					if(array[j][i] > k) goto falhou;
				for(int j = 0; j < n; ++j)
					pode[j][i] = true;
				ja[i] = true;
				falhou:;
			}
			
			for(int i = 0; i < n; ++i) if(!ja[i+100] && array[i][0] <= k){
				for(int j = 1; j < m; ++j)
					if(array[i][j] > k) goto falhou2;
				for(int j = 0; j < m; ++j)
					pode[i][j] = true;
				ja[i+100] = true;
				falhou2:;
			}
				
			for(int i = 0; i < n; ++i)
				for(int j = 0; j < m; ++j)
					if(array[i][j] == k && !pode[i][j]) goto fail;
		}
		printf("Case #%d: YES\n", _);
		continue;
		fail:
		printf("Case #%d: NO\n", _);
	}
	return 0;
}
