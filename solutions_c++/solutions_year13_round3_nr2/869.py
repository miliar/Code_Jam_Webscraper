#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<cstring>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define pii pair<int, int>

#define LIM 10000000
pii fila[LIM];
int ini,fim;

void insere(int x, int y){
	fila[fim++] = mp(x,y);
	if(fim==LIM)
		fim =0;
}

pii tira(){
	pii pt = fila[ini++];
	if(ini==LIM)ini=0;
	return pt;
}

map<pii, int>  d;
map<pii, pii> p;
map<pii, int> f;
void imprime(int x, int  y){
	pii bla = p[mp(x,y)];
	if(bla.first==x && bla.second==y)
		return;
	imprime(bla.first,bla.second);
	int k = f[mp(x,y)];
	if(k==0)
		printf("N");
	else if(k==1)
		printf("E");
	else if(k==2)
		printf("S");
	else
		printf("W");
}

int dy[] = {1,0,-1,0};
int dx[] = {0,1,0,-1}; 
int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		int xf,yf;
		scanf("%d %d",&xf,&yf);
		d.clear();
		f.clear();
		p.clear();
		d[mp(0,0)]=0;
		p[mp(0,0)]=mp(0,0);
		ini=fim=0;
	  insere(0,0);
		bool quebra =0;
		while(ini!=fim){
			pii pt = tira();
			int x = pt.first, y = pt.second;
			int dist = d[mp(x,y)];
			int passo = dist+1;
			for(int k=0;k<4;k++){
				int xx = x+dx[k]*passo, yy = y+dy[k]*passo;
				if(d.find(mp(xx,yy))==d.end()){
					d[mp(xx,yy)] = dist+1;
					p[mp(xx,yy)] = mp(x,y);
					f[mp(xx,yy)] = k;
					if(xx==xf&&yy==yf){quebra=1;break;}
					insere(xx,yy);
				}
			}
			if(quebra)break;
		}
		printf("Case #%d: ",caso);
		imprime(xf,yf);
		printf("\n");
	}
	return 0;
}
