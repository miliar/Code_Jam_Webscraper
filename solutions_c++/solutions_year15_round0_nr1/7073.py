#include <iostream>
using namespace std;

int main() {
	int t, smax, cant, amigos, temp;
	char a;
	cin >> t;

	for(int i=1;i<=t;i++) {
		cant = 0;
		amigos = 0;
		cin >> smax;
		for(int j=0;j<=smax;j++) {
			cin >> a;
			temp = a - '0';
			if(j <= cant) {
				cant += temp;
			}
			else {
				amigos += j - cant;
				cant += temp + j - cant;
			}
		}

		cout << "Case #" << i <<": " << amigos << endl;
	}

	return 0;
}