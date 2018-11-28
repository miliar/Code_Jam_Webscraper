#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

void test(int t){
	cout << "Case #" << t << ": ";
	string s; cin >> s;
	int ans = 0;
	for (int i=1;i<s.length();i++){
		if (s[i] != s[i-1]) ans++;
	}
	if (s[s.length()-1] == '-') ans++;
	cout << ans << endl;
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.txt","w",stdout);
	int n; cin >> n;
	for (int i=1;i<=n;i++) test(i);
}
