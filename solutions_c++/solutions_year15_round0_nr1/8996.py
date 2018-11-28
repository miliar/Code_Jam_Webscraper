#include <iostream>

using namespace std;

int main() {
	int inpiedi = 0, aggiunti = 0, n, n2, persone;
	char curr;

	cin >> n;
	for(int i=0; i<n; i++){
		aggiunti = 0;
		inpiedi = 0;
		cin >> n2;
		n2++;
		for(int j=0; j<n2; j++) {
			cin >> curr;
			persone =  ((int)curr)-((int)'0');
			if(j==0) {
				inpiedi += persone;
			}
			else {
				int diff = inpiedi-j;
				if((persone!=0) && (diff<0)) {
					inpiedi += -diff;
					aggiunti += -diff;
				}
				inpiedi += persone;
			}
		}
		cout << "Case #" << i+1 << ": " << aggiunti << endl;
	}
}