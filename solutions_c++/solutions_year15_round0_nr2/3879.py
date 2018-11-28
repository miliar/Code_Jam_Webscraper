#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++){
		double n, a[1234];
		cin >> n;
		for (int i = 0; i < n; i++){
			cin >> a[i];
		}

		double ans = 123456789;

		for (int MAX = 1; MAX <= 10; MAX++){
			double  special = 0;
			for (int i = 0; i < n; i++){
				if (a[i] > MAX){
					special += ceil( (a[i] / MAX - 1) );
				}
			}
			ans = min(ans, special + MAX);
		}
		cout << "Case #" << t << ": " << ans << endl;
	}

}