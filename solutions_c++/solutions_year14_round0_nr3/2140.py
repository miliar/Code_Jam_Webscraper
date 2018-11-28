#include<iostream>
#include<cstring>
#include<queue>
using namespace std;
const int mx[]={-1,0,1,-1,1,-1,0,1},
		  my[]={-1,-1,-1,0,0,1,1,1};
int r,c,m;
int startx,starty;
int v[60][60],sv[60][60];
bool possible=false;
inline bool check(int x,int y){
	return x>=0 && x<r && y>=0 && y<c;
}
inline int calc(int x,int y){
	int cnt=0;
	for (int i=0;i<8;i++)
		if (check(x+mx[i],y+my[i]) && (v[x+mx[i]][y+my[i]]==1))
			cnt++;
	return cnt;
}
void bfs(int sx,int sy){
	/*
	cout << "bfs:\n";
	for (int i=0;i<r;i++){
		for (int j=0;j<c;j++)
			if (i==sx && j==sy)
				cout << 'c';
			else if (v[i][j]==1)
				cout << "*";
			else
				cout << ".";
		cout << endl;
	}
	*/
	queue<int> qx,qy;
	qx.push(sx);
	qy.push(sy);
	v[sx][sy]=2;
	int lft=r*c-m;
	while (!qx.empty()){
		int qxh=qx.front(),qyh=qy.front();
		qx.pop();
		qy.pop();
		lft--;
		//cout << " now " << qxh << " " << qyh << endl;
		if (lft==0){
			possible=true;
			break;
		}
		if (calc(qxh,qyh)==0)
			for (int i=0;i<8;i++){
				int tx=qxh+mx[i];
				int ty=qyh+my[i];

				if (check(tx,ty) && v[tx][ty]==0){
					v[tx][ty]=2;
					qx.push(tx);
					qy.push(ty);
				}
			}
	}
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++)
			if (v[i][j]==2)
				v[i][j]=0;
}
void dfs(int prev,int now){
	if (possible) return;
	if (now==m)
		for (int i=0;i<r;i++){
			for (int j=0;j<c;j++){
				if (v[i][j]==0)
					bfs(i,j);
				if (possible){
					startx=i;
					starty=j;
					memcpy(sv,v,sizeof(sv));
					return;
				}
			}
		}
	if (now>=m) return;
	if (r*c-prev-1<m-now) return;
	//cout << "dfs " << prev << " " << now << endl;
	for (int k=prev+1;k<r*c;k++){
		int i=k/c,j=k%c;
		if (v[i][j]==0){
			v[i][j]=1;
			dfs(k,now+1);
			v[i][j]=0;
		}
	}
}
int main(){
	int t;
	cin >> t;
	for (int ti=0;ti<t;ti++){
		possible=false;
		memset(v,0,sizeof(v));
		cin >> r >> c >> m;
		dfs(-1,0);
		cout << "Case #" << ti+1 << ":" << endl;
		if (possible){
			for (int i=0;i<r;i++){
				for (int j=0;j<c;j++)
					if (i==startx && j==starty)
						cout << 'c';
					else if (sv[i][j]==1)
						cout << "*";
					else
						cout << ".";
				cout << endl;
			}
		} else
			cout << "Impossible" << endl;
	}
	return 0;
}
