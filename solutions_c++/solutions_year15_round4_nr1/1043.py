#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int dx[4]={0,1,0,-1};
int dy[4]={-1,0,1,0};

int main() {

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin>>T;

	for(int testcase=1 ; testcase<=T ; testcase++) {
		int R,C;
		cin>>R>>C;

		vector<string> grid(R);
		for(int i=0 ; i<R ; i++) cin>>grid[i];

		bool chk_pos = true;
		for(int i=0 ; i<R ; i++) {
			for(int j=0 ; j<C ; j++) {
				if(grid[i][j] != '.') {
					int numi=0, numj=0;

					for(int s=0 ; s<R ; s++)
						if(grid[s][j]!='.') numi++;
					for(int s=0 ; s<C ; s++)
						if(grid[i][s]!='.') numj++;

					if(numi<=1 && numj<=1) chk_pos=false;
				}
			}
		}

		int ans=0;
		if(chk_pos) {
			vector<vector<bool>> pos(R,vector<bool>(C,false));
			
			for(int i=0 ; i<R ; i++) {
				for(int j=0 ; j<C ; j++) {
					if(grid[i][j]!='.' && !pos[i][j]) {
						int s=i, t=j;
						int direction;

						if(grid[i][j]=='^') direction=0;
						else if(grid[i][j]=='>') direction=1;
						else if(grid[i][j]=='v') direction=2;
						else if(grid[i][j]=='<') direction=3;

						while(0<=s && s<R && 0<=t && t<C && !pos[s][t]) {
							if(grid[s][t]=='.') {
								s+=dy[direction];
								t+=dx[direction];
								continue;
							}
							else {
								pos[s][t]=true;

								if(grid[s][t]=='^') direction=0;
								else if(grid[s][t]=='>') direction=1;
								else if(grid[s][t]=='v') direction=2;
								else if(grid[s][t]=='<') direction=3;

								s+=dy[direction];
								t+=dx[direction];
							}
						}

						if(s<0 || s>=R || t<0 || t>=C) ans++;
					}
				}
			}

		}

		cout<<"Case #"<<testcase<<": ";
		if(chk_pos) cout<<ans<<"\n";
		else cout<<"IMPOSSIBLE\n";
	}

	return 0;
}