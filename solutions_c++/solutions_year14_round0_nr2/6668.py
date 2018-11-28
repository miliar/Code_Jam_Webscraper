#pragma comment(linker, "/STACK:65777216")
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <stdio.h>
#include <deque>
#include <map>
#include <set>
#include <stack>
  
using namespace std;
  
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
  
typedef long long li;
typedef unsigned long long uli;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cout.setf(ios::fixed);
	cout.precision(7);
	int z;
	int t;
	cin >> t;
	for(z = 0; z < t; z++){
		double c, f, x;
		cin >> c >> f >> x;
		int i;
		double ans = x / 2;
		for(i = 1; i <= 100005; i++){
			double ans1 = ans;
			ans1 -= x / (2 + f * (i - 1));
			ans1 += c / (2 + f * (i - 1)) + x / (2 + f * i);
			if(ans1 < ans)
				ans = ans1;
		}
		cout << "Case #" << z + 1 << ": " << ans << "\n";
	}
	return 0;
}
/*

*/