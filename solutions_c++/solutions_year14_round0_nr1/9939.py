#include <iostream>
#include <iomanip>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include<cstdio>
using namespace std;

int main(void) {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t,c=1;
	cin >> t;
	while (t--){
		long long a[4][4], b[4][4],n[4],p,q;
		cin >> p;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> q;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> b[i][j];
		int cnt = 0,ans=-1;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (a[p-1][i] == b[q-1][j]){
					ans = a[p-1][i], cnt++;
				}					
			}
		}
		if (cnt == 1){
			printf("Case #%d: %d\n", c++, ans);
			continue;
		}
		else if (cnt>1){
			printf("Case #%d: Bad magician!\n", c++);
		}
		else if (cnt == 0){
			printf("Case #%d: Volunteer cheated!\n", c++);
		}			
	}
	return 0;
}