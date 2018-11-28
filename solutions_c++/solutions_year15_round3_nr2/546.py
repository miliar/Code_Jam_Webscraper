#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

#include <unordered_map>
#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second

int K, L, S;
long double avg, maxx;
string keys, target;
string str;

void gen(int left){
	if(left == 0){
		int occ = 0;
		FOR(i,0,S-L+1)
			if(str.substr(i,L) == target)
				occ++;
		maxx = max(maxx, (long double)occ);
		avg += occ;
		//cerr << "*" << str << ' ' << occ << endl;
		return;
	}
	left--;
	FOR(i,0,K){
		str[left] = keys[i];
		gen(left);
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(cnt,0,T){
		cin >> K >> L >> S;
		cin >> keys >> target;
		str.resize(S);
		avg = 0;
		maxx = 0;
		gen(S);
		//cerr << "**" << maxx << ' ' << avg << endl;
		FOR(i,0,S)
			avg /= K;
		cout << "Case #" << cnt+1 << ": " << fixed << setprecision(7) << maxx-avg << endl;
	}

	return 0;
}
