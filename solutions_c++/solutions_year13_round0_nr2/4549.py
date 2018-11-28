/*
ID: qazzaq71
PROG: packrec
LANG: C++
*/
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long ll;

int n, m;
int a[102][102];
int u[102][102];

bool Ej(){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(u[i][j] == 0){
				return false;
			}
		}
	}
	return true;
}
bool keYiLuYiFaR(int pos){
	// yi jing lu wan le
	int w = -1;
	for(int i = 0; i < m; i++){
		if(u[pos][i] == 0){
			w = i;
			break;
		}
	}
	if(w == -1){
		return false;
	}
	for(int i = 0; i < m; i++){
		if(u[pos][i] == 0){
			if(a[pos][i] != a[pos][w]){
				return false;
			}
		} else {
			if(a[pos][i] > a[pos][w]){
				return false;
			}
		}
	}
	return true;
}
void zhenDeLuYiFaR(int pos){
	for(int i = 0; i < m; i++){
		u[pos][i] = 1;
	}
}
bool keYiLuYiFaC(int pos){
	// yi jing lu wan le
	int w = -1;
	for(int i = 0; i < n; i++){
		if(u[i][pos] == 0){
			w = i;
			break;
		}
	}
	if(w == -1){
		return false;
	}
	for(int i = 0; i < n; i++){
		if(u[i][pos] == 0){
			if(a[i][pos] != a[w][pos]){
				return false;
			}
		} else {
			if(a[i][pos] > a[w][pos]){
				return false;
			}
		}
	}
	return true;
}
void zhenDeLuYiFaC(int pos){
	for(int i = 0; i < n; i++){
		u[i][pos] = 1;
	}
}
bool luYiFa(){
	for(int i = 0; i < n; i++){
		if(keYiLuYiFaR(i)){
			zhenDeLuYiFaR(i);
			return true;
		}
	}
	for(int i = 0; i < m; i++){
		if(keYiLuYiFaC(i)){
			zhenDeLuYiFaC(i);
			return true;
		}
	}
	return false;
}
void printA(int arr[102][102]){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}
int main(){
#ifdef DEBUG
	FILE * ptrFILE=freopen("b.in","r",stdin);
	assert(ptrFILE!=NULL);	
	ptrFILE=freopen("b.out","w",stdout);
	assert(ptrFILE!=NULL);	
#endif
	int t;
	scanf("%d", &t);
	for(int cs = 1; cs <= t; cs++){
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				scanf("%d", &a[i][j]);
			}
		}
//		printA(a);
		memset(u, 0, sizeof(u));
		while(!Ej()){
			if(!luYiFa()){
				break;
			}
		}
		if(Ej()){
			printf("Case #%d: YES\n", cs);
		} else {
			printf("Case #%d: NO\n", cs);
		}
	}
    return 0;
}
