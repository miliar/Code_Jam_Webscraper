#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include<string.h>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include<string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

#define rep(i,n) for (int i =0; i<n ; i++)
#define lp(j,n) for(int j=0;j<n;j++)

using namespace std;


int s[4][4], s1[4][4];
int t, x, y, cnt ,res;

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.in", "w", stdout);

	cin >> t;
	lp(k, t) {

	cin >> x;
	rep(i, 4) {
		rep(j, 4)
			cin >> s[i][j];
	}
	cin >> y;
	rep(i, 4) {
		rep(j, 4)
			cin >> s1[i][j];
	} 
	cnt = 0;
	res = 0;
	lp(i, 4){
		lp(j, 4){
			if (s1[y-1][j]==s[x-1][i]){
				cnt++;
				res = s[x-1][i];
			}	
		}
	}
		
	
	if (cnt == 1)
		cout << "Case #" << k+1 << ": " << res << endl;
	else if (cnt == 0) 
		cout << "Case #" << k + 1 << ": Volunteer cheated!" << endl; 
	else if (cnt > 1)
		cout << "Case #" << k + 1 << ": Bad magician!" << endl;
}

	return 0;
}