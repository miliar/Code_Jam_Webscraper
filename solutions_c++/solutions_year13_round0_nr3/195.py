// Run commented gen() to precompute list of palindromic square-roots
// Comment gen() to solve input
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
#include <cstdio>
#define MAXD 105
using namespace std;
FILE* fout;
struct BigNum {
	int A[MAXD];
	int len;
	void init(int n) {
		memset(A,0,sizeof(A));
		len = n;
	}
	void getlen() {
		for(int i=MAXD-1;i>=0;--i)
			if(A[i]) {
				len = i+1;
				return;
			}
	}
	void add1() {
		int carry = 1;
		for(int i=0;i<MAXD;++i) {
			A[i] += carry;
			if(A[i] >= 2) {
				A[i] = 0;
				carry = 1;
			}
			else break;
		}
		getlen();
	}
	void print() {
		for(int i=len-1;i>=0;--i) fprintf(fout,"%d",A[i]);
		fprintf(fout,"\n");
	}
	void copy(char* str) {
		init(strlen(str));
		for(int i=0;i<len;++i)
			A[i] = str[len-1-i]-'0';
	}
} D, nD, nD2, L[50005], upper, lower;
int li;
void square(BigNum& d,BigNum &res) {
	res.init(d.len);
	for(int i=0;i<d.len;++i)
		for(int j=0;j<d.len;++j)
			res.A[i+j] += d.A[i]*d.A[j];
	int carry = 0;
	for(int i=0;i<MAXD;++i) {
		res.A[i] += carry;
		carry = res.A[i]/10;
		res.A[i] %= 10;
	}
	res.getlen();
}
bool ispal(BigNum& B) {
	for(int i=0;i<B.len/2;++i)
		if(B.A[i] != B.A[B.len-1-i]) return 0;
	return 1;
}
void gen() {
	fout = fopen("c.data","w");
	fprintf(fout,"1\n2\n3\n");
	for(int n=1;n<=25;++n) {
		printf("n=%d\n",n);
		D.init(n);
		D.A[n-1] = 1;
		nD.init(n+n);
		while(D.len == n) {
			// append its reverse
			for(int i=0;i<n;++i)
				nD.A[i] = nD.A[nD.len-1-i] = D.A[n-1-i];
			square(nD,nD2);
			if(ispal(nD2)) nD.print();
			D.add1();
		}
		nD.init(n+n);
		nD.A[0] = nD.A[nD.len-1] = 2;
		nD.print();
		if(n == 25) continue;
		D.init(n);
		D.A[n-1] = 1;
		nD.init(n+n+1);
		while(D.len == n) {
			// odd digits
			for(int i=0;i<n;++i)
				nD.A[i] = nD.A[nD.len-1-i] = D.A[n-1-i];
			for(int i=0;i<3;++i) {
				nD.A[n] = i;
				square(nD,nD2);
				if(ispal(nD2)) nD.print();
			}
			D.add1();
		}
		// 20000...
		nD.init(n+n+1);
		nD.A[0] = nD.A[nD.len-1] = 2;
		nD.print();
		nD.A[n] = 1;
		nD.print();
	}
	exit(0);
}
bool isgreater(BigNum& a,BigNum& b) {
	for(int i=MAXD-1;i>=0;--i)
		if(a.A[i] != b.A[i]) return a.A[i] > b.A[i];
	return 0;
}
int count(BigNum& a) {
	int lo = -1, hi = li-1;
	while(lo < hi) {
		int m = (lo+hi+1)/2;
		square(L[m],D);
		if(isgreater(D,a)) hi = m-1;
		else lo = m;
	}
	return lo+1;
}
int main() {
	int T;
//	gen();
	// read bignums
	FILE* fin = fopen("c.data","r");
	char str[MAXD];
	while(fscanf(fin,"%s",str) == 1) {
		L[li].copy(str);
		++li;
	}
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		char a[105], b[105];
		scanf("%s%s",a,b);
		lower.copy(a);
		upper.copy(b);
		int c = count(upper);
		int d = count(lower);
		if(d) {
			square(L[d-1],D);
			if(!isgreater(D,lower) && !isgreater(lower,D))
				--d; // don't count last guy
		}
		printf("Case #%d: %d\n",cn,c-d);
	}
}
