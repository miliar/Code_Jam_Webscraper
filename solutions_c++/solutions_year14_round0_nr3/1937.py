#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#define MAX 100
using namespace std;
int rx[8] = {-1,-1,-1,0,1,1,1,0};
int ry[8] = {-1,0,1,1,1,0,-1,-1};

int r,c;
int Mp[MAX][MAX];

void show_matrix(int ro,int co){
	for(int i = 0;i < ro;i++){
		for(int j = 0;j < co;j++){
			if(i == ro - 1 && j == co - 1) printf("c");
			else if(Mp[i][j] == 0) printf("*");
			else printf(".");
		}
		printf("\n");
	} 

}
bool solved;

vector < pair <int,int> > _copy(vector < pair < int,int > > V){
	vector < pair<int,int> > A;
	for(int i = 0;i < V.size();i++) A.push_back(make_pair(V[i].first,V[i].second));
	return A;
}

void _solve(int minas,vector < pair < int,int > > V,priority_queue < pair < int,pair < int,int > > > Q){
	if(solved) return;
	if(minas < 0) return;
	if(minas == 0){
		solved = true;
		show_matrix(r,c);
		return;
	}
	int minimum = 0;
	if(!Q.empty()) minimum = Q.top().first;
	while(!Q.empty() && !solved){
		int mines = minas;
		int x = Q.top().second.first;
		int y = Q.top().second.second;
		Q.pop();
		vector < pair < int,int > > V1 = _copy(V);
		vector < pair < int,int > > S;
		for(int i = 0;i < 8;i++){
			int xx = x + rx[i];
			int yy = y + ry[i];
			if(xx < 0 || yy < 0 || xx >= r || yy >= c) continue;
			if(Mp[xx][yy] != 0) continue;
			V1.push_back(make_pair(xx,yy)); 
			S.push_back(make_pair(xx,yy));
			Mp[xx][yy] = 1;
			mines--;
		}
		priority_queue < pair < int,pair < int,int > > > Q1;
		for(int k = 0;k < V1.size();k++){
			int cont = 0;
			for(int i = 0;i < 8;i++){
				int xx = V1[k].first + rx[i];
				int yy = V1[k].second + ry[i];
				if(xx < 0 || yy < 0 || xx >= r || yy >= c) continue;
				if(Mp[xx][yy]) continue;
				cont++;
			}
			if(cont == 0) continue;
			Q1.push(make_pair(-cont,make_pair(V1[k].first,V1[k].second)));
				
		}
		_solve(mines,V1,Q1);
		
		for(int i = 0;i < S.size();i++) Mp[S[i].first][S[i].second] = 0;
	}	

}

int main(){
	int m;
	int t; int  caso = 1;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d %d",&r,&c,&m);
		memset(Mp,0,sizeof Mp);
		printf("Case #%d:\n",caso++);
		int mines = r*c - m;
		//printf("put %d mines\n",mines);
		/*priority_queue < pair < int,pair < int,int > > > Q;
		Q.push(make_pair(0,make_pair(r-1,c-1))); mines--;
		vector < pair < int,int > > V;
		while(mines > 0){
			int x = Q.top().second.first;
			int y = Q.top().second.second;
			//printf("sacando %d %d (%d)\n",x,y,Q.top().first);
			Q.pop();
			Mp[x][y] = 1; V.push_back(make_pair(x,y));
			
			for(int i = 0;i < 8;i++){
				int xx = x + rx[i];
				int yy = y + ry[i];
				if(xx < 0 || yy < 0 || xx >= r || yy >= c) continue;
				if(Mp[xx][yy] != 0) continue;
				V.push_back(make_pair(xx,yy)); Mp[xx][yy] = 1;
				mines--;
			}
			Q = priority_queue < pair < int, pair < int,int > > >();
			for(int k = 0;k < V.size();k++){
				int cont = 0;
				for(int i = 0;i < 8;i++){
					int xx = V[k].first + rx[i];
					int yy = V[k].second + ry[i];
					if(xx < 0 || yy < 0 || xx >= r || yy >= c) continue;
					if(Mp[xx][yy]) continue;
					cont++;
				}
				if(cont == 0) continue;
				Q.push(make_pair(-cont,make_pair(V[k].first,V[k].second)));
				
			}
			show_matrix(r,c);
			printf("=======================\n");
		}
		Mp[r-1][c-1] = 1;*/
		solved = false;
		vector < pair < int,int > > V;
		priority_queue < pair < int,pair < int,int > > > Q;
		V.push_back(make_pair(r - 1,c - 1));
		Q.push(make_pair(0,make_pair(r-1,c-1)));
		Mp[r-1][c-1] = 1;
		_solve(mines-1,V,Q);
		if(!solved) printf("Impossible\n");
		
	}
	return 0;
}
