#include <iostream>

using namespace std;
int a[5][5],b[5][5];
int l1,l2,test,res;

int main(){
    cin >> test;
	for (int t = 1; t<=test; t++) {
		cin >> l1;
		for (int i=1; i<=4; i++) 
			for (int j=1; j<=4 ; j++) cin >> a[i][j];
		cin >> l2;
		for (int i=1; i<=4; i++) 
			for (int j=1; j<=4; j++) cin >> b[i][j];
		res = 0;
		for (int i=1; i<=4; i++) 
			for (int j=1; j<=4; j++) 
				if (a[l1][i] == b[l2][j]) {
					if (res == 0) res = a[l1][i] ; else res = -1;
				}
		
		switch (res) {
		case 0 : 
			cout <<"Case #"<< t <<": "<<"Volunteer cheated!";
			break;
		case -1 : 
			cout <<"Case #"<< t <<": "<<"Bad magician!";
			break;
		default:
			cout <<"Case #"<< t <<": "<<res;
		}
		if (t<test) cout << endl;
	}
}
