#include <fstream>
#include <iostream>
using namespace std;


int mult_table[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

struct Quatr {
	unsigned type;
	short sign;

	Quatr() = default;

	Quatr(const char &c, short sign=1) {
		switch(c) {
			case '1': type = 1; break;
			case 'i': type = 2; break;
			case 'j': type = 3; break;
			case 'k': type = 4; break;
		}
		this->sign = sign;
	}

	Quatr& operator*=(const Quatr& oth) {
		int res_type = mult_table[this->type][oth.type];
		short res_sign = this->sign*oth.sign;
		if(res_type < 0) {
			res_sign = -res_sign;
			res_type = -res_type;
		}
		this->type = res_type;
		this->sign = res_sign;

		return *this;
	}

	Quatr operator*(const Quatr& oth) const {
		Quatr res = *this;
		res *= oth;
		return res;
	}

	bool operator==(const Quatr& oth) const {
		return this->type == oth.type && this->sign == oth.sign;
	}

};

ostream& operator<<(ostream& os, const Quatr& q) {
	if(q.sign < 0) {
		os << '-';
	}
	switch(q.type) {
		case 1: os << '1'; break;
		case 2: os << 'i'; break;
		case 3: os << 'j'; break;
		case 4: os << 'k'; break;
	}
	return os;
}

ifstream in("input");
ofstream out("output");

Quatr last_section[10010];

bool solve(const string& s) {
	Quatr first_section('1');
	for(int i = 0; i < s.size(); ++i) {
		first_section*=Quatr(s[i]);
		if(first_section == Quatr('i')) {
			Quatr second_section('1');
			for(int j = i+1; j < s.size()-1; ++j) {
				second_section*=Quatr(s[j]);
				if(second_section == Quatr('j') && last_section[j+1] == Quatr('k')) {
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int no_cases;
	in >> no_cases;

	for(int t = 1; t <= no_cases; ++t) {
		int l,x;
		in >> l >> x;
		string s;
		in >> s;
		string all_s;
		for(int i = 0; i < x; ++i) {
			all_s += s;
		}

		Quatr curr_value('1');
		for(int i = all_s.size()-1; i >= 0; --i) {
			curr_value = Quatr(all_s[i]) * curr_value;
			last_section[i] = curr_value;
		}
		out << "Case #" << t << ": ";
		if(solve(all_s)) {
			out << "YES";
		}
		else {
			out << "NO";
		}
		out << '\n';
	}
}