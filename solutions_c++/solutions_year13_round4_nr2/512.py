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
#define M 1000000
// mylittlepony
using namespace std;

int main() {
	int T,N;
	long long P;
	cin >> T;
	for(int t =0; t < T; t++) {
		cin >> N >> P;
		long long p =1;
		for(int i =0; i < N; i++) p *=2;
		P =p-P;
		long long k =1;
		int a =0;
		while(k <= P) {
			k *=2;
			a++;}
		long long x =1;
		for(int i =0; i <= N-a; i++) x *=2;
		cout << "Case #" << t+1 << ": " << min(x-2,p-1) << " ";
		k =x =1;
		P =p-P;
		a =0;
		while(k <= P) {
			k *=2;
			a++;}
		for(int i =0; i <= N-a; i++) x *=2;
		cout << max(0LL,p-x) << "\n";}
	return 0;}
        
// look at my code
// my code is amazing
