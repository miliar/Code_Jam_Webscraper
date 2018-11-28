#include <stdio.h>
#include <vector>

unsigned int popcount(unsigned int bits)
{
    bits = (bits & 0x55555555) + (bits >> 1 & 0x55555555);
    bits = (bits & 0x33333333) + (bits >> 2 & 0x33333333);
    bits = (bits & 0x0f0f0f0f) + (bits >> 4 & 0x0f0f0f0f);
    bits = (bits & 0x00ff00ff) + (bits >> 8 & 0x00ff00ff);
    return (bits & 0x0000ffff) + (bits >>16 & 0x0000ffff);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int J, P, S, K;
		scanf("%d%d%d%d", &J, &P, &S, &K);
		std::vector<std::vector<int> > pair;
		for (int i=0; i<J; i++) {
			for (int j=0; j<P; j++) {
				std::vector<int> p;
				p.push_back(i);
				p.push_back(j);
				p.push_back(-1);
				pair.push_back(p);
			}
		}
		for (int i=0; i<P; i++) {
			for (int j=0; j<S; j++) {
				std::vector<int> p;
				p.push_back(-1);
				p.push_back(i);
				p.push_back(j);
				pair.push_back(p);
			}
		}
		for (int i=0; i<J; i++) {
			for (int j=0; j<S; j++) {
				std::vector<int> p;
				p.push_back(i);
				p.push_back(-1);
				p.push_back(j);
				pair.push_back(p);
			}
		}
		std::vector<unsigned int> pat;
		pat.resize(pair.size());
		for (int i=0; i<J*P*S; i++) {
			int j0 = i/(P*S);
			int p0 = i%(P*S)/S;
			int s0 = i%S;
			for (int j=0; j<(int)pair.size(); j++) {
				if (pair[j][0] < 0 || pair[j][0] == j0) {
					if (pair[j][1] < 0 || pair[j][1] == p0) {
						if (pair[j][2] < 0 || pair[j][2] == s0) {
							pat[j] |= (1<<i);
						}
					}
				}
			}
		}
		int res = 0;
		int cur = 0;
		for (unsigned int bit = 0; bit<(1<<(J*P*S)); bit++) {
			if ((int)popcount(bit) <= res) {
				continue;
			}
			/*
			if (J==3) {
				unsigned int shift = P*S;
				unsigned int mask = (1<<shift)-1;
				if ((bit&mask) > ((bit>>shift)&mask)) {
					continue;
				}
				if (((bit>>shift)&mask) > ((bit>>(shift*2))&mask)) {
					continue;
				}
			}
			*/
			bool flg = true;
			for (int i=0; i<(int)pat.size(); i++) {
				if (popcount(bit&pat[i]) > K) {
					flg = false;
					break;
				}
			}
			if (flg) {
				res = (int)popcount(bit);
				cur = bit;
			}
		}
		printf("Case #%d: %d\n", t, res);
		for (int i=0; i<J*P*S; i++) {
			if (cur & (1<<i)) {
				printf("%d %d %d\n", i/(P*S) + 1, i%(P*S)/S + 1, i%S + 1);
			}
		}
	}
	return 0;
}
