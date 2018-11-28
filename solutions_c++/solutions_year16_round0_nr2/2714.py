#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <bitset>

using namespace std;

typedef vector<unsigned long long> vl;

#define ull unsigned long long
#define pb push_back

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	
	string in;
	getline(cin, in);

	for(int t = 1; t <= T; t++) {
		getline(cin, in);
		int N = in.size();

		vector<int> stack;
		for(int i = N-1; i >= 0; i--) {
			if(in[i] == '+') {
				stack.pb(1);
			} else {
				stack.pb(0);
			}
		}

		int flips = 0;
		while(!all_of(stack.cbegin(), stack.cend(), [](int i) {return i == 1;})) {
			int first = stack.back();
			int pos = stack.size()-1;
			while(stack[pos] == first && pos >= 0) {
				if(first == 0) {
					stack[pos] = 1;
				}
				pos -= 1;
			}
			flips += 1;

			if(first == 1) {
				while(stack[pos] == 0 && pos >= 0) {
					stack[pos] = 1;
					pos -= 1;
				}
				flips += 1;
			}
		}

		/*cout << in << endl;
		for(bool b : stack) {
			cout << b << " ";
		}
		cout << endl;*/
		cout << "Case #" << t << ": " << flips << endl;
	}

	return 0;
}
