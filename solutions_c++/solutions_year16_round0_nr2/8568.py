#include <iostream>
#include <cstdio>
using namespace std;


int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,n;
	cin>>T;
	bool checkMinus;
	string s;
	for(int k = 1; k <= T; k++) {
		cin>>s;
		n = 0;
		checkMinus = true;

		for(int i = s.size() - 1; i >= 0; i--) {
			if(checkMinus) {
				if(s[i] == '-') {
					n++;
					checkMinus = false;
				}
			}
			else {
				if(s[i] == '+') {
					n++;
					checkMinus = true;
				}
			}
		} 
		cout<<"Case #"<<k<<": "<<n<<endl;
	}

	return 0;
}