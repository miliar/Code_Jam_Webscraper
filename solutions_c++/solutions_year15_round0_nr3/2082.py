#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

struct smth {
	char st;
	bool neg;
	smth(){};

	smth(char a){
		st = a;
		neg = false;
	}

	smth operator * (smth b) {
		smth n;
		if ((b.neg && !neg) || (neg && !b.neg)) {
			n.neg = true;
		} else {
			n.neg = false;
		}

		if (st == '1') {
			n.st = b.st;
			return n;
		}
		if (b.st == '1') {
			n.st = st;
			return n;
		}
		
		if (st == b.st) {
			n.neg = !n.neg;
			n.st = '1';
			
		}
		if (st == 'i' && b.st == 'j') 
			n.st = 'k';
		
		if (st == 'i' && b.st == 'k') {
			n.st = 'j';
			n.neg = !n.neg;
		}
		
		if (st == 'j' && b.st == 'i') {
			n.st = 'k';
			n.neg = !n.neg;
		}
		if (st == 'j' && b.st == 'k') 
			n.st = 'i';
		
		if (st == 'k' && b.st == 'i')
			n.st = 'j';
		
		if (st == 'k' && b.st == 'j') {
			n.neg = !n.neg;
			n.st = 'i';
		}
		return n;
	}
	
};

string s1, s;
smth suff[10010];

bool try_split(int x) {
	smth curr(s[x]);
	for (int i = x + 1; i < (int)s.size()- 1; i++) {
		if (curr.st == 'j' && !curr.neg) {
			if (suff[i].st == 'k' && !suff[i].neg) {
				return true;
			}
		}
		smth tmp(s[i]);
		curr = curr * tmp;
	}
	if (curr.st == 'j' && !curr.neg) {
		if (suff[s.size() - 1].st == 'k' && !suff[s.size() - 1].neg) {
			return true;
		}
	}
	return false;
}

bool solve() {
	smth curr(s[0]);
	
	for (int i = 1; i < (int)s.size()- 2; i++) {
		if (curr.st == 'i' && !curr.neg) {
			if (try_split(i))
				return true;
		}
		smth tmp(s[i]);
		curr = curr * tmp;
	}
	if (curr.st == 'i' && !curr.neg) {
		if (try_split(s.size() - 2))
			return true;
	}
	return false;
}

void precalc() {
	for (int i = s.size() - 1; i > - 1; i--) {
		if (i + 1 == (int)s.size()) {
			suff[i] = smth(s[i]);
		} else {
			smth tmp(s[i]);
			suff[i] = tmp * suff[i + 1];
		}
	}
}

int n, l, x;

int main() {
	cin >> n;
	for (int i = 0; i< n; i++){
		cin >> l >> x;
		cin >> s1;
		s = "";
		for (int j = 0; j < x; j++) {
			s += s1;
		}
		precalc();
		if (s.size() > 1 && solve())
			cout << "Case #" << i + 1 << ": YES" << endl;
		else
			cout << "Case #" << i + 1 << ": NO" << endl;
	}
	return 0;
}
