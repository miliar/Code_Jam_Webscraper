#include <iostream>
#include <string>
using namespace std;
const int MAXM = 10002;
int main() {
	int T;
	cin>>T;
	int X,R,C;
	for (int i=1;i<=T;i++) {
		cin>>X>>R>>C;
		string ans;
		if (X == 1) {
			ans = "GABRIEL";
		} else if (X == 2) {
			if ((R>=X && R%X==0) ||(C>=X && C%X==0)) {
				ans = "GABRIEL";
			} else {
				ans = "RICHARD";
			}
		} else if (X == 3) {
			if ((R>=X && R%X==0 && C>=2) ||(C>=X && C%X==0 && R>=2)) {
				ans = "GABRIEL";
			} else {
				ans = "RICHARD";
			}
		} else if (X==4) {
			if ((R==4 && C>=3) || (R>=3 && C==4)) {
				ans = "GABRIEL";
			} else {
				ans = "RICHARD";
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}