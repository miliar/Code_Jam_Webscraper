#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
typedef long long ll;
typedef pair<int,int> pii;

int main() {
	int t;
	cin >> t;
	rep(tt, t) {
		string s;
		cin >> s;
		int turn = 0, head=0;
		int mode = (s[0]=='+' ? 1 : 0);
		while(1) {
			if(mode) {
				while(head < s.length() && s[head]!='-') head++;
				if(head == s.length()) break;
			} else {
				while(head < s.length() && s[head]!='+') head++;
			}
			mode = 1 - mode;
			turn++;
		}
		cout << "Case #" << (tt+1) << ": " << turn << endl;
	}
	return 0;
}
