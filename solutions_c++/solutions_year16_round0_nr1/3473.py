#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define SIZEOF(a) (sizeof(a)/sizeof((a)[0]))

typedef long long ll;

const int MAX_N = 20;
int a[MAX_N];

bool Check(){
	FOR(i,10) if(a[i]==0) return false;
	return true;
}

void Add(ll N){
	while(N>0){
		a[N%10] = 1;
		N/=10;
	}
}

int SolveCase(ll n)
{
	FOR(i,10) a[i]=0;
	ll N = n;
	FOR(i,1e6){
		Add(N);
		if(Check()) return N;
		N+=n;
	}
	return -1;
}

int test(){
	int t=1e4;
	FOR(i,t){
		cout << "Case #" << i+1 << ": ";
		const int r = SolveCase(1e6-i);
		if(r >= 0) cout << r;
		else cout << "INSOMNIA";
		cout << endl;
	}
}

int main()
{
	//test();return 0;
	int t; cin >> t;
	FOR(i,t){
		ll n; cin >> n;
		cout << "Case #" << i+1 << ": ";
		const int r = SolveCase(n);
		if(r >= 0) cout << r;
		else cout << "INSOMNIA";
		cout << endl;
	}
	return 0;
}
