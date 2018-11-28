/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

using namespace std;

typedef long long LL;
typedef complex<double> point;
typedef long double ldb;
typedef pair<int,int> pii;

bool mark[1<<22];
int n,k;
int c[1000],t[1000],path[1000];
vector <int> store[1000];

bool go (int mask){
	if (mark[mask])
		return false;
	mark[mask] = true;
	if (mask == ((1<<n)-1)){
		for (int i=0; i<n; i++)
			cout << path[i] << ' ';
		cout << endl;
		return true;
	}
	for (int i=0; i<n; i++) if (((mask & (1<<i))==0) && (c[t[i]]>0)){
		c[t[i]]--;
		for (int j=0; j<(int)store[i].size(); j++)
			c[store[i][j]]++;
		path[__builtin_popcount(mask)] = i+1;
		if (go(mask ^ (1<<i)))
			return true;
		c[t[i]]++;
		for (int j=0; j<(int)store[i].size(); j++)
			c[store[i][j]]--;
	}
	return false;
}

int main(){
	int T; cin >> T;
	for (int o=1; o<=T; o++){
		cout << "Case #" << o << ": ";
		cin >> k >> n;
		for (int i=0; i<n; i++)
			store[i].clear();
		memset(c,0,sizeof c);
		for (int i=0; i<k; i++){
			int temp; cin >> temp;
			c[temp]++;
		}
		for (int i=0; i<n; i++){
			int len;
			cin >> t[i] >> len;
			for (int j=0; j<len; j++){
				int temp; cin >> temp;
				store[i].push_back(temp);
			}
		}
		memset(mark,false,sizeof mark);
		if (!go(0))
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
