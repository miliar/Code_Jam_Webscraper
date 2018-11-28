/*
#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <string>

using namespace std;

long long prime[701000]; 
bool a[100000010];
int len;
void init() {
	memset(a,0,sizeof(a));
	len = 0;
	for (long long i = 2;i <= 1e7;i ++) {
		if(a[i] == 0) {
			prime[len ++] = i;
		}
		for (long long j = 2;j * i <= 1e7;j ++) {
			a[i * j] = 1;
		}
	}
}

long long isprime(long long x) {
	long long tmp = sqrt(x);

	for (long long i = 0;i < len;i ++) {
		if(x % prime[i] == 0) {
			return prime[i] ;
		}
	}
	if(tmp <= 1e7) return -1;
	for (long long i = 1e7;i <= tmp;i ++) {
		if(x % i == 0) return i;
	}
	return -1;
}

long long calc(long long x,int base) {
	long long ret = 0;
	while(x > 0) {
		if(x % 10 == 1) {
			ret = ret * base + 1;
		}
		else {
			ret = ret * base;
		}
		x %= 10;;
	}
	return ret;
}

string binary(long long x) {
	string s = "";
	while(x > 0) {
		if(x & 1) {
			s = "1" + s;
		}
		else {
			s = "0" + s;
		}
		x >>= 1;
	}
	return s;
}
int bit(long long x,int pos) {
	return ((x >> pos) & 1);
}
int T;
int N,J;
int b[12];
int blen;
int main() {
//	cout << calc(11,2) << endl;
	init();
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	int Case = 1;
	while(T --) {
		blen = 0;
		scanf("%d%d",&N,&J);
		printf("Case #%d:\n",Case ++);
 		long long upp = (1 << N) - 1;
		long long low = (1 << (N - 1)) | 1;
		int cnts = 0;
		for (long long i = low;i <= upp;i ++) {
			if(bit(i,0)  == 0 || bit(i,N-1) == 0) continue;
			for (int j = 2;j <= 10;j ++) {
				long long res = calc(i,j);
				int out = isprime(res);
				if(out == -1) {
					blen = 0;
					break;
				}
				else {
					b[blen ++] = out;
				}
			}
			if(blen == 9) {
				cnts ++;
				string s = binary(i);
				cout << s;
				for (int idx = 0;idx < blen;idx ++) {
					printf(" %d",b[idx]);
				}
				puts("");
				if(cnts == J) {
					break;
				}
				blen = 0;
			}
		}
	}

}

*/

#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <string>

using namespace std;

int T,N,J;
long long prime[701000]; 
bool a[100000010];
int len;
void init() {
	memset(a,0,sizeof(a));
	len = 0;
	for (long long i = 2;i <= 1e7;i ++) {
		if(a[i] == false) {
			prime[len ++] = i;
		}
		for (long long j = 2;j * i <= 1e7;j ++) {
			a[i * j] = true;
		}
	}
}

long long isprime(long long x) {
	long long tmp = sqrt(x);

	for (long long i = 0;i < len && prime[i] < x;i ++) {
		if(x % prime[i] == 0) {
			return prime[i];
		}
	}
	if(tmp <= 1e7) return -1;
	for (long long i = 1e7;i <= tmp;i ++) {
		if(x % i == 0) return i;
	}
	return -1;
}


long long calc(long long x,int base) {
	long long sum = 0;
	long long add = 1;
	while(x > 0) {
		if(x & 1) {
			sum += add;
		}
		add = add * base; 
		x >>= 1;
	}
	return sum;
}

string binary(long long x) {
	string s = "";
	while(x > 0) {
		if(x & 1) {
			s = "1" + s;
		}
		else {
			s = "0" + s;
		}
		x >>= 1;
	}
	return s;
}

long long b[12];
int main() {
//	cout << isprime(37) << endl; 
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	init(); 
	int Case = 1;
	while(scanf("%d%d",&N,&J) != EOF) {
		printf("Case #%d:\n",Case ++);
		long long low = (1LL << (N -1)) | 1;
		long long upp = (1LL << N) - 1;
		int blen = 0;
		int cnt = 0;
		for (long long i = low;i <= upp;i ++) {

			if((i >> 0 & 1) == 0 || (i >> (N - 1) & 1) == 0) continue;
			//	cout << i << endl; 
			for (int j = 2;j <= 10;j ++) { 
				long long sum = calc(i,j);
				int factor = isprime(sum);
				if(factor == -1) {
					blen = 0;
					break;
				}
				else {
					b[blen ++] = factor;
				}
			}
			if(blen == 9) {
				string s = binary(i);
				cout << s;
				for (int idx = 0;idx < 9;idx ++) {
					printf(" %I64d",b[idx]);
				}
				puts("");
				blen = 0;
				cnt ++;
					
			}
			if(cnt == J) {
				break;
			} 
		
		}
	
	}
}






















 
