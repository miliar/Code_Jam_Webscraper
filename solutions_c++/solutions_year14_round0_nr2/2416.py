#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

double solve(double C, double F, double X) {
    double rate=2.0, ans=0.0;
	while (true) {
		if (X/(rate+F) > (X-C)/rate)
			break;
		ans+=C/rate;
		rate+=F;
	}
	//cout << C << " " << F << " " << X << endl;
	

	return ans+X/rate;
}

int main() {
//    freopen("B-small-attempt0.in", "rt", stdin);
//    freopen("B-small.out", "wt", stdout);
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
   
    int N;
    cin>>N;
	cout.precision(9);
    for (int i=1; i<=N; i++) {
        double C, F, X;
        cin>>C; cin>>F; cin>>X;
        cout << "Case #" << i << ": " << solve(C, F, X) << endl;
    }
}