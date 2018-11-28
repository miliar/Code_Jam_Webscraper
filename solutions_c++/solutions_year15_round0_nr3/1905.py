#include <cstring>
#include <iostream>
#include <set>
#include <algorithm>
#include <queue>
#include <climits>
using namespace std;

const string one = "1";

string toStr(char c) {
	string ret = "";
	ret += c;
	return ret;
}

string mul(string a, char b) {
	//cout << a << " " << b << endl;

	char sign = '+';
	if(a[0] == '-') {
		sign = '-';
		a = a.substr(1);
	}

	if(a == one) return (sign == '-' ? "-"+toStr(b) : toStr(b));
	if(b == one[0]) return (sign == '-' ? "-"+a : a);
	if(a[0] == b) return (sign == '-' ? one : "-1");

	if(a == "i" && b == 'j') return (sign == '-' ? "-k" : "k");
	if(a == "j" && b == 'i') return (sign == '-' ? "k" : "-k");
	if(a == "i" && b == 'k') return (sign == '-' ? "j" : "-j");;
	if(a == "k" && b == 'i') return (sign == '-' ? "-j" : "j");;
	if(a == "j" && b == 'k') return (sign == '-' ? "-i" : "i");;
	if(a == "k" && b == 'j') return (sign == '-' ? "i" : "-i");;

	return "zzzzzz";
}

int vis[10001][3];

bool isSolvable(const string& s, int a, int c) {
	if(a >= s.size()) return false;
	if(vis[a][c] != -1)
		return vis[a][c];

	if(c == 2) {
		string tmp = mul(one, s[a]);
		for(int i = a+1; i < s.size(); i++) tmp = mul(tmp, s[i]);
		//cout << tmp << endl;

		return (vis[a][c] = (tmp == "k"));
	}

	string tmp = one;
	for(int i = a; i < s.size(); i++) {
		tmp = mul(tmp, s[i]);

		//cout << tmp << endl;

		if(c == 0 && tmp == "i" && isSolvable(s, i+1, c+1)) return (vis[a][c] = 1);
		if(c == 1 && tmp == "j" && isSolvable(s, i+1, c+1)) return (vis[a][c] = 1);
	}

	return (vis[a][c] = 0);
}

int main() {
	int t;
	cin >> t;

	for(int z = 1; z <= t; z++) {
		int l, x;
		cin >> l >> x;

		string s;
		cin >> s;

		string str = "";
		for(int i = 0; i < x; i++)
			str += s;

		memset(vis, -1, sizeof vis);

		cout << "Case #" << z << ": " << (isSolvable(str, 0, 0) ? "YES" : "NO") << endl;
	}
}

