#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

ifstream fin("1.in");
ofstream fout("1.out");

char grid[100][100];

int main(){
	int nCases;
	fin >> nCases;
	for(int t=1;t<=nCases;t++){
		int r,c;
		fin >> r >> c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++)			
				fin >> grid[i][j];
		}

		int count = 0;
		int possible = true;

		int dir[2];
		int cur[2];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){			
				if(grid[i][j] != '.'){
					if(grid[i][j] == '<'){
						dir[0] = 0;
						dir[1] = -1;
					}
					if(grid[i][j] == '>'){
						dir[0] = 0;
						dir[1] = 1;
					}
					if(grid[i][j] == '^'){
						dir[0] = -1;
						dir[1] = 0;
					}
					if(grid[i][j] == 'v'){
						dir[0] = 1;
						dir[1] = 0;
					}

					cur[0] = i;
					cur[1] = j;
					bool found = false;
					while(true){
						cur[0] += dir[0];
						cur[1] += dir[1];
						if(cur[0] < 0 || cur[0] >= r || cur[1] < 0 || cur[1] >= c)
							break;
						if(grid[cur[0]][cur[1]] != '.'){
							found = true;
							break;
						}
					}
					if(!found){
						count++;
						grid[i][j] = 'x';
					}
				}
			}
		}

		int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){			
				if(grid[i][j] == 'x'){
					bool found = false;
					for(int d=0;d<4;d++){
						dir[0] = dirs[d][0];
						dir[1] = dirs[d][1];

						cur[0] = i;
						cur[1] = j;
						while(true){
							cur[0] += dir[0];
							cur[1] += dir[1];
							if(cur[0] < 0 || cur[0] >= r || cur[1] < 0 || cur[1] >= c)
								break;
							if(grid[cur[0]][cur[1]] != '.'){
								found = true;
								break;
							}
						}
						if(found)
							break;
					}
					if(!found)
						possible = false;
				}
			}
		}
		
		if(!possible)
			fout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else
			fout << "Case #" << t << ": " << count << endl;
	}
	return 0;
}