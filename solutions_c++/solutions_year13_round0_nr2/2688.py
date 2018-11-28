#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

#define fori(i,n) for(int i=0;i<n;i++) 
#define fori_1(i,n) for(int i=1;i<n-1;i++) 
#define fori1(i,n) for(int i=1;i<=n;i++) 

bool hay_camino(vector< vector<int>  > &v, int p, int x, int y, int n, int m){
	int cont = 1;
	while((x+cont)<(m-1)){
		if(v[y][x+cont]==p)
			cont++;
		else break;
	}
	if(cont+x==(m-1) and v[y][x+cont]==p)
		return true;
	else{
		cont=-1;
		while((x+cont)>0){
			if(v[y][x+cont]==p)
				cont--;
			else break;
		}
		if(cont+x==0 and v[y][x+cont]==p)
			return true;
		else{
			cont=1;
			while((y+cont)<(n-1)){
				if(v[y+cont][x]==p)
					cont++;
				else break;
			}
			if(cont+y==(n-1) and v[y+cont][x]==p)
				return true;
			else{
				cont=-1;
				while((y+cont)>0){
					if(v[y+cont][x]==p)
						cont--;
					else break;
				}
				if(cont+y==0 and v[y+cont][x]==p)
					return true;
				else
					return false;
			}
		}
	}
}


bool recorrer_filas (vector< vector<int>  > &v, int m, int n) {
	bool flag = false;
	for (int j=0;j<m;j++) {
		for (int i=0; i<n; i++) {
			if(i==0 and v[i][j]==1){
				flag=true;
				continue;
			}
			if(flag and v[i][j]==1)
				continue;
			else
				return false;
		}
		flag = false;
	}
	return true;	
}

bool recorrer_columnas (vector< vector<int>  > &v, int m, int n) {
	bool flag = false;
	for (int i=0;i<n;i++) {
		for (int j=0; j<m; j++) {
			if(j==0 and v[i][j]==1){
				flag=true;
				continue;
			}
			if(flag and v[i][j]==1)
				continue;
			else
				return false;
		}
		flag = false;
	}
	return true;
}


bool verificar_fila_columna (vector< vector<int>  > &v, int m, int n, int i, int j) {
	bool fila = true;
	bool columna = true;
	if(v[i][j]!=1)
		return true;
	//verifica una fila
	for (int col=0;col<m;col++) {
		if (v[i][col] != 1) {
			fila = false;
			break;
		}
	}
	//verifica una columna
	for (int row=0;row<n;row++) {
		if (v[row][j] != 1) {
			columna = false;
			break;
		}
	}
	return (fila || columna);
}

int main(int argc, char *argv[]) {
	
	freopen ("B-small-attempt0.in","r",stdin);
	freopen ("B-small-attempt0.out","w",stdout);
	
	int t;
	cin>>t;
	vector< vector<int>  > v(100,vector<int>(100));
	int n,m;
	bool flag = true;
	fori1(i,t){
		cin>>n>>m;
		fori(j,n){
			fori(k,m){
				cin>>v[j][k];
			}
		}
		if(n>2 || m>2){
			fori(j,n){
				fori(k,m){
					if(!verificar_fila_columna(v,m,n,j,k)){
						flag = false;
						break;
					}
				}
				if(!flag)
					break;
			}
		}
		cout<<"Case #"<<i<<": "<<(flag? "YES" : "NO")<<endl;
		flag = true;
	}
	return 0;
}

