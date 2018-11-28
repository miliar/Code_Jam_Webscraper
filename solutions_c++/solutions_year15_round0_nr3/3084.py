// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <cassert>

using namespace std;

struct q {
	int s;
	char c;
};

q m(q q1, q q2)
{
	q r;
	r.s = q1.s * q2.s;
	if (q1.c == '1')
		r.c = q2.c;
	else if (q2.c == '1')
		r.c = q1.c;
	else if (q1.c == q2.c) {
		r.s *= -1;
		r.c = '1';
	}
	else {
		r.c = 'i' + 'j' + 'k' - q1.c - q2.c;
		if (!(q1.c + 1 == q2.c || q1.c - 2 == q2.c))
			r.s *= -1;
	}
	return r;
}

bool is_minus_one(q q) { return q.s == -1 && q.c == '1'; }
bool is_i(q q) { return q.s == 1 && q.c == 'i'; }
bool is_k(q q) { return q.s == 1 && q.c == 'k'; }

q of_char(char c) { q r; r.s = 1; r.c = c; return r; }
q one() { return of_char('1'); }

string solve()
{
	int l, x; cin >> l >> x;
	string b; cin >> b;
	if (b.size() != l) exit(-1);
	string s;
	for (auto i = 0; i < x; ++i)
		s += b;
	auto p = one();
	for (auto c : s)
		p = m(p, of_char(c));
	if (!is_minus_one(p)) return "NO";
	int first_i = 0;
	p = one();
	int n = s.size();
	if (n != l * x) exit(-1);
	while (first_i < n) {
		p = m(p, of_char(s[first_i]));
		if (is_i(p)) break;
		++first_i;
	}
	if (first_i == n) return "NO";
	int last_k = n - 1;
	p = one();
	while (last_k >= 0) {
		p = m(of_char(s[last_k]), p);
		if (is_k(p)) break;
		--last_k;
	}
	if (last_k <= first_i + 1) return "NO";
	return "YES";
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t; cin >> t;
	for (auto q = 1; q <= t; ++q)
		cout << "Case #" << q << ": " << solve() << endl;
	return 0;
}

