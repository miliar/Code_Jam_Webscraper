#include <iostream>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define X first
#define Y second

using namespace std;

string a[1000];
int n, m;
int opt;
int ways;

void go(vector<string> &A, int p, int cost){
	if (p == m){
		if (cost > opt){
			opt = cost;
			ways = 0;
		}
		if (cost == opt) ways++;
		return ;
	}
	for (int i = 0; i < n; i++){
		int r = a[p].size();
		for (int j = 0; j < min(A[i].size(), a[p].size()); j++){
			if (A[i][j] != a[p][j]) break;
			r--;
		}
		string T = A[i];
		A[i] = a[p];

		if (T == "") r++;

		go(A, p + 1, cost + r);

		A[i] = T;
	}
}

int main(){
	freopen("inputd2.in","r",stdin);
	freopen("outputd2.out","w",stdout);
	int T;
	cin >> T;
	for (int TT = 1; TT <= T; TT++){
		printf("Case #%d: ", TT);
				
		cin >> m >> n;
		for (int i = 0; i < m; i++) cin >> a[i];

		sort(a, a + m);

		vector<string> A(n);
		for (int i = 0; i < n; i++) A[i] = "";
			
		opt = 0;
		ways = 0;
		go(A, 0, 0);
		cout << opt << " " << ways << endl;
	}
    return 0;
}
