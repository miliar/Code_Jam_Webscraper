#include <vector>
#include <iostream>
#include <list>
#include <cmath>
#include <unordered_map>

using namespace std;

int T;
vector<string> input;

void getInput() {
	cin>>T;

	for (int i=0; i<T; i++) {
		int maxs;
		cin>>maxs;
		string vals;
		cin>>vals;
		input.push_back(vals);
	}
}

int main () {
	getInput();
	vector<int> ans;
	
	for (int i=0; i<T; i++) {
		string s = input[i];
		int v = 0;
		int count = s[0]-'0';
		for (int j=1; j<s.size(); j++) {
			int n = s[j]-'0';
			if (j>count) {
				v += j-count;
				count = j+n;
			}
			else {
				count += n;
			}
		}
		ans.push_back(v);
	}

	for (int i=0; i<T; i++) {
		cout<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;
	}

	return 0;
}
