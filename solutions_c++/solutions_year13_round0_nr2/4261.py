#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <string>
#include <iostream>
#include <algorithm>

#include <vector>
#include <map>
#include <queue>

#define dbg(a) cout << a << endl

using namespace std;

int mat[110][110], li[110], co[110], n, m;

void read(){
	scanf("%d %d", &n, &m);
	memset(li, 0, (n+1)*sizeof(int));
	memset(co, 0, (m+1)*sizeof(int));

	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			scanf("%d", &mat[i][j]);
			li[i] = max(li[i], mat[i][j]);
			co[j] = max(co[j], mat[i][j]);
		}
	}
}

void process(){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(mat[i][j] < li[i] && mat[i][j] < co[j]){
				printf("NO\n");
				return;
			}
		}
	}

	printf("YES\n");
}

int main(){

	int t;
	scanf("%d", &t);

	for(int caso = 1; caso <= t; caso++){
		read();

		printf("Case #%d: ", caso);
		process();
	}

	return 0;
}
