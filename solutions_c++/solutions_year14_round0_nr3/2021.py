#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define mod 1000000007


#define N 8 
string I = "Impossible";
int n, m, b;
int Vx[] = {-1, 0, 1, 0, -1, -1, 1, 1};
int Vy[] = {0, 1, 0, -1, 1, -1, 1, -1};
int ja[N][N];
char M[N][N];
int num[N][N];

bool in (int x, int y){
	return x >= 0 && x < n && y >= 0 && y < m;
}


void dfs (int x, int y){
	f (k, 0, 8){
		int xx = x+Vx[k], yy = y+Vy[k];
		if (in(xx, yy)) {
			if (num[xx][yy] == 0 && !ja[xx][yy]){
				ja[xx][yy] = 1;
				dfs (xx, yy);
			}
			ja[xx][yy] = 1;
		}
	}
}

pii possivel (){
	clr (num, 0);
	f (i, 0, n) f (j, 0, m){
		f (k, 0, 8){
			int x = i+Vx[k], y = j+Vy[k];
			if(in(x,y) && M[x][y] == '*') num[i][j]++;
		}
	}
	pii ret = mp (-1,-1);
	f (i, 0, n) f (j, 0, m) if (num[i][j] == 0 && M[i][j] != '*') ret = mp(i,j);
	if (ret.fst == -1) return ret;
	clr (ja, 0);
	ja[ret.fst][ret.snd] = 1;
	dfs (ret.fst, ret.snd);
	f (i, 0, n) f (j, 0, m) if (M[i][j] != '*' && !ja[i][j]) return mp (-1,-1);
	return ret;
}

bool ok = 0;

void print (pii p){
	f (i, 0, n){
		f (j, 0, m){
			if (i == p.fst && j == p.snd) printf("c");
			else printf("%c", M[i][j]);
		}
		printf("\n");
	}
}


void go (int l, int falta){
	if (ok) return;
	if (falta < 0) return;
	if (l == n){
		if (falta != 0) return;
		pii p = possivel();
		if (p.fst == -1) return;
		print(p); ok = 1;
		return;
	}
	f (i, 0, m+1){
		f (j, 0, i) M[l][j] = '*';
		go (l+1, falta-i);
	}
	f (i, 0, m+1) M[l][i] = '.';
}




int main (){
	int tt = 1;
	int t; cin >> t;
	while (t--){
		cin >> n >> m >> b;
		printf("Case #%d:\n", tt++);
		int l = n*m-b;
		if (n == 1 || m == 1){
			if (n == 1){
				printf("c");
				f (i, 0, l-1) printf(".");
				f (i, 0, b) printf("*"); printf("\n");
			}
			else{
				printf("c\n");
				f (i, 0, l-1) printf(".\n");
				f (i, 0, b) printf("*\n"); 
			}
			continue;
		}


		if (l == 1){
			f (i, 0, n){
				f (j, 0, m){
					if (i+j == 0) printf("c");
					else printf("*");
				}
				printf("\n");
			}
			continue;
		}

		ok = 0;
		f (i, 0, n) f (j, 0, m) M[i][j] = '.';
		go(0,b);
		if (ok == 0) cout << I << endl;



		

	}
	return 0;
}

