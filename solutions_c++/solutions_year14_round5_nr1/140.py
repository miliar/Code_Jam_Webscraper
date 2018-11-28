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
		cout << "Case #" << t+1 << ": ";
		int N;
		long long p,q,r,s;
		cin >> N >> p >> q >> r >> s;
		vector<long long> tr(N);
		for(int i =0; i < N; i++) {
			long long x =(1LL*i*p+q)%r;
			if(x < 0) x +=r;
			tr[i] =x+s;}
		vector<long long> S(N+1,0);
		for(int i =0; i < N; i++) S[i+1] =S[i]+tr[i];

		long long ans =S[N];
		int a =0;
		for(int i =0; i < N; i++) {
//			vsetky < a, >= a <= i, > i
			while(a < i && max(S[a+1],S[i+1]-S[a+1]) <= max(S[a],S[i+1]-S[a])) a++;
			ans =min(ans,max(S[N]-S[i+1],max(S[a],S[i+1]-S[a])));}
		cout << fixed << setprecision(12) << (1-1.0*ans/S[N]) << "\n";}
	return 0;}

// look at my code
// my code is amazing
