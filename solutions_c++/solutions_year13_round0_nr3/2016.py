#include <iostream>
#include <list>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <complex>
#include <ctime>
#include <cctype>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 1000000

int make_pal(int n, int d){
	int ans = n;
	if (d>=0) ans = ans*10 + d;	//for odd length palindromes
	while(n){
		ans = ans*10 + n%10;
		n/=10;
	}
	//cout << n << " " << d << " " << ans << endl;
	return ans;
}


int gen_pals(int* P, int N){	//generate all palindromes <= K
	int K = 0;
	#warning make sure last digit is non_zero
	for(int n=0;P[K-1] <= 10*N;++n){
		FORALL(d,-1,9) P[K++] = make_pal(n,d);
	}
	sort(P,P+K);
	K = unique(P,P+K) - P;
	while (P[K-1] > N) K--;
	return K;
}

ll reverse(ll N){
	ll ans = 0;
	while(N) ans = ans*10 + N%10, N/=10;
	return ans;
}

bool is_pal(ll N){
	return N == reverse(N);
}

int P[MAXN];
ll S[MAXN];

int F(ll N, int K){
	return upper_bound(S,S+K,N) - S - 1;
}

int main(){
	int K = gen_pals(P,10000000);
	int j = 0;
	FOR(i,K) {
		S[j] = P[i]*(ll)P[i];
		if (is_pal(S[j]))j++;
	} K = j;
	
	//S now holds the fair and square numbers
	int TEST;
	cin >> TEST;
	FOR(test,TEST){
		ll A,B;
		cin >> A >> B;
		
		cout << "Case #" << (test+1) << ": ";
		cout << F(B,K) - F(A-1,K) << endl;
	}
}













