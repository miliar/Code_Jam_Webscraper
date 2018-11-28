#include<iostream>
#include<fstream>
#include<cmath>
#include<ctime>
using namespace std;

//i->2 j->3 k->4

int pre[10001];
int suf[10001];
string s;


inline int mul_pos(int a, int b) {
	if(a == 1 || b == 1) return a*b;
	if(a == b) return -1;
	if(a == 2 && b == 3) return 4;
	if(a == 3 && b == 2) return -4;
	if(a == 2 && b == 4) return -3;
	if(a == 4 && b == 2) return 3;
	if(a == 3 && b == 4) return 2;
	if(a == 4 && b == 3) return -2;
}

inline int mul(int a, int b) {
	if((a > 0) == (b > 0)) return mul_pos(abs(a),abs(b));
	else return mul_pos(abs(a),abs(b)) * -1;
}

inline int con(char c) {
	if(c == 'i') return 2;
	if(c == 'j') return 3;
	if(c == 'k') return 4;
}

inline bool exist(int l){
	for(int a = 0; a < l-2; ++a)
		if(pre[a] == 2)
			for(int b = a+2; b < l; ++b)
				if(suf[b] == 4)
					if(pre[b-1] == 4)
						return 1;
	return 0;
}

int main() {
	int t,l,x;
	string tmp;
	fstream in;
	fstream f;
	in.open("input.txt");
	f.open("ansC.txt");
	in >> t;
	clock_t time = clock();
	for(int c = 1; c <= t; ++c) {
		in >> l >> x >> s;
		tmp = s;
		for(int i = 1; i < x; ++i)
			s += tmp;
		l *= x;
		pre[0] = con(s[0]);
		for(int i = 1; i < l; ++i)
			pre[i] = mul(pre[i-1], con(s[i]));
		suf[l-1] = con(s[l-1]);
		for(int i = l-2; i >= 0; --i)
			suf[i] = mul(con(s[i]), suf[i+1]);
		if(exist(l))
			f << "Case #" << c << ": Yes\n";
		else
			f << "Case #" << c << ": No\n";
		cout << "Case " << c <<" finished took " << (clock() - time)/(double)CLOCKS_PER_SEC << " seconds\n";
	}
	f.close();
	return 0;
}
