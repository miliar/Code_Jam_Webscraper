#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 200;
const int inf = 2000000;
int lawn[MAXN][MAXN];
int model[MAXN][MAXN];

bool solve(int n, int m){
	
	for(int i = 0; i < n; i++){
		/// each line
		int maxlawn = 0;
		for(int j = 0; j < m; j++)
			maxlawn = max(maxlawn, lawn[i][j]);
		for(int j = 0; j < m; j++)
			model[i][j] = maxlawn;
		}
	
	for(int i = 0; i < m; i++){
		int maxlawn = 0;
		for(int j = 0; j < n; j++)
			maxlawn = max(maxlawn, lawn[j][i]);
		for(int j = 0; j < n; j++)
			model[j][i] = min(maxlawn, model[j][i]);
		}
	
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if( model[i][j] != lawn[i][j] )
				return false;
	return true;
	}

int main(){
	int testcases;
	scanf("%d", &testcases);
	
	int n, m;
	for(int testcase = 0; testcase < testcases; testcase++){
		scanf("%d%d", &n, &m);
		
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				scanf("%d", &lawn[i][j]);
		
		if(solve(n, m))
			printf("Case #%d: YES\n", testcase+1);
		else
			printf("Case #%d: NO\n", testcase+1);
		}
	
	
	return 0;
}
