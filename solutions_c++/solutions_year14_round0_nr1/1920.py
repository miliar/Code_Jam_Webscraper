#include <iostream>
#include <set>

using namespace std;

int main()
{
	int cases = 0, T;
	cin >> T;
	while (T--) {
		int N, tmp, hits = 0;
		set<int> s;
		cin >> N;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> tmp;
				
				if ( N - 1 == i) {
					s.insert(tmp);
				}
			}
		}
		cin >> N;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> tmp;
				if ( N - 1 == i) {
					if (s.find(tmp) != s.end()) {
						hits = hits ? -1 :tmp ;
					}
				}
			}
		}
		cout << "Case #" << ++cases << ": ";
		switch (hits) {
		case -1:
			cout << "Bad magician!";
			break;
		case 0:
			cout << "Volunteer cheated!";
			break;
		default:
			cout << hits;
			break;
		}
		cout << endl;
	}
	return 0;
}