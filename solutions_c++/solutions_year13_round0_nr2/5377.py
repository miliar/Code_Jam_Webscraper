//#include <iostream>
#include <fstream>
#include <queue>
#include <utility>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;
#define fo(i,n) for(int i=0,_n=(n); i<_n; i++)
#define range(i,a,b) for(int i=(a),_b=(b); i<_b; i++)

ifstream cin("in.txt"); ofstream cout("out.txt");
int T,R,C;
int grid[101][101], rowmax[101], colmax[101];
int main() {
	cin>>T;
	fo(test,T) {
		cin>>R>>C;
		fo(i,R) rowmax[i] = 0;
		fo(j,C) colmax[j] = 0;
		fo(i,R) fo(j,C) cin>>grid[i][j], rowmax[i] = max(rowmax[i],grid[i][j]), colmax[j] = max(colmax[j],grid[i][j]);
		bool possible = true;
		fo(i,R) fo(j,C) if(grid[i][j] < rowmax[i] && grid[i][j] < colmax[j]) {
			possible = false;
			i = R; j = C;
		}
		cout<<"Case #"<<test+1<<(possible ? ": YES\n" : ": NO\n");
	}
}
