#include<cstdio>
#include<cmath>
#include<iostream>
#include<string>

using namespace std;

#define MAXR 128

char grid[MAXR][MAXR];
int di[4] = {1,0,-1,0};
int dj[4] = {0,1,0,-1};

int main(){
	int T;
	cin >> T;
	for(int k=0; k<T; k++){
		int R,C;
		cin >> R >> C;
		int impossible=0;
		int res=0;

		for(int i=0; i<R; i++)for(int j=0; j<C; j++)
			cin >> grid[i][j];
		
		for(int i=0; i<R; i++)for(int j=0; j<C; j++){
			if(grid[i][j]=='.')continue;
			int dir;
			if(grid[i][j]=='v')
				dir=0;
			else if(grid[i][j]=='>')
				dir=1;
			else if(grid[i][j]=='^')
				dir=2;
			else dir=3;

			int bad[4];

			for(int d=0; d<4; d++){
				int r=i, c=j; 
				bad[d]=0;
				while(1){
					r+=di[d];
					c+=dj[d];
					if( r<0 || r>=R || c<0 || c>=C ){
						bad[d]=1; 
						break;
					}
					if( grid[r][c]!='.' )
						break;
				}
			}
			if(bad[dir])
				res++;
			if(bad[0] && bad[1] && bad[2] && bad[3]){
				impossible=1;
				break;
			}
		}
		
		cout << "Case #" << (k+1) << ": ";
		if(impossible)
			cout << "IMPOSSIBLE\n";
		else	
			cout << res << "\n";
	}
}
