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

using namespace std;

int main() {
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    string S;
    cin >> S;
    string ret = "";
    bool used[S.sz];
    SET(used, 0);
    int idx = S.sz - 1;
    while (idx > -1) {
    	int mm = idx, i = idx;
    	while (i > -1) {
    		if (S[i] > S[mm])
    			mm = i;
    		i--;
    	}
    	ret += S[mm];
    	used[mm] = true;
    	idx = mm - 1;
    }
    FOR (i, S.sz)
    	if (!used[i])
    		ret += S[i];
    cout << ret;
    cout << "\n";
  }
  return 0;
}
