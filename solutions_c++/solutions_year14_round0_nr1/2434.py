#include <iostream>

using namespace std;

int F[5][5];

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ": ";
		int A, B, a, b, c, d;
		cin >> A;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >> F[i][j];
		a = F[A - 1][0], b = F[A - 1][1], c = F[A - 1][2], d = F[A - 1][3];
		cin >> B;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >> F[i][j];
		int count = (F[B - 1][0] == a || F[B - 1][1] == a || F[B - 1][2] == a || F[B - 1][3] == a) + (F[B - 1][0] == b || F[B - 1][1] == b || F[B - 1][2] == b || F[B - 1][3] == b) + (F[B - 1][0] == c || F[B - 1][1] == c || F[B - 1][2] == c || F[B - 1][3] == c) + (F[B - 1][0] == d || F[B - 1][1] == d || F[B - 1][2] == d || F[B - 1][3] == d);
		if(count == 1) {
			if(F[B - 1][0] == a)
				cout << a << endl;
			else if(F[B - 1][0] == b)
				cout << b << endl;
			else if(F[B - 1][0] == c)
				cout << c << endl;
			else if(F[B - 1][0] == d)
				cout << d << endl;
			else if(F[B - 1][1] == a)
				cout << a << endl;
			else if(F[B - 1][1] == b)
				cout << b << endl;
			else if(F[B - 1][1] == c)
				cout << c << endl;
			else if(F[B - 1][1] == d)
				cout << d << endl;
			else if(F[B - 1][2] == a)
				cout << a << endl;
			else if(F[B - 1][2] == b)
				cout << b << endl;
			else if(F[B - 1][2] == c)
				cout << c << endl;
			else if(F[B - 1][2] == d)
				cout << d << endl;
			else if(F[B - 1][3] == a)
				cout << a << endl;
			else if(F[B - 1][3] == b)
				cout << b << endl;
			else if(F[B - 1][3] == c)
				cout << c << endl;
			else if(F[B - 1][3] == d)
				cout << d << endl;
		}
		else if(!count) {
			cout << "Volunteer cheated!" << endl;
		}
		else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}