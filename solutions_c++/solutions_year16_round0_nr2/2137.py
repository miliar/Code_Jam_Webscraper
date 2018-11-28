#include <iostream>
#include <ios>
#include <set>
#include <string>

using namespace std;
typedef unsigned long long oolong;

int main() {
	long t;
	string q;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for(int i=1;i<=t;++i) {
		cout << "Case #" << i << ": ";
		cin >> q;
		q+="+";
		int c=0;
		for(auto it=q.rbegin()+1;it!=q.rend();++it) {
			if(*it!=*(it-1)) ++c;
		}
		cout << c << endl;
	}
}