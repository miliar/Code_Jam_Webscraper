#include<iostream>
#include<fstream>
using namespace std;

int main() {
	int t,l,total,need;
	string s;
	cin >> t;
	fstream f;
	f.open("ans.txt");
	for(int c = 1; c <= t; ++c) {
		total = 0;
		need = 0;
		cin >> l >> s;
		for(int i = 0; i <= l; ++i) {
			if(total >= i)
				total += s[i]-'0';
			else {
				need += i-total;
				total = i+s[i]-'0';
			}
		}
		f << "Case #" << c << ": " << need << endl;
	}
	f.close();
	return 0;
}
