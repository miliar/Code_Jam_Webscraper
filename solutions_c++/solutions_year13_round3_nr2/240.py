#include <algorithm>
#include <cstdio>
#include <deque>
using namespace std;

const int move[4][2]={ {1, 0}, {0, 1}, {-1, 0}, {0, -1} };
const char pi[4]={ 'E', 'N', 'W', 'S' };

#define mp(x,y) make_pair((x), (y))

int T;
int X, Y;
pair<int,int> odkud[1005][1005];
int tahy[1005][1005];
char pism[1005][1005];
deque<pair<int,int> > fronta;
deque<char> cesta;

int main()
{
	scanf("%d", &T);

		for(int i=0; i<1005; i++) for(int j=0; j<1005; j++) tahy[i][j]=-1;
		fronta.push_back(mp(500, 500));
		tahy[500][500]=0;
		while(!fronta.empty()) {
			pair<int,int> akt=fronta.front();
			fronta.pop_front();
			int x=akt.first, y=akt.second;
			for(int d=0; d<4; d++) {
				int nx=x+move[d][0]*(tahy[x][y]+1);
				int ny=y+move[d][1]*(tahy[x][y]+1);
				if(!(nx>=0 && nx<=1000 && ny>=0 && ny<=1000)) continue;
				if(tahy[nx][ny]==-1) {
					tahy[nx][ny]=1+tahy[x][y];
					odkud[nx][ny]=mp(x, y);
					pism[nx][ny]=pi[d];
					fronta.push_back(mp(nx, ny));
				}
			}
		}
	
	for(int q=1; q<=T; q++) {
		scanf("%d%d", &X, &Y);
		X+=500;
		Y+=500;
		cesta.clear();
		while(!(X==500 && Y==500)) {
			cesta.push_back(pism[X][Y]);
			pair<int,int> nove=odkud[X][Y];
			X=nove.first;
			Y=nove.second;
		}
		printf("Case #%d: ", q);
		for(int i=cesta.size()-1; i>=0; i--) printf("%c", cesta[i]);
		printf("\n");
	}

	return 0;
}
