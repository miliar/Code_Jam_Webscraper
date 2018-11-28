#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

void comp(int tc){
	int smax;
	cin >> smax;
	string digs;
	cin >> digs;
	int ans = 0, standing = 0;
	for (int i = 0; i <= smax; ++i){
		int cur = digs[i] - '0';
		if (cur && standing < i){
			ans += i - standing;
			standing = i;
		}
		standing += cur;
	}
	cout << "Case #" << tc << ": " << ans << endl;
}

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i){
		comp(i);
	}
}