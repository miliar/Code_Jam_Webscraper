#include <iostream>
using namespace std;

struct quat {
	int v, s;
	quat(int _v=0, int _s=1) {
		v = _v; s = _s;
	}
};

int mul[4][4] = { {0,1,2,3}, {1,0,3,2}, {2,3,0,1}, {3,2,1,0} };
int muls[4][4] = { {1,1,1,1}, {1,-1,1,-1}, {1,-1,-1,1}, {1,1,-1,-1} };

quat operator*(const quat &a, const quat &b) {
	return quat(mul[a.v][b.v], a.s*b.s*muls[a.v][b.v]);
}

bool operator==(const quat &a, const quat &b) {
	return a.v==b.v && a.s==b.s;
}

int main() {
	int T, t, N, K, S, i, j;
	string n, s;
	quat q[3] = {quat(1,1), quat(2,1), quat(3,1)}, RES, left, right;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N >> K >> n;
		
		S = N*K; s = "";
		for (i=0; i<K; i++) s += n;
		
		RES = quat(0,1);
		for (i=0; i<S; i++) RES = RES*q[s[i]-'i'];
		
		cout << "Case #" << t << ": ";
		if (RES == quat(0,-1)) {
			left = quat(0,1);
			for (i=0; i<S; i++) {
				left = left*q[s[i]-'i'];
				if (left == quat(1,1)) break;
			}
			
			right = quat(0,1);
			for (j=S-1; j>=0; j--) {
				right = q[s[j]-'i']*right;
				if (right == quat(3,1)) break;
			}
			
			if (i < j) cout << "YES" << endl;
			else cout << "NO" << endl;
		} else cout << "NO" << endl;
	}
	
	return 0;
}
