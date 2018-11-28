#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#define S(n) scanf("%d",&n)
#define Sll(n) scanf("%lld",&n)
#define Sl(n) scanf("%ld",&n)
#define ll long long 
#define li long int
using namespace std;
struct node {
	ll x;
	ll y;
};
ll gcd(ll a, ll b)
{
	return b == 0 ? a : a > b ? gcd(b, a%b) : gcd(a, b%a);
}
bool myfunc(struct node a,struct node b)
{
	if(a.x == b.x) {
		return a.y < b.y;
	} else {
		return a.x < b.x;
	}
}

int a[1010];
int main()
{
	freopen("inp.txt" , "r" ,stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	S(t);
	int t1;
	for(t1 = 1; t1 <= t; t1++) {
		int n;
		S(n);
		int i;
		int j;	
		int ans = 1000010;
		for(i = 1; i <= n; i++) {
			S(a[i]);
		}
		sort(a+1, a+n+1);
		for(i = 1; i <= 1000; i++) {
			int s =0;
			for(j = n; j >= 1; j--) {
				if(a[j] <= i) {
					break;
				}
				s = s +  (a[j] / i);
				if(a[j] % i == 0) {
					s--;
				}
			}
			s = s + i;
			ans = min(ans, s);
		}
		printf("Case #%d: %d\n",t1, ans);
	}
	return 0;
}