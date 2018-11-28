#include <vector>
#include <iostream>
using namespace std;
vector <int> f(int a) {
vector <int> rowa;
	//cout << a << endl;
                for ( int i = 0 ; i < 4 ; i++ ) {
                        for ( int j = 0 ; j<4; j++ ) {
                               int t;
				 cin >> t;
				if ( i+1 == a ) {
                                        //int t;
                                        //cin >> t;
					
					rowa.push_back(t);
					//cout << t<<endl;
                                }
                        }
                }
	return rowa;
}
int main() {
	int T;
	cin >> T;
	for ( int i = 1; i <= T; i++ ) {
		int a, b;
		cin>>a;
		vector <int> rowa = f(a);
		cin >> b;
		vector <int> rowb = f(b);
		int matches = 0;
		int ret = 0;
		//cout << rowa.size() << " "<<rowb.size();
		for ( int i = 0; i < 4; i++ ) {
			for ( int j = 0; j < 4; j++ ) {
				if ( rowa[i] == rowb[j] ) {
					matches++;
					ret = rowa[i];
				}
			}
		}	
		cout << "Case #"<<i <<": ";
		if ( matches == 1 ) {
			cout << ret <<endl;
		}
		if ( matches >= 2 ) {
			cout << "Bad magician!"<<endl;
		}
		if ( matches == 0 ) {
			cout << "Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
