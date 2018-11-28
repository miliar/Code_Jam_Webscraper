										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int r, c;
char mat[110][110];

int main(){
	freopen("A-Pegman.in", "r", stdin);
	freopen("A-Pegman.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> r >> c;
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				cin >> mat[i][j];
		cout << "Case #" << ++test << ": ";
		bool imp = false;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(mat[i][j] == '.')
					continue;
				bool f = false;
				for(int k = 0; k < r; k++)
					if(k != i && mat[k][j] != '.')
						f = true;
				for(int k = 0; k < c; k++)
					if(k != j && mat[i][k] != '.')
						f = true;
				if(!f)
					imp = true;
			}
		}
		if(imp){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		int res = 0;
		for(int i = 0; i < r; i++){
			int p = 0;
			while(p < c && mat[i][p] == '.')
				p++;
			if(p < c && mat[i][p] == '<')
				res++;
			p = c - 1;
			while(p >= 0 && mat[i][p] == '.')
				p--;
			if(p >= 0 && mat[i][p] == '>')
				res++;
		}
		for(int i = 0; i < c; i++){
			int p = 0;
			while(p < r && mat[p][i] == '.')
				p++;
			if(p < r && mat[p][i] == '^')
				res++;
			p = r - 1;
			while(p >= 0 && mat[p][i] == '.')
				p--;
			if(p >= 0 && mat[p][i] == 'v')
				res++;
		}
		cout << res << endl;
	}
	return 0;
}
