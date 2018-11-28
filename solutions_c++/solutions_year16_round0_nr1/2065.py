#include <iostream> 
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm> 
#include <cmath> 

#include <vector> 
#include <set>
#include <map>
#include <string>
#include <bitset>
#include <queue>
#include <unordered_map>
#include <sstream>


using namespace std;
typedef long long ll;

const ll mod = 1e9 + 7;
ll gcd(ll a, ll b)
{
	return b ? gcd(b, a%b) : a;
}
set <int> s;
void count(ll n)
{
	if (n == 0)
		s.insert(0);
	while (n)
	{
		s.insert(n % 10);
		n /= 10;
	}
	return;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; ++t)
	{
		ll n;
		cin >> n;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", t + 1);
			continue;
		}
		s.clear();
		count(n);
		ll tt = 1;
		while (s.size() != 10)
		{
			n /= tt;
			tt++;
			n *= tt;
			count(n);
		}
		printf("Case #%d: %d\n",t + 1,n);	
	}
	return 0;
}