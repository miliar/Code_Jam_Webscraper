//      ------>>          in the name of Allah          <<------
#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <string>
#include <iomanip>
#include <cstring>
#include <memory.h>
#include <iostream>
#include <algorithm>
/**/

#define fr first
#define se second
#define PI acos(-1)
#define Mod 1000000007
#define Max (1<<30)
#define Min -(1<<30)
#define prt fixed << setprecision(12)
#define endl "\n"

using namespace std;

int main() { ios::sync_with_stdio(0); cin.tie(0);
	int T, X = 1;
	cin >> T;
	while(T--) {
		vector <char> v;
		string s;
		cin >> s;
		int n = s.size();
		v.push_back(s[0]);
		for(int i=1; i<n; i++) {
			if(s[i] >= v[0]) v.insert(v.begin(), s[i]);
			else v.push_back(s[i]);
		}
		cout << "Case #" << X++ << ": ";
		for(int i=0; i<n; i++) cout << v[i];
		cout << endl;
	}
	return 0;
}