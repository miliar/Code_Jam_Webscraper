#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool canStand(int n_s, string s, int i) {
	if(n_s < i) return false;
	return true;	
}

int main(int argc, char** argv)
{
	int N;
	cin >> N;

	int T;
	string s;

	for(int n=0; n<N; n++) {
		cin >> T >> s;

		int total = 0, num_s = 0, extra = 0;
		for(int t=0; t<T+1; t++) {
			if(canStand(num_s, s, t)) {
				num_s += s[t] - '0';
			} else {
				extra += (t - num_s);
				num_s += (t - num_s) + s[t] - '0';
			}
		}
		cout << "Case #" << n+1 << ": " << extra << endl;
	}
	
	return 0;
}
