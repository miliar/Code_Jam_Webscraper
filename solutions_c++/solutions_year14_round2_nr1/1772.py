#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
typedef long long ll;

void init() {
    cin.tie(0);
    ios::sync_with_stdio(false);
}

int main() {
    init();
	int t;
	cin >> t;
	rep(tt, t) {
		int n;
		vector<string> inputs, ins;
		cin >> n;
		rep(i, n) {
			string in;
			cin >> in;
			inputs.push_back(in);
			string in2 = "";
			in2 += in[0];
			for( int j=1; j<in.length(); j++ ) {
				if( in[j-1] != in[j] ) {
					in2 += in[j];
				}
			}
			ins.push_back(in2);
		}
		bool ok = true;
		for(int i=1; i<n; i++) {
			if( ins[0] != ins[i] ) {
				ok = false;
				break;
			}
		}
		cout << "Case #" << (tt+1) << ": ";
		if( !ok )
			cout << "Fegla Won" << endl;
		else {
			vector<int> index(n, 0);
			int sum = 0;
			rep(i, ins[0].length()) {
				char c = ins[0][i];
				int minc=200, maxc=0;
				rep(j, inputs.size()) {
					int cnt = 0;
					while( index[j]<inputs[j].length() && inputs[j][index[j]]==c ) {
						index[j]++;
						cnt++;
					}
					if( cnt < minc )  minc = cnt;
					if( maxc < cnt )  maxc = cnt;
				}
				sum += maxc - minc;
			}
			cout << sum << endl;
		}
	}
	return 0;
}
