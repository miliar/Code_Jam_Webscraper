#include<stdio.h>
#include<algorithm>
using namespace std;

int nCase;
long long L, X;
char S[10008], pre[10008], suf[10008];

inline char mul(char a, char b) {
	bool s = (a<0) ^ (b<0);
	a = abs(a), b = abs(b);
	char r;
	if(a == '1') r = b;
	else if(b == '1') r = a;
	else if(a == b) r = '1', s = !s;
	else r = 'i'+'j'+'k'-a-b, s ^= (a==b-2 || a==b+1);
	return s ? -r : r;
}

inline char power(char a, int n) {
	if(n <= 1) return n ? a : '1';
	char h = power(a, n>>1);
	h = mul(h, h);
	return (n&1) ? mul(h, a) : h;
}

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%lld %lld %s", &L, &X, S);
		printf("Case #%d: ", cs);
		pre[0] = S[0];
		for(int i = 1; i < L; ++i) pre[i] = mul(pre[i-1], S[i]);
		suf[L-1] = S[L-1];
		for(int i = L-2; i >= 0; --i) suf[i] = mul(S[i], suf[i+1]);
		char all = suf[0];
		/*for(int i = 0; i < L; ++i) fprintf(stderr, " %d", pre[i]);
		fprintf(stderr, "\n");
		for(int i = 0; i < L; ++i) fprintf(stderr, " %d", suf[i]);
		fprintf(stderr, "\n");
		fprintf(stderr, "power %d %d %d\n", all, X, power(all,X));*/

		if(power(all, X) != -'1') {
			puts("NO");
			continue;
		}
		long long ilen = L*(long long)X, klen = L*(long long)X;
		for(int i = 0; i < L; ++i) {
			for(char j = 0, c = pre[i]; j < 4; ++j, c = mul(all, c))
				if(c == 'i') ilen = min(ilen, i+1+j*L);
			for(char j = 0, c = suf[i]; j < 4; ++j, c = mul(c, all))
				if(c == 'k') klen = min(klen, j*L+L-i);
		}
		//fprintf(stderr, "ilen %lld, klen %lld\n", ilen, klen);
		if(ilen+klen <= L*(long long)X) puts("YES");
		else puts("NO");
	}
}


