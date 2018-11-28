#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	string S;
	string final;
	char prev=0;
	cin >> T;
	for(int i=0;i<T;++i) {
		final="";
		cout << "Case #" << i+1 << ": ";
		cin >> S;
		for(int j=0;j<S.length();++j) {
			prev=final[0];
			if(S[j]<prev) {
				final.push_back(S[j]);
			} else {
				final.insert(0,1,S[j]);
			}
		}
		cout << final << endl;
	}
	return 0;
}