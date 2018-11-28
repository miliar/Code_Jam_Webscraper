#include <fstream>
#include <string>
#include <vector>

long T, l, x;

struct number{
	char sign;
	char c;
	number() : sign('+'), c('1') {}
	number(char c) : sign('+'), c(c) {}
	number(char sign, char c) : sign(sign), c(c) {}
	number(const number &n) : sign(n.sign), c(n.c) {}
	
	bool operator ==(const number &n) const{
		return sign == n.sign && c == n.c;
	}
};
std::string buf, s;

number y[] = {
	number('+', '1'), number('+', 'i'), number('+', 'j'), number('+', 'k'),
	number('+', 'i'), number('-', '1'), number('+', 'k'), number('-', 'j'),
	number('+', 'j'), number('-', 'k'), number('-', '1'), number('+', 'i'),
	number('+', 'k'), number('+', 'j'), number('-', 'i'), number('-', '1'),
};

const number c1('1');
const number ci('i');
const number cj('j');
const number ck('k');

/*std::string p[] =  { 
	"+1", "+i", "+j", "+k",
	"+i", "-1", "+k", "-j",
	"+j", "-k", "-1", "+i",
	"+k", "+j", "-i", "-1", 
} ;*/

number mult(const number &a, const number &b){
	int c, d;
	if (a.c == '1') c = 0; else
 	if (a.c == 'i') c = 4; else 
	if (a.c == 'j') c = 8; else 
	if (a.c == 'k') c = 12;

	if (b.c == '1') d = 0; else 
	if (b.c == 'i') d = 1; else 
	if (b.c == 'j') d = 2; else 
	if (b.c == 'k') d = 3;

	number r;
	if (a.sign == b.sign) r.sign = '+'; else r.sign = '-';
	if (r.sign == y[c + d].sign) r.sign = '+'; else r.sign = '-';
	r.c = y[c + d].c;
	return r;
}

bool solve(const std::string &s){
	number a, b;
	std::vector<number> m(s.length() + 1);
	for (int i = s.length() - 1; i >= 0; --i) m[i] = mult(number(s[i]), m[i + 1]);

	for (int i = 0; i < s.length(); ++i){
		a = mult(a, number(s[i]));
		if (a == ci){
			b = number();
			for (int j = i + 1; j < s.length(); ++j){
				b = mult(b, number(s[j]));
				if (b == cj){
					if (m[j + 1] == ck){
						return true;
					}
				}
			}
		}
	}
	return false;
}

int main() {
	std::ifstream in(".in");
	std::ofstream out(".out");

	in >> T;

	for (int t = 1; t <= T; ++t){
		in >> l >> x;
		in >> buf;
		s = "";
		for (int i = 0; i < x; ++i) s += buf;
		if (solve(s)){
			out << "Case #" << t << ": " << "YES" << std::endl;
		}
		else {
			out << "Case #" << t << ": " << "NO" << std::endl;
		}
	}

	in.close();
	out.close();
	return 0;
}