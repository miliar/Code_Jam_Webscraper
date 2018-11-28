#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	for (int I=0;I<N;I++){
		long r,t,c;
		cin >> r >> t;


		for (c=0;t>=0;c++){
			t -= 2*(r+2*c) + 1;
		}
		if (c == 1) c=2;
		cout << "Case #" << I+1 << ": " << c-1 << endl;
	}


	return 0;
}
