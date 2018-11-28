#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <iostream>
#include <cstdio>

#define swap(type, x, y) {type t = x; x = y; y = t}

using namespace std;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T, case_no = 0;
	cin>>T;
	while(T--){
		case_no++;
		int ans1, ans2, grid1[4][4], grid2[4][4];
		cin>>ans1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin>>grid1[i][j];

		cin>>ans2;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin>>grid2[i][j];

		ans1--;
		ans2--;

		int found = 0, ans;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(grid1[ans1][i] == grid2[ans2][j]){
					found++;
					ans = grid1[ans1][i];
				}

		if(found == 1)
			printf("Case #%d: %d\n", case_no, ans);
		else if(found > 1)
			printf("Case #%d: Bad magician!\n", case_no);
		else
			printf("Case #%d: Volunteer cheated!\n", case_no);
	}

	return 0;
}