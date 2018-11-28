#include <iostream>
#include <string.h>

using namespace std;

string ns(int i) {
	if (i==1) return "11";
	else return "00";
}

int main(void) {

	int t;
	cin >> t;
	int N;
	cin >> N;
	//N=16;
	int J;
	cin >> J;
	//J=50;
	int tmp=0;
	int td=0;

	cout << "Case #1:" << endl;
	for(int i=0; i<J;i++) {
		tmp=i+1;
		cout << "11";
		for (int j=(N-4)/2;j>0;j--) {
			td = (tmp>>(j-1)) & 1;
			cout << ns(td);
		}
		cout << "11 ";
		for (int k=2; k<=10; k++) {
			cout << k+1 << " " ;
		}
		cout << endl;
	}
		
	return 0;
}
