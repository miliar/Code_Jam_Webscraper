#include <iostream> 
#include <fstream> 
#include <cmath> 
#include <algorithm> 
#include <cassert> 
#include <string> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <map> 
#include <set> 
#include <stack> 
#include <iomanip> 
#include <queue> 

#define pb push_back 
#define mp make_pair 
#define ll long long 
#define abracadabra next 
#define pii pair<int, int> 

using namespace std; 

char a[111111];

string solve(char ch, int l, int r) {
	if (l == (r - 1)) {
		a[l] = ch;
		string t;
		t.push_back(ch);
		return t;
	} else if (ch == 'R') {
		string a = solve('R', l, (l + r) / 2);
		string b = solve('S', (l + r) / 2, r);
		return min(a + b, b + a);
	} else if (ch == 'S') {
		string a = solve('P', l, (l + r) / 2);
		string b = solve('S', (l + r) / 2, r);
		return min(a + b, b + a);
	} else if (ch == 'P') {
		string a = solve('P', l, (l + r) / 2);
		string b = solve('R', (l + r) / 2, r);
		return min(a + b, b + a);
	}
}

int n, r, p, s;
string ans;

bool check(char ch) {
	string t = solve(ch, 0, (1 << n));
	int R = r, P = p, S = s;
	for(int i = 0; i < (1 << n); i++) {
		if (a[i] == 'R')
			R--;
		if (a[i] == 'S')
			S--;
		if (a[i] == 'P')
			P--;
	}
	if(R == 0 && S == 0 && P == 0) {
		if (ans == "")
			ans = t;
		else
			ans = min(t, ans);
	}
}

int main(){ 
	ios_base::sync_with_stdio(false); 
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{

		cin >> n >> r >> p >> s;
		ans = "";
		check('P');
		check('S');
		check('R');
		cout << "Case #" << test << ": ";
		if (ans != "")
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	
	
	return 0; 
} 
