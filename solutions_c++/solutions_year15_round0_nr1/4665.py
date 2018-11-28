#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
using namespace std;

string solve(string s) {
	int ans=0, ppl=0; 
	for (int i=0; i<s.size(); i++){
		ppl+=s[i]-'0';
		if (ppl<=i) {
			ans++;
			ppl++;
		}
	}
	return to_string(ans);
}

int main() {
	//freopen("A-small-attempt0.in", "rt", stdin); freopen("A-small.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin); freopen("A-large.out", "wt", stdout);
	//freopen("test.in","rt",stdin); freopen("test.out","wt",stdout);

	int N, t;
	string s;
	cin>>N;
	for (int i=0; i<N; i++) {
		cin>>t>>s;
		cout << "Case #" << i+1 << ": " << solve(s) << endl;
	}
}
