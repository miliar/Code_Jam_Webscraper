#include <iostream>
#include <string>

using namespace std;

#define For(i, od, po) for(int (i) = (od); (i) < (po); (i)++)

void solve(int t){
	string s;
	cin >> s;
	int a = 0, b = 0;
	char last = '*';
	for(auto c: s){
		if(c == last) continue;
		if(c == '-') a++;
		else b++;
		last = c;
	}
	if(last == '+') a--;
	cout << "Case #" << t << ": " << a + b << endl;
	return;
}

int main(){
	int T;
	cin >> T;
	For(i, 0, T) solve(i+1);
	return 0;
}