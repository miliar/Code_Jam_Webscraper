#include<iostream>
#include<vector>
using namespace std;

bool* findLengts(int **f,int n, int m){
	int i,j;
	bool *ls = new bool[100];
	for(i=0;i<100;i++)
		ls[i] = false;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
			ls[f[i][j]-1] = true;
	return ls;
}

bool hasInOut(int **f, int n, int m, int x,int y){
	int i,v = f[x][y];
	bool ver=false,hor=false;
	for(i=0;i<n;i++){
		if(f[i][y] != v){
			ver = true;
			break;
		}
	}
	for(i=0;i<m;i++){
		if(f[x][i] != v){
			hor = true;
			break;
		}
	}	
	if(ver && hor)
		return false;
	else
		return true;
}

int popMinLen(bool *ls){
	int i;
	for(i=0;i<100;i++)
		if(ls[i]){
			ls[i] = false;
			return i+1;
		}
	return -1;
}

void previousStep(int **f, int n, int m,int v){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			if(f[i][j]<v)
				f[i][j] = v;
		}
	}
}

string canBeDone(int **f, int n, int m, bool *ls){
	int x,i,j;
	x = popMinLen(ls);
	if(x == -1)
		return "YES";
	previousStep(f,n,m,x);
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
			if(f[i][j] == x && !hasInOut(f,n,m,i,j))
				return "NO";
	return canBeDone(f,n,m,ls);
}

int main(){
	int c,i,j,k,n,m,**f;
	bool *b;
	cin>>c;
	for(i=0;i<c;i++){
		cin>>n>>m;
		f = new int*[n];
		for(j=0;j<n;j++)
			f[j] = new int[m];

		for(j=0;j<n;j++){
			for(k=0;k<m;k++){
				cin>>f[j][k];
			}
		}
		b = findLengts(f,n,m);
		cout<<"Case #"<<i+1<<": "<<canBeDone(f,n,m,b)<<endl;
		delete f;
	}


	return 0;
}