#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <iomanip>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef istringstream iss;
typedef ostringstream oss;

int main(){
	#ifndef ONLINE_JUDGE
 		freopen("B-large.in", "r", stdin);//B-small-attempt0.in
		freopen("B-large.out", "w", stdout);
	#endif
	ios_base::sync_with_stdio(false);
	double C, X, F;
	int n;
	cin >> n;
	int m = n;
	for(int k = 0; k <n; k++){
		cin >> C >> F >> X;
		int i = 0;
		while (true) {
			if( (C/(2+F*i) + X/(2+F*(i+1))) > X/(2 +F*i)) break;
			i++;
		}
		double t = 0;
		for(int j = 0; j < i; j++){
			t += C/(2 + F*j);
		}
		t += X/(2+F*i);
		printf("Case #");
		printf("%d", k+1);
		printf(": ");
		//cout << "Case #" <<  k + 1 <<  ": ";
		printf("%.7lf\n", t);
		
	}

	return 0;
}



