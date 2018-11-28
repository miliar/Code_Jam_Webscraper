#include <iostream>
#include <set>
#include <fstream>
#include <string>
using namespace std;
int n,t,j;
ifstream fin("B-large.in.txt");
#define cin fin
ofstream fout("out.txt");
#define cout fout
string s;
int main () {
	cin >> t;
	while(t) {
		t--;
		j++;
		cin >> s;
		int x = 0;
		int ans = 0;
		for(int i = s.size()-1; i >= 0; i--) {
			if(s[i] == '-' && x%2==0) { 
				x = 1-x;
				ans++;
			} else if(s[i] == '+' && x%2) {
				x = 1-x;
				ans++;
			}
		}
		cout << "Case #" << j << ": " << ans << endl;
	}
	return 0;
}
