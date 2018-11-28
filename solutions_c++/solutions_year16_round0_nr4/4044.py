#include <bits/stdc++.h>

using namespace std;

int main (){
	freopen("D-small-attempt0 (1).in", "r", stdin);
	freopen("ivan.out", "w", stdout);
	int testcase;
	cin >> testcase;
	int K, C, S;
	for(int i = 0; i < testcase; i++){
		cin >> K >> C >> S;
		cout << "Case #" << i + 1 << ": ";
		for(int j = 1; j < K + 1; j++){
			cout << j << " ";
		}
		cout << endl;
	}
}
