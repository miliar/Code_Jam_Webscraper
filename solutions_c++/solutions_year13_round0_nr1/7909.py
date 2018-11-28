#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <iostream>
using namespace std;
#define fr(a,b,c) for(int a=b;a<c;a++)
#define rp(a,b) fr(a,0,b)
#define cl(a,b) memset((a),(b),sizeof(a))
int dx[]={0,0,-1,1,1,1,-1,-1};
int dy[]={1,-1,0,0,1,-1,1,-1};
bool check(int i,int j){ return i>=0&&i<4&&j>=0&&j<4; }
char mat[10][10];
int main(){
	int t;
	scanf("%d",&t);
	fr(cas,1,t+1){
		bool comp=0;
		rp(i,4){
			scanf("%s",mat[i]);
			rp(j,4) comp|=(mat[i][j]=='.');
		}
		printf("Case #%d: ",cas);
		rp(i,4){
			rp(j,4){
				if(mat[i][j]=='.') continue;
				rp(k,8){
					int x=i;
					int y=j;
					bool deu=1;
					rp(l,4){
						deu&=(mat[x][y]==mat[i][j]|mat[x][y]=='T');
						x+=dx[k];
						y+=dy[k];
						if(!check(x,y)&&l+1!=4){
							deu=0;
							break;
						}
					}
					if(deu){
						printf("%c won\n",mat[i][j]);
						goto fini;
					}
				}
			}
		}
		if(comp) printf("Game has not completed\n");
		else printf("Draw\n");
		fini:;
	}
	return 0;
}
