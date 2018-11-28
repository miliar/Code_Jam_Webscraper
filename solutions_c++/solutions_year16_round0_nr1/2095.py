#include <iostream>
#include <ios>
#include <set>

using namespace std;
typedef unsigned long long oolong;

int main() {
	long t;
	oolong N, q;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for(int i=1;i<=t;++i) {
		cout << "Case #" << i << ": ";
		cin >> N;
		if(N) {
			set<char> digs;
			for(int j=1;j<100;++j) {
				string q=to_string(N*j);
				digs.insert(q.begin(),q.end());
				if(digs.size()==10) {
					cout << q << endl;
					break;
				}
			}
		} else cout << "INSOMNIA" << endl;
	}
}