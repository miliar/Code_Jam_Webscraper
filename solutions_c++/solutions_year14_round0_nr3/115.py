#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <assert.h>
using namespace std;

char grid[50][50];
int t,r,c;
ifstream fin("large.in");

void printIt(){
	cout << "Case #" << t+1 << ":" << endl;
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			cout << grid[i][j];
		}
		cout << endl;
	}
}
void impossible(){
	cout << "Case #" << t+1 << ": " << endl << "Impossible" << endl;
}

int main(){
	int nt;
	fin >> nt;
	for(t=0;t<nt;t++){
		memset(grid,'.',sizeof(grid));
		int  m, empty;
		fin >> r >> c >> m;
		empty = r*c - m;
		if(min(r,c) == 1){
			if(r==1){
				for(int i=0;i<m;i++){
					grid[0][i] = '*';
				}
				grid[0][c-1] = 'c';
			}
			else{
				for(int i=0;i<m;i++){
					grid[i][0] = '*';
				}
				grid[r-1][0] = 'c';
			}
			printIt();
			continue;
		}
		else if(min(r,c) == 2){
			if(m%2 == 0){
				if(empty == 2){
					impossible();
					continue;
				}
				else{
					if(r==2){
						for(int i=0;i<m/2;i++){
							grid[0][i] = '*';
							grid[1][i] = '*';
						}
					}
					else{
						for(int i=0;i<m/2;i++){
							grid[i][0] = '*';
							grid[i][1] = '*';
						}
					}
					grid[r-1][c-1] = 'c';
					printIt();
					continue;
				}
			}
			else{
				assert(m%2 == 1);
				if(empty == 1){
					for(int i=0;i<r;i++){
						for(int j=0;j<c;j++){
							grid[i][j] = (i==r-1 && j==c-1)?'c':'*'; 
						}
					}
					printIt();
					continue;
				}
				else{
					impossible();
					continue;
				}
			}
		}
		else{
			for(int i=0;i<r-2;i++){
				for(int j=0;j<c-2;j++){
					if(m){
						grid[i][j] = '*';
						m--;
					}
				}
			}
			if(m==0){
				grid[r-1][c-1] = 'c';
				printIt();
				continue;
			}

			if(empty%2 == 0){
				for(int j=0;j<c-2;j++){
					for(int i=r-2;i<r;i++){
						if(m){
							grid[i][j] = '*';
							m--;
						}
					}
				}
				for(int i=0;i<r-2;i++){
					for(int j=c-2;j<c;j++){
						if(m){
							grid[i][j] = '*';
							m--;
						}
					}
				}
				if(m==0){
					grid[r-1][c-1] = 'c';
					printIt();
					continue;
				}
				else if(m == 1 || m == 2){
					impossible();
					continue;
				}
				else if (m==3){
					grid[r-1][c-1] = 'c';
					grid[r-2][c-2] = '*';
					grid[r-1][c-2] = '*';
					grid[r-2][c-1] = '*';
					printIt();
					continue;
				}
				else{
					assert(false);
				}
			}
			else{
				assert(r==2 || c==2 || grid[r-3][c-3] == '*');
				grid[r-2][c-2] = '.';
				m++;
				for(int j=0;j<c-3;j++){
					for(int i=r-2;i<r;i++){
						if(m){
							grid[i][j] = '*';
							m--;
						}
					}
				}
				for(int i=0;i<r-3;i++){
					for(int j=c-2;j<c;j++){
						if(m){
							grid[i][j] = '*';
							m--;
						}
					}
				}
				if(m==0){
					grid[r-1][c-1] = 'c';
					printIt();
					continue;
				}
				else if (m==2 || m==4 || m==6){
					impossible();
					continue;
				}
				else if(m == 8){
					grid[r-1][c-1] = 'c';
					grid[r-2][c-2] = '*';
					grid[r-1][c-2] = '*';
					grid[r-2][c-1] = '*';
					grid[r-3][c-1] = '*';
					grid[r-3][c-2] = '*';
					grid[r-3][c-3] = '*';
					grid[r-2][c-3] = '*';
					grid[r-1][c-3] = '*';
					printIt();
					continue;
				}
				else{
					assert(false);
				}
			}

		}
	}
	return 0;
}