#include<iostream>
#include<set>
using namespace std;

int main() {
	int T,t,line,a,count,r;
	set<int> s;
	cin >> T;
	t = 0;
	while(t++<T) {
		s.clear();
		cin >> line;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				cin >> a;
				if (i+1 == line) {
					s.insert(a);
 				}
			}
		}
		count = 0;
		cin >> line;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				cin >> a;
				if (i+1 == line) {
					if (s.find(a) != s.end()) {
						count++;
						r = a;
					}
				}
			}
		}
		if (count == 1) {
			cout << "Case #" << t << ": " << r << endl;
		} else if (count == 0) {
			cout << "Case #" << t << ": Volunteer cheated!" << endl;
		} else {
			cout << "Case #" << t << ": Bad magician!" << endl;
		}		
	}
}