#include <iostream>
#include <stdio.h>
using namespace std;

int s[100][100];
int line_large[100], col_large[100];

int slution(int m, int n){
	for(int j = 0; j < n; ++j){
		int max = s[0][j];
		for(int i = 0; i < m; ++i){
			int x = s[i][j];
			if(x > max) max = x;
		}
		col_large[j] = max;
	}
	
	for(int i = 0; i < m; ++i)
		for(int j = 0; j < n; ++j){
			int x = s[i][j];
			if(line_large[i] > x && col_large[j] > x )
				return 0;
		}
	return 1;
}

int main(void){
	int n, k = 0;
	cin >> n;
	while(k++ < n){
		int m, n;
		cin >> m >> n;
		for(int i = 0; i < m; ++i){
			int max = -1;
			for(int j = 0; j < n; ++j){
				int t;
				cin >> t;
				s[i][j] = t;
				if(t > max) max = t;
			}
			line_large[i] = max;
		}
		if(slution(m, n)) printf("Case #%d: YES\n", k);
		else printf("Case #%d: NO\n", k);
	}
	
	return 0;

}