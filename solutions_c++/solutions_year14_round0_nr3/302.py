#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;

int g[50][50];

void Output(int R, int C, bool tr){
	if(tr) swap(R,C);
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			if(i==0 && j==0) printf("c");
			else{
				int t = tr?g[j][i]:g[i][j];
				printf("%c",t?'.':'*');
			}
		}
		puts("");
	}
}

void Myfill(int r1, int c1, int r2, int c2){
	for(int i = 0; i < r1; i++){
		for(int j = 0; j < c2; j++){
			g[i][j] = 1;
		}
	}
	for(int i = 0; i < r2; i++){
		for(int j = 0; j < c1; j++){
			g[i][j] = 1;
		}
	}
}

void Myfill2(int r1, int c1, int r2, int c2, int m){
	for(int i = r1; i < r2; i++){
		for(int j = c1; j < c2; j++){
			if(m==0) return;
			g[i][j] = 1;
			m--;
		}
	}
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int R,C,M;
		cin>>R>>C>>M;
		memset(g,0,sizeof(g));
		bool tr = false;
		if(R>C){
			swap(R,C);
			tr = true;
		}
		int m = R*C-M;
		printf("Case #%d:\n",Case);
		bool flag = true;
		if(R==1){
			for(int i = 0; i < R; i++){
				for(int j = 0; j < m; j++){
					g[i][j] = 1;
				}
			}
		}else if(R==2){
			if(m%2==1 || m==2) flag = false;
			else{
				for(int i = 0; i < R; i++){
					for(int j = 0; j < m/2; j++){
						g[i][j] = 1;
					}
				}
			}
		}else{
			flag = false;
			for(int i = 2; i <= R; i++){
				for(int j = 2; j <= C; j++){
					for(int i2 = i; i2 <= R; i2++){
						for(int j2 = j; j2 <= C; j2++){
							/*if(i*j2+i2*j-i*j==m){
								flag = true;
								Myfill(i,j,i2,j2);
								i = j = i2 = j2 = INF;
							}else */if(i*j2+i2*j-i*j<=m && m <= i2*j2){
								flag = true;
								Myfill(i,j,i2,j2);
								Myfill2(i,j,i2,j2,m-(i*j2+i2*j-i*j));
								i = j = i2 = j2 = INF;
							}
						}
					}
				}
			}
		}
		if(m==1) flag = true;
		if(flag)Output(R,C,tr);
		else puts("Impossible");
	}
	return 0;
}

