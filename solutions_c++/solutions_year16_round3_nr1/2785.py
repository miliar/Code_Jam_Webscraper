#include <iostream>
#include <set>
#include <vector>
using namespace std;

class senate {
public:
	int pos, val;
	senate (int p, int v): val(v), pos(p) {}
	senate () {}
};

struct compare {
    bool operator() (const senate& a, const senate& b) const{
        if (a.val == b.val) return a.pos < b.pos;
    	return a.val > b.val;
    }
};


int main() {
	int T, N, temp, sum;
	cin >> T;
	set<senate, compare> V;
	senate f, s;
	std::set<senate>::iterator it;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ":";
		cin >> N ;
		sum = 0;
		for (int j = 0; j < N; j++) {
			cin >> temp;
			V.insert(senate(j, temp));
		}
		
		while(V.size() > 0) {
			it = V.begin(); f = *it;  V.erase(it); it++; s = *it;  V.erase(it); 
			cout << " " << (char)  ('A' + f.pos);
			if (f.val == s.val && (V.size()%2 == 0)) {
				cout << (char) ('A' + s.pos) ;
				s.val--;
			}
			f.val--;
			if (f.val > 0) {
				V.insert(f);
			}
			if (s.val > 0) {
				V.insert(s);
			}
		}
		V.clear();
		cout << "\n";
	}
	return 0;
}