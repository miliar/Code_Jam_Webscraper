#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <math.h>
#include <map>

using namespace std;

int main(int argc, char** argv) {
	int T;
	cin >> T;

	int N;
	double x;

	vector<float> n;
	vector<float> k;

	for(int i=1; i<=T; i++) {
		cin >> N;

		n.clear(); k.clear();

		for(int j=0; j<N; j++) {
			cin >> x;
			n.push_back(x);
		}	
		for(int j=0; j<N; j++) {
			cin >> x;
			k.push_back(x);
		}

		// sort both
		sort(n.begin(), n.end());
		sort(k.begin(), k.end());

		int npoints = 0;
		int npoints1 = 0;
		int naomiIdx = 0;
		int kenIdx1 = 0;
		int kenIdxL = k.size()-1;

		vector<float> k1 = k;
		for(int j=0; j<N; j++) {
			double chosen1 = n[j];
			if(chosen1 < k[kenIdx1]) {
				// put chosen against his largest unused
				if(k[kenIdxL]<chosen1) npoints1++;
				kenIdxL--;
			} else {
				kenIdx1++;
				npoints1++;
			}
			int kenIdx = 0;
			while(kenIdx < k1.size() && k1[kenIdx]<chosen1) {
				if(k1[kenIdx]==-1) {
					kenIdx++;
					continue;
				}
				kenIdx++;
			}
			if(kenIdx == k1.size()) npoints++;
			else k1[kenIdx] = -1;
		}
		cout << "Case #" << i << ": " << npoints1 << " " << npoints << endl;
	}

}
