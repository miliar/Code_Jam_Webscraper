#include <iostream>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	int X,R,C;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> X >> R >> C;
		cout << "Case #" << t+1 <<": ";
		if (X==1) {
			cout << "GABRIEL" << endl;
		} else if (X==2) {
			if (R%2==1 && C%2==1) {
				cout << "RICHARD" << endl;
			} else cout << "GABRIEL" << endl;
		} else if (X==3) {
			if (R==1 || C==1) {
				cout << "RICHARD" << endl;
			} else if (R==3 || C==3) {
				cout << "GABRIEL" << endl;
			} else {
				cout << "RICHARD" << endl;
			}
		} else if (X==4) {
			if (R==4 && C==4) {
				cout << "GABRIEL" << endl;
			} else if ((R==4 && C==3) || (R==3 && C==4)) {
				cout << "GABRIEL" << endl;
			} else { cout << "RICHARD" << endl; }
		}
	}
}