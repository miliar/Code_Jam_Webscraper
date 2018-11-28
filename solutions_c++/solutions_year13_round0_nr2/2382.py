//
// a.cpp -- A
//
// Siwakorn Sriakaokul - ping128
// Written on Saturday, 13 April 2013.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>

using namespace std;

#define MAXN 105

int in[MAXN][MAXN];
int b[MAXN][MAXN];
int n;

void solve(){
	
	int n, m;
	cin >> n >> m;
	for(int i = 0; i < n; i++ ){
		for(int j = 0; j < m; j++ ){
			cin >> in[i][j];
			b[i][j] = 100;
		}
	}


	for(int i = 0; i < n; i++ ){
		int maxx = -1;
		for(int j = 0; j < m; j++ ){
			maxx = max(maxx, in[i][j]);
		}
		for(int j = 0; j < m; j++ ){
			if(b[i][j] > maxx)
				b[i][j] = maxx;
		}
	}

	for(int j = 0; j < m; j++ ){
		int maxx = -1;
		for(int i = 0; i < n; i++ ){
			maxx = max(maxx, in[i][j]);
		}
		for(int i = 0; i < n; i++ ){
			if(b[i][j] > maxx){
				b[i][j] = maxx;
			}
		}
	}

	for(int i = 0; i < n; i++ ){
		for(int j = 0; j < m; j++ ){
			if(b[i][j] != in[i][j]){
				cout << "NO" << endl;
				return ;
			}
		}
	}
	cout << "YES" << endl;
}


int main()
{
	int test;
	cin >> test;
	for(int tt = 0; tt < test; tt++ ){
		printf("Case #%d: ", tt + 1);
		solve();
	}
	return 0;
}
