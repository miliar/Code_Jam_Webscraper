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
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #"  << t+1 << ": ";
		int R,C;
		cin >> R >> C;
		vector<string> V(R);
		for(int i =0; i < R; i++) cin >> V[i];
		vector< vector<bool> > ch(R,vector<bool>(C,false));
		bool ok =true;
		for(int i =0; i < R; i++) {
			int x =-1, y =-1;
			for(int j =0; j < C; j++) if(V[i][j] != '.') {
				x =j;
				break;}
			for(int j =0; j < C; j++) if(V[i][j] != '.') y =j;
			if(x == -1) continue;
			if(x != y) {
				if(V[i][x] == '<') ch[i][x] =true;
				if(V[i][y] == '>') ch[i][y] =true;}
			else {
				if(V[i][x] == '<' || V[i][x] == '>') ch[i][x] =true;
				int p =0;
				for(int j =0; j < R; j++) if(V[j][x] != '.') p++;
				if(p == 1) ok =false;}
			}
		for(int i =0; i < C; i++) {
			int x =-1, y =-1;
			for(int j =0; j < R; j++) if(V[j][i] != '.') {
				x =j;
				break;}
			for(int j =0; j < R; j++) if(V[j][i] != '.') y =j;
			if(x == -1) continue;
			if(x != y) {
				if(V[x][i] == '^') ch[x][i] =true;
				if(V[y][i] == 'v') ch[y][i] =true;}
			else {
				if(V[x][i] == '^' || V[x][i] == 'v') ch[x][i] =true;
				int p =0;
				for(int j =0; j < C; j++) if(V[x][j] != '.') p++;
				if(p == 1) ok =false;}
			}
		if(!ok) {cout << "IMPOSSIBLE\n"; continue;}
		int ans =0;
		for(int i =0; i < R; i++) for(int j =0; j < C; j++)
			if(ch[i][j]) ans++;
		cout << ans << "\n";}
	return 0;}

// look at my code
// my code is amazing
