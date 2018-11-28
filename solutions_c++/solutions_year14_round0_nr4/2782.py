#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		int N;
		cin >> N;
		vector<double> p1;
		vector<double> p2;
		for( int j = 0; j < N; j++ ) {
			double p;
			cin >> p;
			p1.push_back(p);
		}
		sort(p1.begin(), p1.end());
		for( int j = 0; j < N; j++ ) {
			double p;
			cin >> p;
			p2.push_back(p);
		}
		sort(p2.begin(), p2.end());
	
	
		int res1 = 0;
		int k = 0;
		for( int j = 0; j < N; j++ ) {
			if( p1[j] > p2[j-k] ) {
				res1++;
			} else {
				k++;
			}
		}
		int res2 = 0;
		k = 0;
		for( int j = 0; j < N; j++ ) {
			if( j + k >= N ) {
				res2++;
			} else if( p1[j] > p2[j + k] ) {
				k++;
				j--;
			}
		}
		cout << "Case #" << i << ": " << res1 << " " << res2 << endl;
	}

	return 0;
}