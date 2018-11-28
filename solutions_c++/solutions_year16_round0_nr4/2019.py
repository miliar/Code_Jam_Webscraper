#include <bits/stdc++.h>
// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
#define dibs reserve
#define OVER9000 1234567890
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-8
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
#define dbl long double
#define pi 3.14159265358979323846
using namespace std;
// mylittledoge

#ifdef DONLINE_JUDGE
	// palindromic tree is better than splay tree!
	#define lld I64d
#endif

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ":";
		int K,C,S;
		cin >> K >> C >> S;
		if(S*C < K) {cout << " IMPOSSIBLE\n"; continue;}
		set<long long> ans;
		int a =0;
		for(int i =0; i < (K+C-1)/C; i++) {
			long long x =0;
			for(int j =0; j < C; j++) {
				x =x*K+a;
				a =(a+1)%K;}
			ans.insert(x+1);}
		ALL_THE(ans,it) cout << " " << *it;
		cout << "\n";}
	return 0;}

// look at my code
// my code is amazing
