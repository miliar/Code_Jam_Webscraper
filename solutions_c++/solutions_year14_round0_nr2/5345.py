#include <set>
#include <queue>
#include <vector>
#include <iomanip> 
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;


double solve(){
	double C, F, X;
	cin >> C >> F >> X;
	double minT = 1e12;
	double cps = 2;
	double t = 0;
	while (t < minT) {
		minT = min(minT, t + X / cps);		
		t += C / cps;
		cps += F;
	}
	return minT;
}
int main(){
#if 1
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		cout << "Case #" << i << ": ";
		printf("%0.10lf", solve());
		cout << endl;
	}
	return 0;
}