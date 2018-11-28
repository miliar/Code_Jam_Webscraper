#include <bits/stdc++.h>
using namespace std; 
/* 0 represents 1, 1 represents i, 2 represents j, 3 represents k, 4 represents -1, 
 * 5 represents -i, 6 represents -j, 7 represents -k 
 */
 map <char, int> m;
int main() {
	m['i'] = 1;
	m['j'] = 2;
	m['k'] = 3;
	int quaternion[8][8] = {{0, 1, 2, 3, 4, 5, 6, 7},
							{1, 4, 3, 6, 5, 0, 7, 2},
							{2, 7, 4, 1, 6, 3, 0, 5},
							{3, 2, 5, 4, 7, 6, 1, 0},
							{4, 5, 6, 7, 0, 1, 2, 3},
							{5, 0, 7, 2, 1, 4, 3, 6},
							{6, 3, 0, 5, 2, 7, 4, 1},
							{7, 6, 1, 0, 3, 2, 5, 4}};
	int t;
	int z = 1;
	scanf("%d", &t);
	while(t--) {
		int n, x;
		scanf("%d%d", &n, &x);
		int i;
		char input[20005];
		scanf("%s", input);
		char str[10005];
		for(i = 0; i < n; i++) {
			str[i] = input[i];
		}
		str[n] = '\0';
		for(i = 0; i < x - 1; i++) {
			strcat(input, str);
		}
		int len = strlen(input);
		int y = 0;
		int posi = INT_MAX;
		int posk = INT_MIN;
		int posinv1 = INT_MIN;
		for(i = 0; i < len; i++) {
			int ind = m[input[i]];
			y = quaternion[y][ind];
			if(y == 1) {
				posi = min(posi, i);
			} else if(y == 3){
				posk = max(posk, i);
			} else if(y == 4) {
				posinv1 = max(posinv1, i);
			}
		}
		//printf("%d %d %d\n", posi, posk, posinv1);
		if(posinv1 + 1 == len && posi < posk && posk < posinv1) {
			printf("Case #%d: YES\n", z++);
		} else {
			printf("Case #%d: NO\n", z++);
		}
		/*
		int subpart = 0;
		for(i = 1; i <= n; i++) {
			int ind = m[input[i]];
			subpart = quaternion[subpart][ind];
		}
		//printf("%d\n", subpart);
		int tempsubpart = 0;
		int visited[10], visited3[10];
		int cnt = 0;
		for(i = 0; i < 10; i++) {
			visited[i] = INT_MAX;
			visited3[i] = INT_MIN;
		}
		while(cnt < x) {
			visited[tempsubpart] = min(visited[tempsubpart], (cnt++) * n);
			tempsubpart = quaternion[tempsubpart][subpart];
		}
		tempsubpart = 0;
		cnt = 0;
		while(cnt < x) {
			visited3[tempsubpart] = max(visited3[tempsubpart], (cnt++) * n);
			tempsubpart = quaternion[tempsubpart][subpart];
		}
		/*for(i = 0; i < 10; i++) {
			printf("%d %d\n", i, visited[i]);
		}*/
		/*
		int visited2[10];
		visited2[1] = INT_MAX;
		visited2[3] = INT_MIN;
		visited2[4] = INT_MIN;
		for(i = 0; i < 10; i++) {
			if(visited[i] != INT_MAX) {
				int j;
				tempsubpart = i;
				for(j = 1; j <= n; j++) {
					int ind = m[input[j]];
					tempsubpart = quaternion[tempsubpart][ind];
					if(tempsubpart == 1) {
						if(visited[i] + j <= x * n)
							visited2[1] = min(visited2[1], visited[i] + j);
					} else if(tempsubpart == 3 || tempsubpart == 4) {
						if(visited3[i] + j <= x * n)
						visited2[tempsubpart] = max(visited2[tempsubpart], visited3[i] + j);
					}
				}
			}
		}
		//printf("%d %d %d\n",visited2[1], visited2[3], visited2[4]);
		if(visited2[1] < visited2[3] < visited2[4] && visited2[4] / n == x) {
			printf("Case #%d: YES\n", z++);
		} else {
			printf("Case #%d: NO\n", z++);
		}
		*/

	}
	return 0;
}