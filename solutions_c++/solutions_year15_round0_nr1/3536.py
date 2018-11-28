#include <iostream>

using namespace std;
int T;
string ch;
int Smax;

int main() {
	freopen("A-large.in.txt", "r", stdin);
	freopen("StandingOvation.out", "w", stdout);
	cin>>T;
	for (int sT = 1; sT <= T; sT++) {
		cin>>Smax>>ch;
		int res = 0;
		int cur = 0;
		for (int i = 0; i <= Smax; i++) {
			if (ch[i] > '0') {
				res = res + max(0, i - cur);
				cur = cur + max(0, i - cur) + ch[i] - '0';
			}
		}
		cout<<"Case #"<<sT<<": "<<res<<endl;
	}
}