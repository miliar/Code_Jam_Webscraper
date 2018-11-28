#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool check(vector< vector<int> > grid, int x, int y){
	bool valid = true;
	
	for(int i = 0; i < grid[x].size(); i++){
		if(grid[x][i] > grid[x][y]){
			valid = false;
			break;
		}
	}
	if(valid)
		return true;
		
	for(int i = 0; i < grid.size(); i++){
		
		if(grid[i][y] > grid[x][y]){
			
			return false;
		}
	}
	return true;
}

int main(){
	ofstream out("lawn.out");
	ifstream in("lawn.in");
	
	int t, temp;
	in >> t;
	
	for(int i = 0; i < t; i++){
		int n,m;
		in >> n >> m;
		
		vector< vector<int> > grid(n);
		for(int j=0; j<n; j++){
			for(int k=0; k<m; k++){
				in >> temp;
				grid[j].push_back(temp);
			}
		}
		
		bool z = false;
		
		for(int j = 0; j < n; j++){
			for(int k = 0; k < m; k++){
				if(!check(grid,j,k)){
					out << "Case #" << i+1 << ": NO" << endl;
					z = true;
					break;
				}
			}
			if(z)
				break;
		}
		
		if(z)
			continue;
		else
			out << "Case #" << i+1 << ": YES" << endl;
		
	}
	
	return 0;
}

