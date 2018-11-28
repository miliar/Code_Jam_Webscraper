#include <bits/stdc++.h>

#define For(i,a,b) for (int i = (a); i <= (b); i++)
#define Ford(i,a,b) for (int i = (a); i >= (b); i--)
#define Rep(i,a) for (int i = 0; i < (a); i++)
#define Repd(i,a) for (int i = (int)(a) - 1; i >=0; i--)
#define PI (acos(0.0) * 2)
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PII pair<int, int>
#define PIII pair<PII, int>
#define VI vector<int>
#define sz(a) ((int)a.size())
#define oo 1000000000
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(a,u,v) {cout << #a << " = "; For(_,u,v) cout << a[_] << ' '; cout << endl;}
typedef long long LL;
using namespace std;

int ntest;
int r,c;
string s[200];
bool check(int x, int y){
	int co = 0;
	for(int i=0; i<r; i++){
		if(s[i][y]!='.') co++;
	}
	for(int i=0; i<c; i++){
		if(s[x][i]!='.') co++;
	}
//	cout << s[0]<< endl;
//	cout << co << endl;
	return co<3;
}

int dfs(int x, int y){
	if(s[x][y] == '<'){
		for(int i=0; i<y; i++){
			if(s[x][i]!= '.') return 0;
		}
		return 1;
	}
	if(s[x][y] == '>'){
		for(int i=y+1; i<c; i++){
			if(s[x][i]!= '.') return 0;
		}
		return 1;
	}
	if(s[x][y] == '^'){
		for(int i=0; i<x; i++){
			if(s[i][y]!= '.') return 0;
		}
		return 1;
	}
	if(s[x][y] == 'v'){
		for(int i=x+1; i<r; i++){
			if(s[i][y]!= '.') return 0;
		}
		return 1;
	}
}

void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%d %d\n",&r,&c);
	for(int i=0; i<r; i++){
		getline(cin,s[i]);
	}
	int res=0;
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if(s[i][j]!='.'){
				if(check(i,j)) { cout << "IMPOSSIBLE" << endl; return;}
				res += dfs(i,j);
			}
		}
	}
	cout << res << endl;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
