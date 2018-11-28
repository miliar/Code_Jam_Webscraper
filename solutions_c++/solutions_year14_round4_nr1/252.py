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
#define dibs reserve
#define OVER9000 1234567890LL
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-10
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
using namespace std;
// mylittledoge

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	srand(time(0));
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ":";
		int N,X;
		cin >> N >> X;
		multiset<int> S;
		for(int i =0; i < N; i++) {
			int a;
			cin >> a;
			S.insert(a);}
		int ans =0;
		while(!S.empty()) {
			int x =*S.rbegin();
			auto it =S.upper_bound(X-x);
			if(it == S.end()) it--;
			if(it == S.begin()) {
				S.erase(--S.end());
				ans++;
				continue;}
			it--;
			S.erase(it);
			S.erase(--S.end());
			ans++;}
		cout << " " << ans << "\n";}
	return 0;}

// look at my code
// my code is amazing
