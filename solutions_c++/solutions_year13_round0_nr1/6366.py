#include<cstdio>
#include<algorithm>

using namespace std;

int T;
char map[6][6];

// F: not determined, X: X wins, O: O wins
char back(int x, int y, int dx, int dy, char s){
	if(map[x][y] == '.') return 'F';
	if(x>=4 || y>=4) return s;
	if(s == 'T') return back(x+dx, y+dy, dx, dy, map[x][y]);
	else if(s != map[x][y] && map[x][y] != 'T') return 'F';
	else return back(x+dx, y+dy, dx, dy, s);
}

int main(void){
	bool nf = false;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		for(int j=0;j<4;j++){
			scanf("%s",&map[j]);
		}
		printf("Case #%d: ",i+1);

		nf = false;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(map[j][k] == '.') nf = true;
			}
		}

		char res;
		res = back(0,0,1,0,map[0][0]);
		res = (res == 'F') ? back(0,0,0,1,map[0][0]) : res;
		res = (res == 'F') ? back(0,0,1,1,map[0][0]) : res;
		res = (res == 'F') ? back(1,0,0,1,map[1][0]) : res;
		res = (res == 'F') ? back(2,0,0,1,map[2][0]) : res;
		res = (res == 'F') ? back(3,0,0,1,map[3][0]) : res;
		res = (res == 'F') ? back(0,1,1,0,map[0][1]) : res;
		res = (res == 'F') ? back(0,2,1,0,map[0][2]) : res;
		res = (res == 'F') ? back(0,3,1,0,map[0][3]) : res;
		res = (res == 'F') ? back(0,3,1,-1,map[0][3]) : res;

		if(res == 'F'){
			if(nf) printf("Game has not completed\n");
			else printf("Draw\n");
		}
		else{
			printf("%c won\n",res);
		}
	}
}