#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define LARGE

using namespace std;

void checkNum(int i, bool v[]);
bool done(bool v[]);

int main(int argc, char *argv[]) {

	//freopen("A-small.in", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
	 	bool v[10] = {false, false, false, false, false, false, 
				false, false, false, false};
		int N;
		cin >> N;
		int n = 0;
		while (n <= 500000) {
			checkNum(N * ++n, v);
			if (done(v)) {
				break;
			} 
		}
		if (n > 500000) {
			cout << "Case #"<<(i+1)<<": INSOMNIA\n";
		} else {
			cout << "Case #"<<(i+1)<<": "<<N * n<<"\n";
		}
	}
	return 0;
}

void checkNum(int i, bool v[]) {
	v[i % 10] = true;
	if (i > 9) 
		checkNum(i / 10, v); 
}

bool done(bool v[]) {
	for (int i = 0; i < 10; i++) {
		if (v[i]) {
			continue;
		} else {
			return false;
		}
	}
	return true;
}
