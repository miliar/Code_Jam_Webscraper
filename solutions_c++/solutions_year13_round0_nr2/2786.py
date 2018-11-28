#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

bool search(const vector < vector <int> > map, int r, int c, int row, int col){
	bool f1, f2;
	f1 = f2 = true;
	for(int i=0;i<row;i++){
		if(map[i][c]==2){
			f1 = false;
			break;
		}
	}
	for(int i=0;i<col;i++){
		if(map[r][i]==2){
			f2 = false;
			break;
		}
	}
	return (f1||f2);
}

int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		int row, col;
		cin >> row >> col;
		
		vector < vector <int> > lawn;
		int temp;
		for(int i=0;i<row;i++){
			vector <int> tempvec;
			for(int j=0;j<col;j++){
				cin >> temp;
				tempvec.push_back( temp );
			}
			lawn.push_back( tempvec );
		}

		bool f = true;
		for(int r=0;r<row;r++){
			if(!f)	break;
			for(int c=0;c<col;c++){
				if(lawn[r][c]==1){
					if(!search(lawn, r, c, row, col)){
						f = false;
						break;
					}
				}
			}
		}
		if(f)	printf("Case #%d: YES\n", t);
		else	printf("Case #%d: NO\n", t);
	}
	return 0;
}