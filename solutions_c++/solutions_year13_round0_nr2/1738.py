#include<iostream>
#include<fstream>

using namespace std;

int lawn[200][200];

int tallest_in_row_or_col(int val, int row, int col, int tot_row, int tot_col) {
	int tallest_in_row=1,tallest_in_col=1;
	for(int i=0;i<tot_col;i++) if(lawn[row][i]>val) tallest_in_row=0;
	for(int i=0;i<tot_row;i++) if(lawn[i][col]>val) tallest_in_col=0;
	if(tallest_in_row || tallest_in_col) return 1;
	else return 0;
}

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	int t,n,m,possible;
	fin>>t;
	for(int count=1;count<=t;count++) {
		fin>>n>>m;
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				fin>>lawn[i][j];
			}
		}
		
		possible=1;
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if(!tallest_in_row_or_col(lawn[i][j],i,j,n,m)) {
					possible=0;
					break;
				}
			}
			if(!possible) break;
		}
		
		if(possible)
			fout<<"Case #"<<count<<": "<<"YES\n";
		else
			fout<<"Case #"<<count<<": "<<"NO\n";
	}
}
