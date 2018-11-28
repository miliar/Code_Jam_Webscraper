#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

class Q {
public:
	enum Part {R = 0, I = 1, J = 2, K = 3};
	static Q table[4][4];
	Part part;
	int sign;

	Q(Part p = R, int s = 1)
	{
		part = p;
		sign = s;
	}

	Q operator*(const Q& other) const
	{
		Q q = table[part][other.part];
		q.sign *= sign * other.sign;
		return q;
	}
	
	Q operator^(unsigned long long n) const
	{
		Q res;
		Q cur = *this;
		for (int i=0; (1ULL<<i)<=n; i++) {
			if (n & (1ULL<<i)) {
				res = res * cur;
			}
			cur = cur * cur;
		}
		return res;
	}
};

Q
Q::table[4][4] = {
	Q(R, 1), Q(I, 1), Q(J, 1), Q(K, 1),
	Q(I, 1), Q(R, -1), Q(K, 1), Q(J, -1),
	Q(J, 1), Q(K, -1), Q(R, -1), Q(I, 1),
	Q(K, 1), Q(J, 1), Q(I, -1), Q(R, -1)
};

Q seq[20000];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int L;
		unsigned long long X;
		scanf("%d", &L);
		scanf("%llu", &X);
		Q cur;
		for (int i=0; i<L; i++) {
			char c;
			scanf(" %c", &c);
			if (c == 'i') {
				seq[i] = Q(Q::I);
			} else if (c == 'j') {
				seq[i] = Q(Q::J);
			} else {
				seq[i] = Q(Q::K);
			}
			cur = cur * seq[i];
		}
		cur = cur^X;
		const char* res = "NO";
		if (cur.part == Q::R && cur.sign == -1) {
			cur = Q();
			int step = 0;
			int cnt = 0;
			bool end = false;
			for (unsigned long long i=0; i<X && !end; i++) {
				for (int j=0; j<L && !end; j++) {
					cur = cur * seq[j];
					if (step == 0 && cur.part == Q::I && cur.sign == 1) {
						cur = Q();
						cnt = 0;
						step = 1;
					}
					if (step == 1 && cur.part == Q::J && cur.sign == 1) {
						step = 2;
						end = true;
					}
					if (cnt > L*16) {
						end = true;
					}
					cnt++;
				}
			}
			if (step == 2) {
				res = "YES";
			}
		}
		printf("Case #%d: %s\n", t, res);
	}

	return 0;
}