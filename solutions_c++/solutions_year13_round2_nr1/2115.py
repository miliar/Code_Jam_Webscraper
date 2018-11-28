#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<vector>
#include<deque>
#include<utility>
#include<map>
#include<math.h>
#include<memory.h>

#define li long long
#define fs first
#define sc second
#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define mp make_pair

using namespace std;

long long INF = 1e9 + 7;

int a[105], n;

int dfs(int X, int i){
	if(i == n) return 0;
	if(X > a[i]) return dfs(X + a[i], i + 1);
	int X1 = X;
	int j;
	if(X != 1){
		for(j = 1; j <= 20; j++){
			X1 = 2 * X1 - 1;
			if(X1 > a[i]) break;
		}
	}
	if(X != 1){
		return min(j + dfs(X1 + a[i], i + 1), 1 + dfs(X, i + 1));
	}
	else
		return 1 + dfs(X, i + 1);
}

int main(){
	freopen("A-small-attempt0 (1).in", "r", stdin);
	freopen("OUTPUT.txt", "w", stdout);
	int T;
	cin >> T;
	for(int z = 0; z < T; z++){
		int A;
		cin >> A >> n;
		int i;
		for(i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a + n);
		cout << "Case #" << z + 1 << ": " << dfs(A, 0) << "\n";
	}
	return 0;
}