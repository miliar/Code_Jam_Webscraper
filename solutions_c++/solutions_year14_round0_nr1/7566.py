#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

using namespace std;

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,r1,r2,x=1;
	cin >>  t ;
	int grid1[4][4],grid2[4][4],arr1[4],arr2[4];
	while(t--){
		cin >> r1 ;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> grid1[i][j];
			}
		}
		r1--;
		for (int i = 0; i < 4; ++i) {
			arr1[i] = grid1[r1][i];
		}
		cin >> r2 ;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> grid2[i][j];
			}
		}
		r2--;
		for (int i = 0; i < 4; ++i) {
			arr2[i] = grid2[r2][i];
		}
		vector<int> v;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if(arr1[i] == arr2[j])
					v.push_back(arr1[i]);
			}
		}
		if(v.size() == 1){
			cout << "Case #" << x << ": " << v[0] << endl;
		}
		else if(v.size() > 1 ){
			cout << "Case #" << x << ": Bad magician!" << endl;
		}
		else {
			cout << "Case #" << x << ": Volunteer cheated!" << endl;
		}
		x++;
	}
}
