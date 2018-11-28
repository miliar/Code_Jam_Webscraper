#include "iostream"
#include "string"
#include "vector"
#include "algorithm"
#include "numeric"
#include "queue"
#include "set"
#include "sstream"
#include "tuple"

using namespace std;

struct P {
	int count;
	char name;

	bool operator<(const P& p2) const {
		return tie(count, name) > tie(p2.count, p2.name);
	}
};

struct Solution {
	set<P> p;

	bool valid() {
		if (p.size() == 0) return true;
		if (p.size() == 1) return false;
		if (p.size() == 2) return p.begin()->count == next(p.begin())->count;
		if (p.size() >= 3) return true;
		throw exception();
	}

	char take_one() {
		auto party = *p.begin();
		p.erase(party);
		party.count--;
		if (party.count > 0) p.insert(party);
		return party.name;
	}

	void solve() {
		while (p.size() > 0) {
			cout << take_one();
			if (!valid()) cout << take_one();
			cout << " ";
		}
	}
};

int main() {
	int T = 0;
	cin >> T;

	for (int t = 0; t < T; t++) {
		int N;
		cin >> N;
		set<P> p;
		for (int i = 0; i < N; i++) {
			int count;
			cin >> count;
			p.insert({ count, 'A' + (char)i });
		}
		cout << "Case #" << t + 1 << ": ";
		Solution{ p}.solve();
		
		cout << endl;
	}

	return 0;
}