#include<cstdio>
#include<algorithm>

using namespace std;
const int MAX = 8;

char m[MAX][MAX];
int casos, nx, no, nt;
bool draw;

int main(){
	int a, b, res;
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
		res = 0;
		draw = true;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf(" %c", &m[i][j]);
		for(int k=0;k<2;k++){
			for(int i=0;i<4;i++){
				nx = no = nt = 0;
				for(int j=0;j<4;j++){
					a = i;
					b = j;
					if(k == 1) swap(a, b);
					if(m[a][b] == 'X') nx++;
					if(m[a][b] == 'O') no++;
					if(m[a][b] == 'T') nt++;
				}
				if(nx+nt == 4) res = 1;
				if(no+nt == 4) res = 2;
				if(nx+no+nt < 4) draw = false;
			}
		}
		for(int k=0;k<2;k++){
			nx = no = nt = 0;
			for(int i=0;i<4;i++){
				a = b = i;
				if(k == 1) b = 3-i;
				if(m[a][b] == 'X') nx++;
				if(m[a][b] == 'O') no++;
				if(m[a][b] == 'T') nt++;
			}
			if(nx+nt == 4) res = 1;
			if(no+nt == 4) res = 2;
			if(nx+no+nt < 4) draw = false;
		}
		
		printf("Case #%d: ", inst);
		if(res == 0 && !draw) printf("Game has not completed\n");
		if(res == 0 && draw) printf("Draw\n");
		if(res == 1) printf("X won\n");
		if(res == 2) printf("O won\n");
	}
}
