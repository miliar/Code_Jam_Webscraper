/*
*	Category: CodeJam
*  Problem: B.Lawnmower.cpp
*  Status:
* 	Date: Apr 13, 2013
* 	Time: 8:44:20 AM
* 	Author: Hossam Yousef
*/

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

int grid[100][100];

int main() {
	freopen("test.txt", "rt", stdin);
		freopen("o.txt", "wt", stdout);
	int tc, N, M;
	scanf("%d",&tc);
	for(int t = 1; t <= tc; t++){
		int MX;
		vector<int> I;
		vector<int> J;
		scanf("%d%d",&N,&M);
		for(int i = 0; i < N; i++)
			for(int j = 0; j < M; j++){
				scanf("%d",&grid[i][j]);
				MX = max(MX,grid[i][j]);
			}
			int temp1 = 0, temp2 = 0;
			for(int T = 1; T < MX; T++){
				for(int i = 0; i < N; i++){
					for(int j = 0; j < M; j++){
						if(grid[i][j] == T){
							temp1 = 0;
							for(int a = 0; a < N; a++){
								if(grid[a][j] == T)temp1++;
							}
							temp2 = 0;
							for(int a = 0; a < M; a++){
								if(grid[i][a] == T)temp2++;
							}
							if(temp1 == N){
								I.push_back(j);
							}
							if(temp2 == M){
								J.push_back(i);
							}
						}
					}
				}
				for(int i = 0; i < (int)I.size(); i++)
				{
					for(int a = 0; a < N; a++){
						grid[a][I[i]] = T+1;
					}
				}
				I.clear();
				for(int i = 0; i < (int)J.size(); i++)
				{
					for(int a = 0; a < M; a++){
						grid[J[i]][a] = T+1;
					}
				}
				J.clear();
			}
			int temp = 0;
			for(int i = 0; i < N; i++){
				for(int j = 0; j < M; j++){
					if(grid[i][j] == MX) temp++;
				}
			}
			if(temp == N*M) printf("Case #%d: YES\n",t);
			else printf("Case #%d: NO\n",t);

	}
	return 0;
}
