#include<iostream>
#include<vector>

using namespace std;

int main () {

	int casos;
	cin >> casos;
	for(int t=1 ; t<= casos; ++t) {
	
		vector<int> s(16, 0);
		
		int x,l;
		for(int k=0; k<2; k++) {
			cin >> l;			
			for(int i=0 ; i<4 ; i++) {
				for(int j=0 ; j<4 ; j++) {
					cin >> x;
					if (i ==  l-1){
						s[x-1] ++;
					}
				}			
			}
		}
		int dos = 0, v;
		for(int i=0 ; i<16; i++) {
  		dos += s[i] == 2;
  		if(s[i] == 2) v = i+1;
		}

		cout << "Case #" << t<< ": ";
		if(dos == 1) {
			cout << v << endl;
		}else if(dos == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}
