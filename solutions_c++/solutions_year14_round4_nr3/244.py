// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#define dibs reserve
#define OVER9000 1234567890LL
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-10
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
using namespace std;
// mylittledoge

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	srand(time(0));
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ":";
		int W,H,B;
		cin >> W >> H >> B;
		vector< vector<bool> > M(H,vector<bool>(W,true));
		for(int k =0; k < B; k++) {
			int x0,y0,x1,y1;
			cin >> x0 >> y0 >> x1 >> y1;
			for(int i =y0; i <= y1; i++) for(int j =x0; j <= x1; j++)
				M[i][j] =false;
			}
		if(B == 0) {cout << " " << W << "\n"; continue;}

		vector< vector<int> > G(2*W*H+2);
		vector< map<int,int> > F(2*W*H+2);
		int dx[] ={0,0,1,-1};
		int dy[] ={1,-1,0,0};
		for(int i =0; i < H; i++) for(int j =0; j < W; j++) if(M[i][j])
			for(int k =0; k < 4; k++) if(min(i+dx[k],j+dy[k]) >= 0 && i+dx[k] < H && j+dy[k] < W)
				if(M[i+dx[k]][j+dy[k]]) {
					G[2*(i*W+j)+1].push_back(2*((i+dx[k])*W+j+dy[k]));
					F[2*(i*W+j)+1][2*((i+dx[k])*W+j+dy[k])] =1;
					G[2*((i+dx[k])*W+j+dy[k])].push_back(2*(i*W+j)+1);
					F[2*((i+dx[k])*W+j+dy[k])][2*(i*W+j)+1] =0;}
		for(int i =0; i < W*H; i++) if(M[i/W][i%W]) {
			G[2*i].push_back(2*i+1);
			F[2*i][2*i+1] =1;
			G[2*i+1].push_back(2*i);
			F[2*i+1][2*i] =0;}
		for(int i =0; i < W; i++) {
			G[2*W*H].push_back(2*i);
			F[2*W*H][2*i] =1;
			G[2*i+1].push_back(2*W*H);
			F[2*i+1][2*W*H] =1;
			G[2*W*H+1].push_back((W*H-1-i)*2);
			F[2*W*H+1][(W*H-1-i)*2] =1;
			G[(W*H-1-i)*2+1].push_back(2*W*H+1);
			F[(W*H-1-i)*2+1][2*W*H+1] =1;
			G[2*i].push_back(2*W*H);
			F[2*i][2*W*H] =0;
			G[2*W*H].push_back(2*i+1);
			F[2*W*H][2*i+1] =0;
			G[(W*H-1-i)*2].push_back(2*W*H+1);
			F[(W*H-1-i)*2][2*W*H+1] =0;
			G[2*W*H+1].push_back((W*H-1-i)*2+1);
			F[2*W*H+1][(W*H-1-i)*2+1] =0;}

		int f =0;
		while(true) {
			vector<int> ako(2*W*H+2,-1);
			queue<int> q;
			q.push(2*W*H);
			ako[2*W*H] =2*W*H;
			while(!q.empty()) {
				int a =q.front();
				if(a == 2*W*H+1) break;
				for(uint i =0; i < G[a].size(); i++) if(ako[G[a][i]] == -1 && F[a][G[a][i]] == 1) {
					ako[G[a][i]] =a;
					q.push(G[a][i]);}
				q.pop();}

			if(ako[2*W*H+1] == -1) break;
			f++;
			int a =2*W*H+1;
			while(a != 2*W*H) {
				auto it =F[ako[a]].find(a), jt =F[a].find(ako[a]);
				it->ss =0, jt->ss =1;
				a =ako[a];}
			}
		cout << " " << f << "\n";}
	return 0;}

// look at my code
// my code is amazing
