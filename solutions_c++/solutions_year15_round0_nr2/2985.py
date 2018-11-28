// GCJ2015 Qual
// B: Infinite House of Pancakes

#include <iostream>
#include <string>
using namespace std;

int main() {
	int T, testcase;
	cin >> T;
	for (testcase=1; testcase<=T; testcase++) {
		int D, P, n[1001]={0}, ans=1000;
		cin >> D;
		for (int i=0; i<D; i++) {
			cin >> P;
			n[P]++;
		}

		for (int maxp=1; maxp<=1000; maxp++) {
			int time=0;
			for (int i=maxp+1; i<=1000; i++) {
				time += n[i] * ((int)((i-1)/maxp));
			}
			time += maxp;
			ans = min(ans, time);
		}
		cout << "Case #" << testcase << ": " << ans << endl;
	}
}
