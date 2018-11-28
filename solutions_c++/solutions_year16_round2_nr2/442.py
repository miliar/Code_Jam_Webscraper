#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <time.h>
using namespace std;

typedef long long ll;

#define labs(a) ((a)<0?-(a):(a))

string a, b;
int n;

void sol (int ind, int fl) {
	if (ind == n) {
		return;
	}

	if (a[ind] != '?' && b[ind] != '?') {
		if (fl) {
			sol (ind+1, fl);
		} else if (a[ind] == b[ind]) {
			sol (ind+1, 0);
		} else if (a[ind] < b[ind]) {
			sol (ind+1, 1);
		} else {
			sol (ind+1, 2);
		}
	} else if (b[ind] != '?') {
		if (!fl) {
			a[ind] = b[ind];
			sol(ind+1, fl);
		} else if (fl == 1) {
			a[ind] = '9';
			sol(ind+1, fl);
		} else {
			a[ind] = '0';
			sol(ind+1, fl);
		}
	} else if (a[ind] != '?') {
		if (!fl) {
			b[ind] = a[ind];
			sol (ind+1, fl);
		} else if (fl == 1) {
			b[ind] = '0';
			sol(ind+1, fl);
		} else {
			b[ind] = '9';
			sol(ind+1, fl);
		}
	} else {
		if (!fl) {
			b[ind] = a[ind] = '0';
			sol (ind+1, fl);
		} else if (fl == 1) {
			a[ind] = '9';
			b[ind] = '0';
			sol (ind+1, fl);
		} else {
			a[ind] = '0';
			b[ind] = '9';
			sol (ind+1, fl);
		}
	}

	return;
}

ll val (string x) {
	ll ret = 0;
	for (int i=0;i<x.size();i++) {
		ret *= 10LL;
		ret += (ll)(x[i]-'0');
	}
	return ret;
}

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);

	int t;
	scanf ("%d", &t);

	for (int it=1;it<=t;it++) {
		printf ("Case #%d: ", it);

		cin >> a >> b;
		n = a.size();

		string ba, bb, ta, tb;
		ll best = 1LL<<62;
		int bigfl = 0;
		for (int i=0;i<n;i++) {
			if (a[i] != '?' && b[i] != '?') {
				if (!bigfl && a[i] < b[i]) {
					bigfl = 1;
				} else if (!bigfl && a[i] > b[i]) {
					bigfl = 2;
				}
			} else if (b[i] != '?') {
				ta = a;
				tb = b;
				for (char ca = '0';ca<='9';ca++) {
					a = ta;
					b = tb;
					a[i] = ca;
					sol (i+1, bigfl?bigfl:(a[i]==b[i]?0:(a[i]<b[i]?1:2)));
					ll va, vb;
					va = val(a);
					vb = val(b);
					if (labs(va-vb) < best) {
						best = labs(va-vb);
						ba = a;
						bb = b;
					} else if (labs(va-vb) == best) {
						if (ba > a) {
							ba = a;
							bb = b;
						} else if (ba == a) {
							bb = min (bb, b);
						}
					}
					//cout << ca << " " << a << " " << b << " " << labs(va-vb) << " " << best << endl;
					
				}
				a = ta;
				b = tb;
				a[i] = b[i];
			} else if (a[i] != '?') {
				ta = a;
				tb = b;
				for (char cb = '0';cb<='9';cb++) {
					a = ta;
					b = tb;
					b[i] = cb;
					sol (i+1, bigfl?bigfl:(a[i]==b[i]?0:(a[i]<b[i]?1:2)));
					ll va, vb;
					va = val(a);
					vb = val(b);
					if (labs(va-vb) < best) {
						best = labs(va-vb);
						ba = a;
						bb = b;
					} else if (labs(va-vb) == best) {
						if (ba > a) {
							ba = a;
							bb = b;
						} else if (ba == a) {
							bb = min (bb, b);
						}
					}
				}
				a = ta;
				b = tb;
				b[i] = a[i];
			} else {
				ta = a;
				tb = b;
				for (char ca = '0';ca<='9';ca++) {
					for (char cb = '0';cb<='9';cb++) {
						a = ta;
						b = tb;
						a[i] = ca;
						b[i] = cb;
						sol (i+1, bigfl?bigfl:(a[i]==b[i]?0:(a[i]<b[i]?1:2)));
						ll va, vb;
						va = val(a);
						vb = val(b);
						if (labs(va-vb) < best) {
							best = labs(va-vb);
							ba = a;
							bb = b;
						} else if (labs(va-vb) == best) {
							if (ba > a) {
								ba = a;
								bb = b;
							} else if (ba == a) {
								bb = min (bb, b);
							}
						}
					}
				}
				a = ta;
				b = tb;
				a[i] = b[i] = '0';
			}
			//cout << a << " " << b << " " << best << " " << ba << " " << bb << endl;
		}
		cout << ba << " " << bb << endl;
	}
	return 0;
}