#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	cin.sync_with_stdio(false);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++){
		int N, m, previous = 0;
		cin >> N;
		int result = 0;
		int result2 = 0;
		vector<int> v;
		int maxSpeed = 0;
		for (int i = 0; i < N; i++){
			cin >> m;
			int a = previous - m;
			if (a > 0){
				result += a;
			}
			if (a > maxSpeed){
				maxSpeed = a;
			}
			previous = m;
			v.push_back(m);
		}
		for (int i = 0; i < N-1; i++){
			int add = min(v[i],maxSpeed);
			result2 += add;
		}
		cout << "Case #" << t << ": " << result << " " << result2 << endl;
	}

	return 0;
}
