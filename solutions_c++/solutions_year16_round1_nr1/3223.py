#include <fstream>
#include <iostream>
#include <string>

using namespace std;

ofstream fout("out.txt");
ifstream fin ("A-large.in.txt");

#define cin fin
#define cout fout

int t, tt;
string s,a;

int main () {
	cin >> t;
	while (t) {
		tt++;
		t--;
		cin >> s;
		a = "";
		for(int i = 0; i < s.size(); i++) {
			if(i == 0) a = s[i];
			else if(a[0] <= s[i]) a = s[i] + a;
			else if(a[0] > s[i]) a = a + s[i];
		}
		cout << "Case #" << tt << ": " << a << endl;
	}	
	return 0;
}
