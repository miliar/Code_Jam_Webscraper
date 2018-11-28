#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

typedef long long LL;

using namespace std;

int main() {
  freopen("Dl.out","wt", stdout);
  freopen("Dl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    LL K, C, S;
    cin >> K >> C >> S;
    vector<LL> ret;
    int idx = 0;
    while (idx < K) {
    	LL prev = 0LL;
    	FOR (i, C) {
    		prev *= K;
    		if (idx < K)
    			idx++;
    		prev += (idx - 1);
    	}
    	ret.pb(prev + 1);
    }
  	if (ret.size() <= S) {
  		FOR (i, ret.sz) {
  			if (i)
  				cout << " ";
  			cout << ret[i];
  		}
  	}
  	else
  		cout << "IMPOSSIBLE";
    cout << "\n";
  }
  return 0;
}
