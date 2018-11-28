#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

int tab[10][10];
int cur[10][10];
int mult[10][10];
int n, M;

bool valid() {
	/*
  printf("CHECANDO\n");
	for(int i=0;i<n;i++) { 
		for(int j=0;j<n;j++)
			cout << tab[i][j];
		cout << endl;
	}	
  */

	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			cur[i][j]=tab[i][j];
	int s = 0;
	int roda = n-1;
	while(roda--) {
	  s += cur[0][n-1];
		for(int i=0;i<n;i++)
		  for(int j=0;j<n;j++) {
				mult[i][j] = 0;
				for(int k=0;k<n;k++)
					mult[i][j] += cur[i][k]*tab[k][j];
			}
	  for(int i=0;i<n;i++)
		  for(int j=0;j<n;j++)
			  cur[i][j]=mult[i][j];
	}
	return s == M; 
}

bool tenta(int x, int y) {
	// printf("TENTA %d %d\n",x,y);
	if(x>=n) {
		return valid();
	}
	if(y>=n) {
		return tenta(x+1,x+2);
	}
	tab[x][y]=0;
	if(tenta(x,y+1)) return true;
	tab[x][y]=1;
  if(tenta(x,y+1)) return true;
	return false;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		cin >> n >> M;
		memset(tab,0,sizeof(tab));
		if(tenta(0,1)) {
			printf("Case #%d: POSSIBLE\n", caso);
			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++) 
					cout << tab[i][j];
				cout << endl;
			}	
		} else {
			printf("Case #%d: IMPOSSIBLE\n", caso);
		}
	}
	return 0;
}
