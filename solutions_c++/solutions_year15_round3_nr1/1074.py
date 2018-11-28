using namespace std;
#include <iostream>

int main(){
	
	int T;
	cin >> T;
	for (int n = 1; n <= T; n++){
	
		int R, C, W;
		cin >> R >> C >> W;
		int res = (C / W) * R + W - 1;
		if (C%W != 0) res ++;
		cout << "Case #" << n << ": " << res << endl;
	}
	
}
