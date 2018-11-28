#include <iostream>
//#include <algorithm>
using namespace std;

void solve(){
	int X, Y;
	cin >> X >> Y;
	if (X > 0){
		for (int i = 0;i < X; ++i)
			cout << "WE";
	}else if (X < 0){
		for (int i = 0;i < -X; ++i)
			cout << "EW";
	}
	if (Y > 0){
		for (int i = 0;i < Y; ++i)
			cout << "SN";
	}else if (Y < 0){
		for (int i = 0;i < -Y; ++i)
			cout << "NS";
	}
}

int main(void){
	int T;
	cin >> T;
	for (int i = 1;i <= T; ++i){
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}