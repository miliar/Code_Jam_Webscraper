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

const int MAX = 1000*1000+100;

inline int rev(int a){
	int b = 0;
	while(a){
		b = b*10+(a%10);
		a /= 10;
	}
	return b;
}

int main(){
	ios_base::sync_with_stdio(false);

	VI ans;
	ans.resize(MAX);
	ans[1] = 1;
	FOR(i,2,MAX){
		int j = rev(i);
		ans[i] = ans[i-1]+1;
		if(j < i && i%10)
			ans[i] = min(ans[j]+1, ans[i]);
	}
	cerr << 'o';

	int T;
	cin >> T;
	FOR(cnt,0,T){
		int n;
		cin >> n;
		cout << "Case #" << cnt+1 << ": " << ans[n] << endl;
	}
	cerr << 'k';

	return 0;
}
