#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;
typedef __int128_t bint;

int n, j;
char p[42];

void print(bint k)
{
	vector<int> d;
	while(k) {
		d.push_back((int)(k%10));
		k/=10;
	}
	for(int i=d.size()-1; i>=0; i--) printf("%d", d[i]);
}

bint prim(bint k)
{
	bint d=2;
	while(d<=(1LL<<10)) {
		if(k%d==0) return d;
		d++;
	}
	return 1;
}

int main()
{
	scanf("%*d%d%d", &n, &j);
	printf("Case #%d:\n", 1);
	for(ll m=0; m<(1LL<<(n-2)) && j; m++) {
		p[0]=1;
		for(ll i=1, k=m; i<=n-2; i++, k/=2) {
			p[i]=(k&1);
		}
		p[n-1]=1;
		vector<bint> w;
		for(int b=2; b<=10; b++) {
			bint k=0;
			for(bint i=n-1, j=1; i>=0; i--, j*=b) {
				k+=p[i]*j;
			}
			bint div;
			if((div=prim(k))==1) break;
			w.push_back(div);
		}
		if(w.size()==9) {
			for(int i=0; i<n; i++) printf("%d", p[i]);
			for(int i=0; i<w.size(); i++) {
				printf(" ");
				print(w[i]);
			}
			printf("\n");
			j--;
		}
	}

	return 0;
}
