#include <iostream>
using namespace std;

char s[102];

int main() {
	int T;

	cin>>T;
	for (int ti = 1; ti <= T; ti++) {
		cout<<"Case #"<<ti<<": ";
		cin>>s;
		char last = s[0];
		int count = 1, 
			i = 1;
		while (s[i]) {
			if (last != s[i]) {
				last = s[i];
				count++;
			}
			i++;
		}
		if (last == '+') {
			count--;
		}
		cout<<count<<endl;
	}

	return 0;
}