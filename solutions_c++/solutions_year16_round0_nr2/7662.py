#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int T, ans;
string st;

int main(){
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	cin >> T;
	for (int h=1; h<=T; h++){
		cin >> st;
		cout << "Case #" << h << ": ";
		ans = 0;
		for (int i=1; i<st.size(); i++) if (st[i] != st[i-1]) ans++; 
		if (st[st.size()-1] == '-') ans++;
		cout << ans << endl;
	}
}
