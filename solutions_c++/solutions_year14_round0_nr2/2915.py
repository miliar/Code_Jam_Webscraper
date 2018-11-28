#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.in","w",stdout);
	int T;
	int k = 1;
	cin >> T;
	while(T--){
		double C , F , X;
		cin >> C >> F >> X;
		double old = 0 , add = 2;
		double res = 2000000000;
		for(int i = 0 ; i < 100000 ; ++i){
			res = min(res , old + X / add);
			old += C / add;
			add += F;
		}
		cout << "Case #" << k << ": " << setprecision(7) << fixed << res << endl;
		k++;
	}
	return 0;
}
