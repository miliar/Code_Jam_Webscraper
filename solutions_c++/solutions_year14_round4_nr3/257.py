#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#define MAX_N 200000
using namespace std;

int H, W, B;
int movx[4]={0,0,-1,1};
int movy[4]={-1,1,0,0};
bool enRango(int i, int j)
{
	return (i>=0 && j>=0 && i<H && j<W);
}

struct Eje{ long long f, m; long long d(){return m-f;}};
typedef map <int, Eje> MIE; MIE red[MAX_N];
int N, F, D;
void iniG(int n, int f, int d){N=n; F=f; D=d; fill(red, red+N, MIE());}
void aEje(int d, int h, int m){
	red[d][h].m=m; red[d][h].f=red[h][d].m=red[h][d].f=0;
}

#define DIF_F(i,j) (red[i][j].d())
#define DIF_FI(i) (i->second.d())
int v[MAX_N];
long long camAu(){
	fill(v, v+N, -1);
	queue<int> c;
	c.push(F);
	while(!(c.empty()) && v[D]==-1){
		int n = c.front(); c.pop();
		for(MIE::iterator i = red[n].begin(); i!=red[n].end(); i++){
			if(v[i->first]==-1 && DIF_FI(i) > 0){
				v[i->first]=n;
				c.push(i->first);
			}
		}
	}
	if(v[D]==-1) return 0;
	int n=D;
	long long f = DIF_F(v[n], n);
	while(n!=F){
		if(f<DIF_F(v[n], n)) f = DIF_F(v[n], n);
		n=v[n];
	}
	n=D;
	while(n!=F){
		red[n][v[n]].f=-(red[v[n]][n].f+=f);
		n=v[n];
	}
	return f;
}

long long flujo(){
	long long tot=0, c;
	do{
		tot+=(c=camAu());
	}while(c>0);
	return tot;
}

int tab[512][512];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++)
	{
		cin >> W >> H >> B;
		memset(tab,0,sizeof(tab));
		iniG(2*H*W+2, 2*H*W, 2*H*W+1);
		
		int x0, y0, x1, y1;
		for(int i=0; i<B; i++)
		{
			cin >> x0 >> y0 >> x1 >> y1;
			
			for(int j=x0; j<=x1; j++)
				for(int k=y0; k<=y1; k++)
				{
					tab[k][j]=1;
				}
		}
		
		for(int i=0; i<W; i++)
		{
			if(tab[0][i]==0)
				aEje(2*H*W, i, 1);
			if(tab[H-1][i]==0)
				aEje(H*W+W*(H-1)+i, 2*H*W+1, 1);
		}
		
		/*for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				cout << tab[i][j] << " ";
			}
			cout << endl;
		}
		cout << "TIro el flujo" << endl;*/
		
		for(int i=0; i<H; i++)
			for(int j=0; j<W; j++)
			{
				aEje(W*i+j, H*W+W*i+j, 1);
				//cout << i << " " << j << endl;
				if(tab[i][j]==0)
				for(int k=0; k<4; k++)
				{
					int newi=i+movy[k], newj=j+movx[k];
					if(enRango(newi, newj) && tab[newi][newj]==0)
					{
						//cout << i << " " << j << " " << newi << " " << newj << endl;
						aEje(H*W+W*i+j, W*newi+newj, 1);
					}
				}
			}
		
		int ans=flujo();
		
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
