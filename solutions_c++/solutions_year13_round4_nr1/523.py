// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#define dibs reserve
#define OVER9000 123456789012345678LL
#define tisic 47
#define soclose 10e-7
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define chocolate win
#define uint unsigned int
#define ff first
#define ss second
#define abs(x) ((x < 0)?(-x):x)
#define mod 1000002013LL
// mylittlepony
using namespace std;

int N;
long long cost(long long d) {
	return d*(N-1)-d*(d-1)/2;}

int main() {
	int T,M,a,b;
	cin >> T;
	for(int t =0; t < T; t++) {
		cin >> N >> M;
		vector<int> nas(N,0);
		vector<int> vys(N,0);
		long long ans0 =0, ans =0,c;
		for(int i =0; i < M; i++) {
			cin >> a >> b >> c;
			nas[--a] +=c;
			vys[--b] +=c;
			ans0 =(ans0+c*cost(b-a))%mod;}
		vector<int> z(N,0);
		for(int i =0; i < N; i++) {
			z[i] +=nas[i];
			for(int j =0; j < vys[i]; j++) for(int k =i; k >= 0; k--)
				if(z[k] > 0) {
					ans =(ans+cost(i-k))%mod;
					z[k]--;
					break;}}
		ans0 =(ans0-ans)%mod;
		if(ans0 < 0) ans0 +=mod;
		cout << "Case #" << t+1 << ": " << ans0 << "\n";}
	return 0;}
        
// look at my code
// my code is amazing
