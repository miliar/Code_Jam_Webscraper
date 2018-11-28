#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>

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


int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(cnt,0,T){
		int s_max, acc = 0, added = 0;
		string s;
		cin >> s_max >> s;
		FOR(i,0,s_max+1) if(s[i] != '0'){
			if(acc < i){
				added += i-acc;
				acc = i;
			}
			acc += s[i]-'0';
		}
		cout << "Case #" << cnt+1 << ": " << added << '\n';
	}
	
	return 0;
}
