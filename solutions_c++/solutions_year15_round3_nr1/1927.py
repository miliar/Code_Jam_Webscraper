#include<iostream>

using namespace std;

#define REP(a, b, c) for(int a=(b); a<(c); a++)

int main(){
	int T;
	cin >> T;
	REP(t, 0, T){
		int R, C, W;
		cin >> R >> C >> W;
		int z, y;
		z = (C+W-1)/W;
		y = R*z + W-1;
		cout << "Case #" << t+1 << ": " << y << "\n";
	}
	return 0;
}

