#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
// 0  1 2  3 4  5 6  7
// i -i j -j k -k 1 -1
typedef long long LL;
const int N = 1e4 + 11;
char s[N];
int p[N], q[N];
int encode(char c){
	if(c=='i')	return 0;
	if(c=='j')	return 2;
	if(c=='k')	return 4;
	if(c=='1')	return 6;
}
int mul(int a, int b){
	int x = a>>1;
	int y = b>>1;
	if(x==3)	return b^(a&1);
	if(y==3)	return a^(b&1);
	if((x+1)%3==y)	return ((y+1)%3)*2 ^ (a&1) ^ (b&1);
	if((y+1)%3==x)	return ((x+1)%3)*2 ^ (a&1) ^ (b&1) ^ 1;
	else	return 7 ^ (a&1) ^ (b&1);
}
int ni(int a){
	int x = a>>1;
	if(x==3)	return a;
	else	return (a^1);
}
int mi(int x, LL n){
	int ans = encode('1');
	while(n){
		if(n&1)	ans = mul(ans, x);
		x = mul(x, x);
		n >>= 1;
	}
	return ans;
}
void out(int x){
	switch(x){
		case 0:	printf("i"); break;
		case 1:	printf("-i"); break;
		case 2:	printf("j"); break;
		case 3:	printf("-j"); break;
		case 4:	printf("k"); break;
		case 5:	printf("-k"); break;
		case 6:	printf("1"); break;
		case 7:	printf("-1"); break;
	}
	printf("\n");
}
int main()
{
	// freopen("C-large.in", "r", stdin);
	// freopen("ou.txt", "w", stdout);
	// freopen("in.txt", "r", stdin);
	int t, kase=0;
	scanf("%d", &t);
	while(t--){
		LL L, X;
		cin >> L >> X;
		scanf("%s", s+1);
		p[0] = q[0] = encode('1');
		for(int i=1; i<=L; i++){
			p[i] = mul(p[i-1], encode(s[i]));
		}
		for(int i=L; i>0; i--){
			q[L-i+1] = mul(encode(s[i]), q[L-i]);
			// out(q[L-i+1]);
		}
		LL a = 1e16;
		LL b = 1e16;
		for(int i=1; i<=L; i++){
			int nf = mul(encode('i'), ni(p[i]));
			// out(encode('i'));
			// out(ni(p[i]));
			// out(nf);
			int t = encode('1');
			for(int j=0; j<4; j++){
				if(nf==t){
					a = min(a, j*L+i);
					break;
				}
				t = mul(t, p[L]);
			}
		}
		for(int i=L; i>0; i--){
			int nf = mul(ni(q[L+1-i]), encode('k'));
			// out(ni(q[L+1-i]));
			// out(encode('k'));
			// out(nf);
			int t = encode('1');
			for(int j=0; j<4; j++){
				if(nf==t){
					b = min(b, j*L+L+1-i);
					break;
				}
				t = mul(q[L], t);
			}
		}
		// cout << a << ' ' << b << endl;
		printf("Case #%d: %s\n", ++kase, (a+b<L*X) && mi(p[L], X)==7? "YES" : "NO");
	}
	return 0;
}