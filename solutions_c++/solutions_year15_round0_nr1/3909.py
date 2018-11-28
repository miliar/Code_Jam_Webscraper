#include <iostream>
using namespace std;

int main() {
	int t;
	cin>> t;
	for(int tn=0; tn<t; tn++) {
		int smax;
		string s;
		cin>>smax;
		cin>>s;
		int ans = 0;
		int tot = 0;
		for(int i=0; i<s.size(); i++) {
			if (tot < i) {
				ans += i-tot;
				tot = i;
			}
			tot += s[i]-'0';
		}
		cout << "Case #"<<tn+1<<": "<<ans<<endl;
	}
}