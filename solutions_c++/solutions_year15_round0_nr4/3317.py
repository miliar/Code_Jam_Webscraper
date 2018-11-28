#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <utility>

using namespace std;


string solve_case() {
	int x, r, c;
	cin>>x>>r>>c;
	bool can = true;
	if ((r * c) % x) {
		can = false;
	}
	for (int i = 0; i < x; ++i) {
		int w = i + 1, l = x - i;
		if (max(w, l) > max(r, c) || min(w, l) > min(r, c)) {
			can = false;
		}
		if (x > 3 && w > 1 && l > 1 && max(w, l) > min(r, c)) {
			can = false;
		}
	}
	return can ? "GABRIEL" : "RICHARD";
}

int main() {
	int tt;
	cin>>tt;
	for (int t = 1; t <= tt; ++t) {
		cout<<"Case #"<<t<<": "<<solve_case()<<endl;
	}
	return 0;
}

