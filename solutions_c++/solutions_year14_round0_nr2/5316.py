#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
		double C,F,X;
		cin >> C >> F >> X;
		double best = X/2;
		double time = 0;
		double rate = 2;
		for(int farms=0; farms*C<=X*200; farms++) {
			//cout << farms << " " << time << " " << X/2 << endl;
			time += C/rate;
			rate += F;
			best = min(best, time+X/rate);
		}
		printf("%.7lf\n",best);
        }
}
