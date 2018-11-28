#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T; i++) {
		int r;
		int n;
		bool carta[16];
		for(int j=0; j<16; j++)
			carta[j] = true;
		cout << "Case #" << i << ": ";
		for(int j=0; j<2; j++) {
			cin >> r;
			for(int k=1; k<=4; k++) {
				for(int l=0; l<4; l++) {
					cin >>n;
					n--;
					carta[n] = carta[n] && k==r;
				}
			}
		}
		n=0;
		for(int j=0; j<16; j++) {
			if(!carta[j]) continue;
			n++;
			if(n>1) break;
			r=j+1;
		}
		if(n>1) cout << "Bad magician!\n";
		else if(n==0) cout << "Volunteer cheated!\n";
		else cout << r << endl;
	}
	return 0;
}
