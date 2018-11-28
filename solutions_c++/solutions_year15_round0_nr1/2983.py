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
int main()
{
	freopen("inp.txt" , "r" ,stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	cin >> t;
	int t1;
	for(t1 = 1; t1 <= t; t1++) {
		int l;
		cin >> l;
		string s;
		cin >> s;
		int i;

		int ans = 0;
		int sum = 0;
		for(i = 0; i <= l; i++) {
			int t = s[i] - '0';
			if(sum >= i) {
				sum = sum + t;
			} else {
				ans += (i - sum);
				sum = sum + t + (i - sum );
			}
		}
		cout << "Case #" << t1 << ": ";
		cout << ans << endl;
	}
	return 0;
}