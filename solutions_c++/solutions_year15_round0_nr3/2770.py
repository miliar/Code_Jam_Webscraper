#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#define ll long long

enum lul {
	one, i, j, k, mone, mi, mj, mk
};

unordered_set<lul> neg{ mone, mi, mj, mk };
unordered_map<lul, lul> m{ { one, mone }, { mone, one }, { i, mi }, { mi, i }, { j, mj }, { mj, j }, { k, mk }, { mk, k } };
unordered_map<char, lul> conv{ { 'i', i }, { 'j', j }, { 'k', k } };

lul lookup[4][4] = { { one, i, j, k }, { i, mone, k, mj }, { j, mk, mone, i }, { k, j, mi, mone } };
string print[8] = { "1", "i", "j", "k", "-1", "-i", "-j", "-k" };
lul givesi[8] = { i, one, k, mj, mi, mone, mk, j };
lul givesj[8] = { j, mk, one, i, mj, k, mone, mi };

lul operator*(lul l1, lul l2) {
	bool isneg = neg.count(l1) ^ neg.count(l2);
	lul l1p = neg.count(l1) ? m[l1] : l1;
	lul l2p = neg.count(l2) ? m[l2] : l2;
	return isneg ? m[lookup[l1p][l2p]] : lookup[l1p][l2p];
}

lul powl(lul l, ll p) {
	if (l == one) return l;
	if (l == mone) return p & 1l ? mone : one;

	if (p % 4 == 0)
		return one;
	if (p % 4 == 1)
		return l;
	if (p % 4 == 2)
		return mone;
	if (p % 4 == 3)
		return m[l];
}



int main() {

	ofstream cout("out.txt");
	ifstream cin("in.in");

	int T;
	cin >> T;
	for (int idx = 1; idx <= T; idx++) {
		int L, X;
		cin >> L >> X;
		lul prod = one;
		
		
		string s;
		cin >> s;
		unordered_map<lul, ll> firstof;

		for (ll c = 0; c < s.size(); c++) {
			prod = prod * conv[s[c]];
			if (firstof.count(prod) == 0)
				firstof[prod] = c;
		}
		if (powl(prod, X) != mone) {
			cout << "Case #" << idx << ": NO" << endl;
			continue;
		}
		int level = 0;
		int indexi = firstof.count(i) ? firstof[i] : -1;
		lul now = one;
		if (firstof.count(i) == 0) {
			
			for (int a = 0; a < 4; a++) {
				level++;
				now = now * prod;
				if (firstof.count(givesi[now])) {
					indexi = level*L + firstof[givesi[now]];
					break;
				}
			}
			
			
		}
		if (indexi == -1) {
			cout << "Case #" << idx << ": NO" << endl;
			continue;
		}
		lul partial = one;
		bool done = false;
		for (ll p = indexi - level*L + 1; p < s.size(); p++) {
			partial = partial * conv[s[p]];
			if (partial == j) {
				done = true;
				break;
			}
		}
		if (done) {
			cout << "Case #" << idx << ": YES" << endl;
			continue;
		}

		
		
		int indexj = -1;
		now = partial;
		
		for (int a = 0; a < 4; a++) {
			level++;	
			if (firstof.count(givesj[now])) {
				indexj = level*L + firstof[givesj[now]];
				break;
			}
			now = now * prod;
		}

		if (indexj != -1 && indexj < L*X) 
			cout << "Case #" << idx << ": YES" << endl;
		else
			cout << "Case #" << idx << ": NO" << endl;
		
	}

}