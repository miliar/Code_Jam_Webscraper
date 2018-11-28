#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>

using namespace std;
#define mp(x, y) make_pair(x, y)

#define ttrip int
struct trip {
	ttrip f, s, t;
	trip () {f = s = t = 0;}
	trip (ttrip a, ttrip b, ttrip c) {
		f = a; s = b; t = c;
	}
};

trip gen (char x, int n, string & ans) {
	string s[2];
	s[0].resize(1<<n);
	s[1].resize(1<<n);
	s[0][0] = x;
	int curr = 1;
	for (int i = 0; i < n; i++) {
		int last = 1-curr;
		for (int j = 0; j < 1<<i; j++) {
			if (s[last][j] == 'R') {
				s[curr][2*j] = 'R';
				s[curr][2*j+1] = 'S';
			} else if (s[last][j] == 'P') {
				s[curr][2*j] = 'P';
				s[curr][2*j+1] = 'R';
			} else {
				s[curr][2*j] = 'P';
				s[curr][2*j+1] = 'S';
			}
		}
		curr = last;
	}
	trip cnt;
	ans = s[1-curr];
	for (int i = 0; i < ans.length(); i++) {
		if (ans[i] == 'R')	cnt.f++;
		else if (ans[i] == 'P')	cnt.s++;
		else	cnt.t++;
	}
	return cnt;
}

void swapp (string &s, int beg, int end) {
	int h = (beg+end+1)/2;
	for (int i = beg, j = h; i < h; i++, j++) {
		swap(s[i], s[j]);
	}
}

bool lar(string &s, int beg, int end) {
	int h = (beg+end+1)/2;
	for (int i = beg, j = h; i < h; i++, j++) {
		if (s[i] > s[j])	return true;
	}
	return false;
}

void go(string &s, int beg, int end) {
	//printf ("%d %d\n", beg, end);
	if (beg == end)	return;
	if (beg == end-1) {
		if (s[beg] > s[end])	swap(s[beg], s[end]);
		return;
	}
	int h = (beg+end)/2;
	go (s, beg, h);
	go (s, h+1, end);
	if (lar(s, beg, end))	swapp(s, beg, end);
	return;
}

int main (void) {
	int t;
	scanf ("%d", &t);
	for (int c = 1; c <= t; c++) {
		printf ("Case #%d: ", c);
		int n, r, p, s;
		scanf ("%d%d%d%d", &n, &r, &p, &s);
		string str, stp, sts;
		trip rr = gen('R', n, str);
		trip pp = gen('P', n, stp);
		trip ss = gen('S', n, sts);
		string ans = "";
		if (rr.f == r && rr.s == p && rr.t == s) {
			go(str, 0, str.length()-1);
			if (ans == "")	ans = str;
			ans = min(ans, str);
		}
		if (pp.f == r && pp.s == p && pp.t == s) {
			go(stp, 0, stp.length()-1);
			if (ans == "")	ans = stp;
			ans = min(ans, stp);
		}
		if (ss.f == r && ss.s == p && ss.t == s) {
			go(sts, 0, sts.length()-1);
			if (ans == "")	ans = sts;
			ans = min(ans, sts);
		}
		if (ans == "") {
			printf ("IMPOSSIBLE\n");
		} else {
			printf ("%s\n", ans.c_str());
		}

	}
}