#define WU2

#include <iostream>
#include <limits.h>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
//#include <unordered_set>
//#include <unordered_map>

using namespace std;

typedef long long ll;




int main() {
#ifdef WU
	freopen("C://Users//wu//Desktop//in.txt", "r", stdin);
#endif
#ifdef WU2
	string file_name = "B-small-attempt0";
	freopen(("C://Users//wu//Desktop//" + file_name + ".in").c_str(), "r", stdin);
	freopen(("C://Users//wu//Desktop//" + file_name + ".out").c_str(), "w", stdout);
#endif

	int T, t = 0;
	cin >> T;

	while (T - (t++)) {
		int D;
		vector<int> P;
		int times = INT_MAX;
		cin >> D;
		for(int i = 0; i < D; i++) {
            int n;
            cin >> n;
            P.push_back(n);
		}
        for(int i = 1; i <=1000 ; i++) {
            int sum = i;
            for(auto m:P) {
                sum += (m-1)/i;
            }
            times = min(times,sum);
        }

		cout << "Case #" << t << ": ";
		cout << times << endl;


	}
}
