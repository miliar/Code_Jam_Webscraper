#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <set>
#include <string>
#include <string.h>
#include <math.h>
#include <fstream>
using namespace std;
#define re return
#define LL long long
#define EPS 0.00000000001
#define MOD 1000000000
#define INF 1000000000000000
#define N 10008


int mmax;
char s[N];

int solve(){
	int need = 0, cur = 0;
	for (int i = 0; i <= mmax; ++i){
		int add = 0;
		if (i > cur){
			add = i - cur;
			need += add;
		}
		cur += add + s[i] - '0';
	}
	re need;
}

int main(){
#ifndef ONLINE_JUDGE
	ifstream cin("A-large.in");
	ofstream cout("A.out");
#endif
	
	int T;
	cin >> T;
	for (int t1 = 0; t1 < T; ++t1){
		memset(s, 0, sizeof(s));
		cin >> mmax >> s;
		cout<<"Case #"<<t1+1<<": "<<solve()<<endl;
	}
	re 0;
}