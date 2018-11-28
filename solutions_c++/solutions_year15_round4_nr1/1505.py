#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

const int dx[]={-1, 0, 1, 0};
const int dy[]={0, 1, 0, -1};
int T, row, col;
bool discovery[110][110];
char data[110][110];
pair<int, int> node[110][110][4];

bool isPossible(int x, int y) {
	if(x==-1 || x==row || y==-1 || y==col) return false;
	return true;
}

void makeGraph() {
	for(int i=0 ; i<row ; i++) {
		for(int j=0 ; j<col ; j++) {
			for(int k=0 ; k<4 ; k++) {
				node[i][j][k]=make_pair(-1, -1);
				if(data[i][j]=='.') continue;

				int x=i, y=j;
				while(1) {
					int nextX=x+dx[k], nextY=y+dy[k];
					if(!isPossible(nextX, nextY) || data[nextX][nextY]!='.') {
						node[i][j][k]=make_pair(nextX, nextY);
						break;
					}
					x=nextX; y=nextY;
				}
			}
		}
	}
}

int getDirect(const char& ch) {
	if(ch=='^') return 0;
	else if(ch=='>') return 1;
	else if(ch=='v') return 2;
	else if(ch=='<') return 3;
}

int solution() {
	int ret=0;
	for(int i=0 ; i<row ; i++) {
		for(int j=0 ; j<col ; j++) {
			if(discovery[i][j] || data[i][j]=='.') continue;

			int x=i, y=j, d=getDirect(data[i][j]);
			while(1) {
				discovery[x][y]=true;
				int d=getDirect(data[x][y]);
				int nextX=node[x][y][d].first, nextY=node[x][y][d].second;
				if(!isPossible(nextX, nextY)) {
					bool flag=false;
					for(int k=0 ; k<4 ; k++) {
						if(isPossible(node[x][y][k].first, node[x][y][k].second)) {
							ret++;
							flag=true;
							break;
						}
					}

					if(flag) break;
					else return -1;
				}
				else if(discovery[nextX][nextY])
					break;
				x=nextX; y=nextY;
			}
		}
	}

	return ret;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	scanf("%d", &T);
	for(int t=1 ; t<=T ; t++) {
		memset(discovery, false, sizeof(discovery));
		scanf("%d%d", &row, &col);
		for(int i=0 ; i<row ; i++)
			scanf("%s", data[i]);
		makeGraph();

		printf("Case #%d: ", t);
		int sol=solution();
		if(sol==-1) puts("IMPOSSIBLE");
		else printf("%d\n", sol);
	}
}