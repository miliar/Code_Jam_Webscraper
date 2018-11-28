#include<iostream>
#include<cstdio>
#include<cstring>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define LL long long 
LL a, b, k;
LL p[50];
int bit_a[50], bit_b[50], bit_k[50];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	p[0] = 1;
	for (int i = 1; i <= 32; ++i)
		p[i] = p[i - 1] * (LL)2;
	int T; cin >> T;
	int ca = 0;
	while (T--) {
		cin >> a >> b >> k;
		++ca;
		printf("Case #%d: ", ca);
		int ans = 0;
		for (int i = 0; i < a;++i)
		for (int j = 0; j < b;++j)
		if ((i&j) < k) ++ans;
		cout << ans << endl;
	}
}

