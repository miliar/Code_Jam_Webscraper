#include <iostream>
#include <set>
#include <fstream>
using namespace std;
set<int> s;
int n;
int t;
long long x;
int j;
ifstream fin("A-large.in.txt");
#define cin fin
ofstream fout("out.txt");
#define cout fout
int main () {
	cin >> t;
	while(t) {
		t--;
		j++;
		cin >> n;
		bool o = 0;
		s.clear();
		for(long long i = 1; i <= 1000; i++) { 
			x = i*n; 
			while(x) { 
				s.insert(x%10); x/=10; 
			} if(s.size() == 10) { 
				cout << "Case #" << j << ':' << ' ' <<  i*n << endl; o = 1; 
				break; 
			} 
		}
		if(!o) { cout <<  "Case #" << j << ':' << " INSOMNIA\n"; }
	}
	return 0;
}

/*
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
*/
