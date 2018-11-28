#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct Q {
	char c;
	int sign;
};


Q calc(Q q1, Q q2) {
	Q res;
	switch(q1.c) {
	case '1':
		res.c = q2.c;
		res.sign = q1.sign * q2.sign;
		break;
	case 'i':
		switch(q2.c) {
		case '1':
			res.c = q1.c;
			res.sign = q1.sign * q2.sign;
			break;
		case 'i':
			res.c = '1';
			res.sign = q1.sign * q2.sign * -1;
			break;
		case 'j':
			res.c = 'k';
			res.sign = q1.sign * q2.sign;
			break;
		case 'k':
			res.c = 'j';
			res.sign = q1.sign * q2.sign * -1;
			break;
		}
		break;
	case 'j':
		switch(q2.c) {
		case '1':
			res.c = q1.c;
			res.sign = q1.sign * q2.sign;
			break;
		case 'i':
			res.c = 'k';
			res.sign = q1.sign * q2.sign * -1;
			break;
		case 'j':
			res.c = '1';
			res.sign = q1.sign * q2.sign * -1;
			break;
		case 'k':
			res.c = 'i';
			res.sign = q1.sign * q2.sign;
			break;
		}
		break;
	case 'k':
		switch(q2.c) {
		case '1':
			res.c = q1.c;
			res.sign = q1.sign * q2.sign;
			break;
		case 'i':
			res.c = 'j';
			res.sign = q1.sign * q2.sign;
			break;
		case 'j':
			res.c = 'i';
			res.sign = q1.sign * q2.sign * -1;
			break;
		case 'k':
			res.c = '1';
			res.sign = q1.sign * q2.sign * -1;
			break;
		}
		break;
	}
	return res;
}



bool solve() {
	int L;
	int X;
	char s[10000 * 10 + 1] = {0, };

	scanf("%d %d", &L, &X);
	scanf("%s", s);

//	printf("%s\n", s);

	Q q;
	q.c = '1';
	q.sign = 1;

	for (int i=0; i<L; i++) {
		Q q2;
		q2.c = s[i];
		q2.sign = 1;
		q = calc(q, q2);
	}

//	printf("%c : %d\n", q.c, q.sign);

	Q q1 = q;

	q.c = '1';
	q.sign = 1;

	for (int i=0; i<X; i++) {
		q = calc(q, q1);
	}

//	printf("%c : %d\n", q.c, q.sign);

	if (!(q.c=='1' && q.sign == -1))
		return false;


	for (int i=0; i < min(X, 10); i++)
		memcpy(s + (L*i), s, L);

	bool fi = false;
	bool fj = false;
	bool fk = false;

	q.c = '1';
	q.sign = 1;
	int bi = 0;
	for (int i=0; i<L*min(X, 10); i++) {
		Q q2;
		q2.c = s[i];
		q2.sign = 1;
		q = calc(q, q2);
//		printf("(%c %d) ", q.c, q.sign);
		if (q.c == 'i' && q.sign == 1) {
			fi = true;
			bi = i+1;
			break;
		}
	}

	if (!fi) return false;

	q.c = '1';
	q.sign = 1;
	for (int i=bi; i<L*min(X, 10); i++) {
		Q q2;
		q2.c = s[i];
		q2.sign = 1;
		q = calc(q, q2);
//		printf("(%c %d) ", q.c, q.sign);
		if (q.c == 'j' && q.sign == 1) {
			fj = true;
			bi = i+1;
			break;
		}
	}

	if (!fj) return false;

	q.c = '1';
	q.sign = 1;
	for (int i=L*min(X, 10)-1; i>=bi; i--) {
		Q q2;
		q2.c = s[i];
		q2.sign = 1;
		q = calc(q2, q);
//		printf("(%c %d) ", q.c, q.sign);
		if (q.c == 'k' && q.sign == 1) {
			fk = true;
			break;
		}
	}

	return (fk);
}

int main() {

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int i=1; i<=T; i++) {
		if (solve())
			printf("Case #%d: YES\n", i);
		else
			printf("Case #%d: NO\n", i);
	}



	fclose (stdout);
	fclose (stdin);

	return 0;
}
