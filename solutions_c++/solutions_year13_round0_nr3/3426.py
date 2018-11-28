#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <set>
#include <utility>

#define rep(i,j,k) for (int i = (int)j; i < (int)k; i++)
#define rep0(i,j) rep(i,0,j)
#define each(a,it) for (typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
#define mp(a,b) make_pair(a,b)
#define INF 999999

using namespace std;

long long T, A, B;

string convertInt(int number) {
   stringstream ss;
   ss << number;
   return ss.str();
}

bool isPal(int x) {
	
	string s1 = convertInt(x);
	string s2 = string( s1.rbegin(), s1.rend() );
	
	if (s1 == s2)
		return true;
	return false;
}

void solve (int i) {
	int count = 0;
	for (int j = ceil(sqrt(A)); j <= floor(sqrt(B)); j++) {
		
		if (isPal(j) && isPal(j*j))
			count++;
	}
	cout << "Case #" << i << ": " << count << "\n";
} 

int main(int argc, char *argv[]) {

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	
	cin >> T;
	
	rep (i,1,T+1) {
		cin >> A >> B;
		solve(i);
	}
}