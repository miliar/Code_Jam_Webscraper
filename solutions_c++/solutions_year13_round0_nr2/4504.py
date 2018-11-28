#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

int arr[110][110];
int n, m;
int maxInRow[110], maxInCol[110];
void calcMax() {
	for(int i = 0; i < n; i ++) {
		maxInRow[i] = 0;
		for(int j = 0; j < m; j ++) {
			maxInRow[i] = max(maxInRow[i], arr[i][j]);
		}
		//cout << "maxInRow[" << i << "] = " << maxInRow[i] << endl;
	}
	for(int j = 0; j < m; j ++) {
		maxInCol[j] = 0;
		for(int i = 0; i < n; i ++) {
			maxInCol[j] = max(maxInCol[j], arr[i][j]);
		}
		//cout << "maxInCol[" << j << "] = " << maxInCol[j] << endl;
	}
}

bool validate() {
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < m; j ++) {
			if(arr[i][j]==maxInRow[i] || arr[i][j]==maxInCol[j]) {
				
			} else {
				return false;
			}
		}
	}
	return true;
}

int main() {
	freopen("D:\\Downloads\\B-large.in", "r", stdin);
	freopen("sample.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i ++) {
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i ++) {
			for(int j = 0; j < m; j ++) {
				scanf("%d", &arr[i][j]);
			}
		}
		printf("Case #%d: ", i);
		calcMax();
		if(validate()) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}
