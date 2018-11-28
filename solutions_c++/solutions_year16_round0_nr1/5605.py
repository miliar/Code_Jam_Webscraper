#include <iostream>
#include <vector>
#include <set>
using namespace std;

int calc(int N){
	set<int> digitsSeen;
	long long f = N;
	while(true){
		long long g = f;
		while (g != 0){
			digitsSeen.insert(g%10);
			g /= 10;
			}
		if (10 == digitsSeen.size()	) return f;
		f += N;
		}
	}
const bool test = false;
int main(void){
	int t;
	cin >> t;
	for (int i = 1; i <= t; i += 1){
		int N;
		if (!test) {
			cin >> N;
		} else {
			N = i;
		}
		cout << "Case #" << i << ": ";
		if (0 == N) {
		cout << "INSOMNIA";
		} else {
		cout << calc(N);
		}
		cout << "\n";
		}
	return 0;
	}
