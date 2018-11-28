#include <iostream>
using namespace std;

int A[4][4], B[4][4], C[4], D[4], qwerty;

int match(){
	int m=0;
	for(int i=0; i < 4; i++)
	{
		for(int j=0; j < 4; j++){
			if (C[i] == D[j]) {
				m++;
				qwerty = C[i];
			}
		}
	}
	return m;
}

int main ()
{
	int t;
	cin >> t;
	for(int q=1; q<=t; q++){
		int p1, p2;
		cin >> p1;
		for(int i=0; i < 4; i++){
			for(int j=0; j < 4; j++){
				cin >> A[i][j];
				if(i==(p1-1)){
					C[j] = A[i][j];
				}
			}
		}
		cin >> p2;
		for(int i=0; i < 4; i++){
			for(int j=0; j < 4; j++){
				cin >> B[i][j];
				if(i==(p2-1)){
					D[j] = B[i][j];
				}
			}
		}
		int ans;
		ans = match();
		cout << "Case #" << q << ": ";
		if(ans == 0){cout << "Volunteer cheated!" << endl;}
		else if(ans == 1){cout << qwerty << endl;}
		else {cout << "Bad magician!" << endl;}
	}
	return 0;
}