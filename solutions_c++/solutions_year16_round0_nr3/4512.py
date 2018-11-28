#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string.h>
#include <queue>
#include <map>
#include <set>
#include <math.h>

using namespace std;

#define MAXN 35
#define MAXJ 505
#define INF 2000000000
typedef long long ll;
typedef pair <ll, ll> pp;
int N, J, C;
ll n;
pp tmp[11];

ll po(int a, int b)
{
	ll res = 1;
	for(int i=0; i<b; i++) res *= a;
	return res;
}
ll convert(ll a, ll b)
{
	ll res = 0;
	for(int i=0; i<N; i++) {
		ll cur = 1<<i;
		if((a & cur) == cur) res += po(b, i);
	}
	return res;
}

ll findp(ll num)
{
	if((num % 2) == 0) {
	//	mp[num] = 2;
		return 2;
	}
	for(ll i=3; i*i<=num; i+=2) {
		if((num%i) == 0) {
	//		mp[num] = i;
			return i;
		}
	}
	//mp[num] = -1;
	return 0;
}
			
void printbinary(ll num)
{
	for(int i=N-1; i>=0; i--) {
		ll cur = 1<<i;
		if((num&cur) == cur) printf("1");
		else printf("0");
	}
	return;
}
int main(void)
{
	cin >> C;
	cin >> N >> J;
	printf("Case #1:\n");
	n = 1<<(N-1);
	n++;
	int cnt = 0;
	//printf("%lld\n", n);
	for(ll i=n; i<n*2; i++) {
		//printf("%lld\n", i);
		if((i%2) == 0) continue;
		if(cnt == J) return 0;
		memset(tmp, 0, sizeof(tmp));
		int f = 0;
		for(int j=2; j<=10; j++) {
			ll c;
		//	printbinary(i);
		//	printf("\n");
			if(j > 2) c = convert(i, j);
			else c = i;
			//printf("ay %d %lld\n",j,  c);
			tmp[j].first = i;
			tmp[j].second = findp(c);
			if(tmp[j].second == 0) f = 1;
		}
		if(f == 0) {
			printbinary(i);
		//	printf(" %d ", cnt);
			for(int j=2; j<=10; j++) {
			//	printf(" haha %lld\n", convert(i, j) % tmp[j].second);
				printf(" %lld", tmp[j].second);
			}
			if(cnt != 49) printf("\n");
			cnt++;
		}
	}
	return 0;
}
		
	
