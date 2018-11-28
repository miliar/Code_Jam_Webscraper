#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<iostream>

using namespace std;

#define ll long long
#define EPS 1e-5

char sA[200],sB[200];
double dA, dB;
ll lA, lB;

int T,cs;
int num[200], n;
int o2o[200][200];
int t0t[200][200];
int t1t[200][200];
ll dp[111][2][3];
ll pals[200];

int cmp(int a[], int b[], int sz) {
	for(int i=0;i<sz;++i)
		if(a[i] < b[i]) return 0;
		else if(a[i] > b[i]) return 2;
	return 1;
}

ll go(int pos, bool head, int tail) {
	if(pos == n / 2) {
		if(n % 2 == 0) {
			if(head | (tail != 2)) return 1;
			else return 0;
		}
		else {
			if(head | (tail != 2)) return min(num[pos]+1,3);
			else return 0;
		}
	}

	ll &ret = dp[pos][head][tail];
	if(ret != -1) return ret;
	ret = 0;

	int ntail = tail;
	for(int i=0;i<2;++i)
		if(head) {
			if(i > num[n-1-pos]) ntail = 2;
			else if(i == num[n-1-pos]) {
				if(tail == 0) ntail = 0;
				else ntail = 1;
			}
			else {
				ntail = 0;
			}
			ret += go(pos + 1, 1, ntail);
		}
		else if(i <= num[pos]) {
			if(i > num[n-1-pos]) ntail = 2;
			else if(i == num[n-1-pos]) {
				if(tail == 0) ntail = 0;
				else ntail = 1;
			}
			else {
				ntail = 0;
			}
			ret += go(pos + 1, i < num[pos], ntail);
		}
	return ret;
}

ll calc() {
	if(n == 0) return 0;
	if(n == 1) {
		if(num[0] >= 3) return 3;
		else if(num[0] == 2) return 2;
		else if(num[0] == 1) return 1;
		else return 0;
	}


	ll ret = 0;
	for(int i=1;i<n;++i) ret += pals[i];
	memset(dp,-1,sizeof(dp));

	int tail;
	if(1 > num[n-1]) tail = 2;
	else if(1 == num[n-1]) tail = 1;
	else tail = 0;
	ret += go(1,1 < num[0],tail);
	if(n % 2 == 0) {
		int c = cmp(num,t0t[n],n);
		if(c != 0) ret++;
	}
	else {
		int c = cmp(num,t0t[n],n);
		if(c != 0) ret++;
		c = cmp(num,t1t[n],n);
		if(c != 0) ret++;
		c = cmp(num,o2o[n],n);
		if(c != 0) ret--;
	} return ret;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	pals[1] = 3;
	for(int i=2;i<=100;++i)
		if(i % 2 == 0)
			pals[i] = (1ll<<(i/2-1)) + 1;
		else
			pals[i] = (1ll<<(i/2-1)) * 3 + 2;

	for(int len=2;len<=100;++len) {
		if(len % 2 == 0) {
			t0t[len][0] = 2, t0t[len][len-1] = 2;
		}
		else {
			t0t[len][0] = 2, t0t[len][len-1] = 2;
			t1t[len][0] = 2, t1t[len][len/2] = 1, t1t[len][len-1] = 2;
			for(int i=0;i<len;++i)
				o2o[len][i] = 1;
			o2o[len][len/2] = 2;
		}
	}

	scanf("%d",&T);
	for(cs=1;cs<=T;++cs) {
		scanf("%s %s",sA, sB), dA = dB = 0;
		for(int i=0;i<strlen(sA);++i) dA *= 10, dA += sA[i] - '0';
		for(int i=0;i<strlen(sB);++i) dB *= 10, dB += sB[i] - '0';
		dA--;
		lA = sqrt(dA) + EPS;
		lB = sqrt(dB) + EPS;

		ll X = 0, Y = 0;

		n = 0;
		while(lA) num[n++] = lA % 10, lA /= 10;
		reverse(num,num+n);
		X = calc();

		n = 0;
		while(lB) num[n++] = lB % 10, lB /= 10;
		reverse(num,num+n);
		Y = calc();
		printf("Case #%d: %lld\n",cs,Y - X);
	}
	return 0;
}