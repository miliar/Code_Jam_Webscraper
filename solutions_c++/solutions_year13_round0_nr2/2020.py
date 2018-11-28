#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

template<class T>
class point {
	public:
	T x, y;
	point() {}
	point(T a, T b)
	{ x = a, y = b; }
	bool operator < (const point &other)
	const{ return x == other.x? y < other.y : x > other.x; }
};

int matrix[110][110], n, m, nmatrix[110][110];
point<int> rows[110], cols[110];

int main()
{
	int t; scanf("%d",&t);
	for(int p = 1; p <= t; ++p) {
		scanf("%d %d",&n,&m);
		for(int i = 0; i < n; ++i)
			rows[i] = point<int>(0,i);
		for(int i = 0; i < m; ++i)
			cols[i] = point<int>(0,i);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j) {
				scanf("%d",&matrix[i][j]);
				rows[i].x = max(rows[i].x, matrix[i][j]);
				cols[j].x = max(cols[j].x, matrix[i][j]);
			}
		sort(rows, rows + n);
		sort(cols, cols + m);
		for(int i = 0, j = 0, k = 0; i < n + m; ++i) {
			if(j < n && k < m) {
				if(rows[j].x > cols[k].x) {
					for(int l = 0; l < m; ++l) {
						nmatrix[rows[j].y][l] = rows[j].x;
					}
					j++;
				}
				else {
					for(int l = 0; l < n; ++l) {
						nmatrix[l][cols[k].y] = cols[k].x;
					}
					k++;
				}
			}
			else if(j < n) {
				for(int l = 0; l < m; ++l) {
					nmatrix[rows[j].y][l] = rows[j].x;
				}
				j++;
			}
			else {
				for(int l = 0; l < n; ++l) {
					nmatrix[l][cols[k].y] = cols[k].x;
				}
				k++;
			}
		}
		bool valid = true;
		printf("Case #%d: ",p);
		for(int i = 0; i < n && valid; ++i) {
			for(int j = 0; j < m && valid; ++j) {
				if(matrix[i][j] != nmatrix[i][j]) {
					printf("NO\n");
					valid = false;
				}
			}
		}
		if(valid) printf("YES\n");
	}
	return 0;
}
