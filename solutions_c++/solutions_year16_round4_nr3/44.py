#include <iostream>
#include <vector>

using namespace std;

enum Dir { Left, Right, Up, Down };
typedef pair<int, int> P;
typedef pair<P, Dir> V;

ostream& operator<<(ostream& out, Dir dir) {
	if(dir == Left) out << "Left";
	if(dir == Right) out << "Right";
	if(dir == Up) out << "Up";
	if(dir == Down) out << "Down";
	return out;
}

struct Fuu { };

int R, C;
int n;
char X[128][128];
int Q[512];
vector<int> asd;

V getpos(int i) {
	if(i < C) return make_pair(P(0, i), Up);
	i -= C;
	if(i < R) return make_pair(P(i, C - 1), Right);
	i -= R;
	if(i < C) return make_pair(P(R - 1, C - 1 - i), Down);
	i -= C;
	if(i < R) return make_pair(P(R - 1 - i, 0), Left);
	throw 0;
}

V move(V x) {
	int i = x.first.first;
	int j = x.first.second;
	char& c = X[i][j];
	Dir nd;
	switch(x.second) {
		case Left:
			if(c == '\\') {
				nd = Down;
			} else {
				nd = Up;
				c = '/';
			}
		break;
		case Up:
			if(c == '/') {
				nd = Left;
			} else {
				nd = Right;
				c = '\\';
			}
		break;
		case Right:
			if(c == '\\') {
				nd = Up;
			} else {
				nd = Down;
				c = '/';
			}
		break;
		case Down:
			if(c == '/') {
				nd = Right;
			} else {
				nd = Left;
				c = '\\';
			}
		break;
	}
	return V(P(i, j), nd);
}

V invert(V v) {
	int i = v.first.first;
	int j = v.first.second;
	switch(v.second) {
		case Left: return V(P(i, j - 1), Right);
		case Right: return V(P(i, j + 1), Left);
		case Up: return V(P(i - 1, j), Down);
		case Down: return V(P(i + 1, j), Up);
	}
	throw 0;
}

void conn(int a, int b) {
	if(a >= b) throw 0;
//	cout << "CONN " << a + 1 << ' ' << b + 1 << '\n';
	V v = getpos(a);
	V t = getpos(b);
	while(true) {
//		cout << v.first.first << ' ' << v.first.second << ' ' << v.second << '\n';
		v = move(v);
//		cout << " -> " << v.first.first << ' ' << v.first.second << ' ' << v.second << '\n';
		if(v == t) break;
		int i = v.first.first;
		int j = v.first.second;
		if(i == 0 && v.second == Up) throw Fuu();
		if(i == R - 1 && v.second == Down) throw Fuu();
		if(j == 0 && v.second == Left) throw Fuu();
		if(j == C - 1 && v.second == Right) throw Fuu();
		v = invert(v);
	}
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	int tc;
	cin >> tc;
	for(int ti = 1; ti <= tc; ++ti) {
		fill((char*)X, (char*)X + 128 * 128, ' ');
		asd.clear();
		
		cin >> R >> C;
		n = 2 * R + 2 * C;
		
		for(int i = 0; i < n / 2; ++i) {
			int a, b;
			cin >> a >> b;
			--a;
			--b;
			Q[a] = b;
			Q[b] = a;
		}
		for(int i = 0; i < n; ++i) {
			asd.push_back(i);
		}
		cout << "Case #" << ti << ":\n";
		bool ok = true;
		try {
			while(!asd.empty()) {
				bool found = false;
				for(int i = 1; i < asd.size(); ++i) {
					if(Q[asd[i]] == asd[i - 1]) {
						conn(asd[i - 1], asd[i]);
						asd.erase(asd.begin() + i - 1);
						asd.erase(asd.begin() + i - 1);
						found = true;
						break;
					}
				}
				if(!found) throw Fuu();
			}
		} catch(Fuu x) {
			ok = false;
			cout << "IMPOSSIBLE";
		}
		if(ok) {
			for(int i = 0; i < R; ++i) {
				for(int j = 0; j < C; ++j) {
					if(X[i][j] == ' ') X[i][j] = '/';
					cout << X[i][j];
				}
				cout << '\n';
			}
		}
		cout << '\n';
	}
	
	return 0;
}
