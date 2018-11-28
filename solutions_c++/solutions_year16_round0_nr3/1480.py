#include <bits/stdc++.h>
using namespace std;
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<ii, ii>
#define vvi vector<vi>
#define MAX 1000000
#define MAXN 200005
#define MAXE 100005
#define INF 10000000
#define MOD 1000000007
#define FOR(x,n) for(int x = 0; x < n; x++)
#define FOR1e(x,n) for(int x = 1; x <= n; x++)

const int N = 10000;
int lp[N+1];
vector<int> pr;

char printable[33];

void crivo() { 
	for (int i=2; i<=N; ++i) {
	      if (lp[i] == 0) {
	            lp[i] = i;
	            pr.push_back (i);
	      }
	      for (int j=0; j<(int)pr.size() && pr[j]<=lp[i] && i*pr[j]<=N; ++j)
	            lp[i * pr[j]] = pr[j];
	}
}

void printar(long long v) {
	stack<int> f;
	while(v > 0) {
		if(v%2) f.push(1);
		else f.push(0);
		v >>= 1;
	}
	while(!f.empty()) {
		printf("%d", f.top());
		f.pop();
	}
}
void precompute() {
	long long b[12], divisor[12], tmp, fac[12];
	b[2] = 1;
	for(int it = 0; it < 15; it++) {
		b[2] *= 2;
	}
	b[2]++;

	int total = 0;
	bool ok, ok2;
	while(total < 50) {
		tmp = b[2];
		for(int i = 3; i <= 10; i++) { b[i] = 0; fac[i] = 1; }

		while(tmp > 0) {
			for(int i = 3; i <= 10; i++) {
				if(tmp%2 == 1) b[i] += fac[i];
				fac[i] *= i;
			}
			tmp /= 2;
		}
		ok = true;
		for(int i = 2; i <= 10; i++) {
			ok2 = false;
			for(int ind = 0; ind < pr.size(); ind++) {
				if(b[i]%pr[ind] == 0LL) {
					ok2 = true; divisor[i] = pr[ind]; break;
				}
			}
			if(!ok2) {
				ok = false; break;
			}
		}
		if(ok) {
			total++;
			printar(b[2]);
			for(int j = 2; j <= 10; j++) printf(" %lld", divisor[j]);
			printf("\n");
		}
		b[2] +=2;
	}
}

int conta = 0;
void backtrack(int ind, int even, int odd) {
	if(conta >= 500 ) return;
	if(even < 0 || odd < 0) return;
	if(even == 0 && odd == 0) {
		conta++;
		printf("%s 3 2 3 2 7 2 3 2 11\n", printable);
		return;
	}
	else if(ind == 31) return;
	
	if(ind%2 == 0) {
		if(even > 0) {
			printable[ind] = '1';
			backtrack(ind+1, even-1, odd);
			printable[ind] = '0';
		}
		if(((31 - ind)/2) >= even && (30 - ind)/2 >= odd) {
			backtrack(ind+1, even, odd);	
		}
	}
	
	if(ind%2 == 1) {
		if(odd > 0) {
			printable[ind] = '1';
			backtrack(ind+1, even, odd-1);
			printable[ind] = '0';
		}
		if(((31 - ind)/2) >= even && (30 - ind)/2 >= odd) {
			backtrack(ind+1, even, odd);	
		}
	}
}
int main() {
	int c;
	printf("Case #1:\n");
//	crivo();
//	precompute();
	for(int i = 0; i < 32; i++) printable[i] = '0';
	printable[0] = '1';
	printable[31] = '1';
	printable[32] = '\0';

//	backtrack(1, 3, 4);
	backtrack(1, 5, 5);
//	backtrack(1, 7, 8);
}