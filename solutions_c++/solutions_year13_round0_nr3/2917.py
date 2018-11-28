#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;


bool ispal(unsigned long long i) {
	ostringstream oss;
	oss << i;
	string s = oss.str();
	for (int j=0;j<s.length();++j) {
		if (s[j] != s[s.length()-j-1])
			return false;
	}
	return true;
}

int main(void) {
	int T;
	cin>>T;
	for (int i=0;i<T;++i) {
		unsigned long long a,b;
		cin>>a;
		cin>>b;
		int count = 0;
		for (unsigned long long x = ceil(sqrt(a)); x<=floor(sqrt(b));++x) {
			if (ispal (x*x) & ispal(x)) {
				++count;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<'\n';
	}
}
