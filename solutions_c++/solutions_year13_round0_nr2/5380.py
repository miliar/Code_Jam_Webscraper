#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <list>
#include <string>
#include <vector>
#include <algorithm>

#define INF 		2000000000ll
#define FOR(i,a,b)	for(int i = a; i < b; i++)
#define MIN(a,b)	({a < b ? a : b;})
#define MAX(a,b)	({a > b ? a : b;})
#define AB(a)		({a < 0 ? -a : a;})
#define EQ(a,b)		({AB(a - b) <= 1e-10 ? true : false;})
#define CL(a)		memset(a,b,sizeof(a))
#define NOT(a)		a = not a

using namespace std;

int input[100][100];
int M,N;
bool row(int a, int val){
	FOR(i,0,N) {
		if(input[a][i] > val){
			return false;
		}
	}
	return true;
}
bool col(int a, int val){
	FOR(i,0,M) {
		if(input[i][a] > val){
			return false;
		}
	}
	return true;
}
void solve(int num){
	cin >> M >> N;
	FOR(i,0,M) FOR(n,0,N) cin >> input[i][n];
	
	cout << "Case #" << num + 1 << ": ";
	FOR(i,0,M)
	FOR(n,0,N)
	if(not row(i, input[i][n]) and not col(n, input[i][n])) {
		cout << "NO" << endl; return ;
	}
	cout << "YES" << endl;
}
int main(){
	int T;
	cin >> T;
	FOR(i,0,T) solve(i);
	return 0;
}