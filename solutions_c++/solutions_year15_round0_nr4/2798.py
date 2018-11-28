#include<iostream>
using namespace std;

string R="RICHARD";
string G="GABRIEL";

int main() {
	int nCases; cin >> nCases;
	for(int caseNum=1;caseNum<=nCases;caseNum++) {
		int x, r, c; cin >> x >> r >> c;
		//cout << x << "  " << r << " " << c << endl;
		string ans;
		if (x==1) ans = G;//c
		if (x==2) {
			if (r==1 && c==1) ans = R; //c
			else if (r==1 && c==2) ans = G; //c
			else if (r==1 && c==3) ans = R; //c
			else if (r==1 && c==4) ans = G; //c

			if (r==2) {
				ans = G; //c
			}
			if (r==3) {
				if (c==1) ans = R;//c
				if (c==2) ans = G;//c
				if (c==3) ans = R;//c
				if (c==4) ans = G;//c
			}
			if (r==4) {
				ans = G;//c
			}
		}
		if (x==3) {
			if (r<2 || c<2) ans = R;//c
			if (r==2) {
				if (c==2) ans = R; //c
				if (c==3) ans = G;//c
				if (c==4) ans = R;//c
			}
			if (r==3) {
				if (c==2) ans = G;//c
				if (c==3) ans = G;//c
				if (c==4) ans = G;//c
			}
			if (r==4) {
				if (c==2) ans = R;//c
				if (c==3) ans = G;//c
				if (c==4) ans = R;//c
			}
		}
		if (x==4) {
			if (r<2 || c<2) ans = R;//c
			if (r==2) {
				if (c==2) ans = R; //c
				if (c==3) ans = R; //c
				if (c==4) ans = R; //c
			}
			if (r==3) {
				if (c==2) ans = R; //c
				if (c==3) ans = R; //c
				if (c==4) ans = G; //c
			}
			if (r==4) {
				if (c==2) ans = R; //c
				if (c==3) ans = G; //c
				if (c==4) ans = G; //c
			}
		}
		cout << "Case #"<<caseNum<<": " << ans << endl;
	}
	return 0;
}