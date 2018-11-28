#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

string s;
int gn, gl, gx;

vector<int> table_i;
map<int,char> table_k;
int k_max;

struct Digit
{
	char a;
	int sign;

	Digit() {
		a = '1';
		sign = 1;
	}

	void set(char _a, int _s) {
		a = _a;
		sign = _s;
	}

	bool isEqual(char _t) const {
		return ((sign == 1) && (a == _t));
	}

	void mult(Digit &b)
	{
		if(a == '1') {
			a = b.a;
			sign = (sign * b.sign);
			return;
		}

		if(b.a == '1') {
			a = a;
			sign = (sign * b.sign);
			return;
		}

		if(a == 'i') {
			if(b.a == 'i') {
				a = '1';
				sign = (sign * b.sign * -1);
				return;
			}
			if(b.a == 'j') {
				a = 'k';
				sign = sign * b.sign;
				return;
			}
			a = 'j';
			sign = (sign * b.sign * -1);
			return;
		}

		if(a == 'j') {
			if(b.a == 'i') {
				a = 'k';
				sign = (sign * b.sign * -1);
				return;
			}
			if(b.a == 'j') {
				a = '1';
				sign = (sign * b.sign * -1);
				return;
			}
			a = 'i';
			sign = (sign * b.sign);
			return;
		}

		if(b.a == 'i') {
			a = 'j';
			sign = (sign * b.sign);
			return;
		}
		if(b.a == 'j') {
			a = 'i';
			sign = (sign * b.sign * -1);
			return;
		}

		a = '1';
		sign = (sign * b.sign * -1);
		return;
	}
};

char get(int n)
{
	return s[n % gl];
}

bool make_table_i()
{
	Digit a, b;
	table_i.clear();
	for(int i=0; i<gn; i++) {
		b.set(get(i), 1);
		a.mult(b);
		if(a.isEqual('i'))
			table_i.push_back(i);
	}
	return (table_i.size() > 0);
}

bool make_table_k()
{
	Digit a, b;
	k_max = -1;
	table_k.clear();
	for(int i = (gn-1);i >= 0; i--) {
		a.set(get(i), 1);
		a.mult(b);
		if(a.isEqual('k')) {
			table_k[i] = '1';
		}
		b = a;
	}

	if(table_k.size()) {
		map<int,char>::iterator it = table_k.end();
		it--;
		k_max = it->first;
	}
	return (table_k.size() > 0);
}

bool calc()
{
	int i, j;
	Digit a, b, c, d;

	if(gn == 3) {
		if( (s[0] != 'i') ||
			(s[1] != 'j') ||
			(s[2] != 'k'))
		{
			return false;
		}
		return true;
	}

	int ni = 0, nj = 0, nk = 0;
	for(i=0; i<gl; i++) {
		if(s[i] == 'i')
			ni++;
		else if(s[i] == 'j')
			nj++;
		else
			nk++;
	}

	if( ((ni == 0) && (nj == 0)) ||
		((ni == 0) && (nk == 0)) ||
		((nj == 0) && (nk == 0)))
	{
		return false;
	}

	if( make_table_i() && make_table_k()) {
		int jmax = min(k_max, gn);
		for(i=0; i < table_i.size(); i++) {
			c.set('1', 1);
			for(j = (table_i[i]+1); j < jmax; j++) {
				d.set(get(j), 1);
				c.mult(d);
				if(c.isEqual('j') && (table_k.find(j+1) != table_k.end())) {
					return true;
				}
			}
		}
	}
	return false;
}

void solve(int nCase)
{
	cin >> gl >> gx >> s;
	gn = (gl * gx);
	if((gn > 2) && calc())
		printf("Case #%d: YES\n", nCase);
	else
		printf("Case #%d: NO\n", nCase);
}


int main(int argc, char cargv[])
{
	int n, i;
	// freopen("small.in", "r", stdin);
	
	scanf("%d", &n);
	for(i=0; i<n; i++)
	{
		solve(i+1);
	}
	return 0;
}
