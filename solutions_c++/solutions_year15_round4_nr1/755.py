#include <cstdio>
#include <iostream>
using namespace std;

char s[200][200];
int inD[200][200];
int eD[200][200];
int GI[200*200],GJ[200*200],nG;

int nxt[200][200][4];

const int di[] = {-1,0,1,0};
const int dj[] = {0,1,0,-1};

int main() {
	int T,ics=0;
	scanf("%d",&T);
	while(T--) {
		int R,C;
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;++i) {
			scanf("%s",s[i]);
		}
		for(int i=0;i<R;++i) for(int j=0;j<C;++j) {
			inD[i][j] = 0;
			eD[i][j] = 0;
		}
		nG = 0;
		for(int i=0;i<R;++i) for(int j=0;j<C;++j) if(s[i][j]!='.') {
			for(int d=0;d<4;++d) {
				int pi = i + di[d];
				int pj = j + dj[d];
				
				while( pi >= 0 && pi < R && pj >= 0 && pj < C && s[pi][pj] == '.' ) {
					pi = pi + di[d];
					pj = pj + dj[d];
				}
				
				if( pi >= 0 && pi < R && pj >= 0 && pj < C ) {
					nxt[i][j][d] = pi * C + pj;
					eD[pi][pj]++;
				}
				else {
					nxt[i][j][d] = -1;
				}
			}
			
			int pt = 0;
			switch( s[i][j] ) {
				case '^': pt = 0; break;
				case '>': pt = 1; break;
				case 'v': pt = 2; break;
				case '<': pt = 3; break;
				default: break;
			}
			if( nxt[i][j][pt] == -1 ) {
				GI[nG] = i;
				GJ[nG] = j;
				++nG;
			}
			else {
				int pi = nxt[i][j][pt] / C;
				int pj = nxt[i][j][pt] % C;
				inD[pi][pj]++;
			}
		}
		bool fail = false;
		int ans = nG;
		for(int i=0;i<nG;++i) {
			if( inD[GI[i]][GJ[i]] == 0 && eD[GI[i]][GJ[i]] == 0 ) {
				fail = true;
				break;
			}
			if( inD[GI[i]][GJ[i]] == 0 && eD[GI[i]][GJ[i]] != 0 )
				++ans;
		}
		
		if(fail)
			printf("Case #%d: IMPOSSIBLE\n",++ics);
		else
			printf("Case #%d: %d\n",++ics,nG);
	}
	return 0;
}