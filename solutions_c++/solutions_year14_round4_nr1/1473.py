#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream inp("A-large.in");
	cin.rdbuf(inp.rdbuf());
	ofstream out("output.txt");
	cout.rdbuf(out.rdbuf());
	int T; cin>>T;
	for(int t=1; t<=T; t++) {
		int r = 0;
		int n, x; cin>>n>>x;
		vector<int> s(n);
		for(int i=0; i<n; i++)
			cin>>s[i];
		sort(s.begin(), s.end());
		int i1=0, i2=n-1;
		while(i1<=i2) {
			if (s[i1]+s[i2]<=x) i1++;
			i2--;
			r++;
		}
		cout<<"Case #"<<t<<": "<<r<<endl;
	}
	return 0;
}