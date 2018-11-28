/*Santiago Zubieta*/
#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>  

using namespace std;

int main(){
	int T, row[2], grid[2][4][4];
	scanf("%d", &T);
	for(int z = 0; z < T; z++){
		for(int k = 0; k < 2; k++){
			scanf("%d", &row[k]);
			row[k]--;
			for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
					scanf("%d", &grid[k][i][j]);
				}
			}
		}
		set<int> das_set;
		int res[17];
		for(int i = 1; i <= 16; i++){
			res[i] = 0;
		}
		for(int k = 0; k < 2; k++){
			for(int i = 0; i < 4; i++){
				int num = grid[k][row[k]][i];
				das_set.insert(num);
				res[num]++;
			}
		}
		int setSize = das_set.size();
		printf("Case #%d: ", z + 1);
		if(setSize == 7){
			for(int i = 1; i <= 16; i++){
				if(res[i] == 2){
					printf("%d", i);
				}
			}
		}
		if(setSize == 8){
			printf("Volunteer cheated!");
		}
		if(setSize < 7){
			printf("Bad magician!");
		}
		if(z + 1 < T){
			puts("");
		}
	}
}