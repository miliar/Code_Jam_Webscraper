using namespace std;
#include <iostream>

int main(){
	
	int T;
	cin >> T;
	for (int n = 1; n <= T; n++){
		int X, R, C;
		cin >> X >> R >> C;

		if ( (R*C)%X != 0)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==1 || X==2)
			cout << "Case #" << n << ": GABRIEL" << endl;


		else if (X==3 && R==1 && C==3)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==3 && R==2 && C==3)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else if (X==3 && R==3 && C==1)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==3 && R==3 && C==2)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else if (X==3 && R==3 && C==3)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else if (X==3 && R==3 && C==4)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else if (X==3 && R==4 && C==3)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else if (X==4 && R==1 && C==4)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==4 && R==2 && C==2)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==4 && R==2 && C==4)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==4 && R==3 && C==4)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else if (X==4 && R==4 && C==1)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==4 && R==4 && C==2)
			cout << "Case #" << n << ": RICHARD" << endl;

		else if (X==4 && R==4 && C==3)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else if (X==4 && R==4 && C==4)
			cout << "Case #" << n << ": GABRIEL" << endl;

		else
			cout << "Case #" << n << ": OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO" << endl;
	}
	
}
