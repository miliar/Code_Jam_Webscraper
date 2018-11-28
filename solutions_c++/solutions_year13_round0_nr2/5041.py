#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.o", "w+", stdout);

	int t;
	int m;
	int n;
	int tempNum;
	bool canCutm;
	bool canCutn;
    cin >> t;
	char buffer[300];
	int lawn[100][100];
	
	for(int ti = 0; ti < t; ti++){
		cout << "Case #" << (ti+1) << ": ";
		cin >> m;
		cin >> n;
		for(int mi = 0; mi < m; mi++){
			for(int ni = 0; ni < n; ni++){
				cin >> lawn[mi][ni];	 
			}
		}
		for(int mi = 0; mi < m; mi++){
			for(int ni = 0; ni < n; ni++){
				tempNum = lawn[mi][ni];
				canCutm = 1;
				canCutn = 1;
				for(int mj = 0; mj < m; mj++){
					canCutm = canCutm & (lawn[mj][ni] <= tempNum);
				}
				for(int nj = 0; nj < n; nj++){
					canCutn = canCutn & (lawn[mi][nj] <= tempNum);
				}
				if(!(canCutm|canCutn)){
					break;
				}
			}
			if(!(canCutm|canCutn)){
				break;
			}
		}
		if(!(canCutm|canCutn)){
			cout << "NO\n";
		}
		else{
			cout << "YES\n";
		}
	}
}