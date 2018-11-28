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

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; ++t)
	{
		string s;
		cin >> s;
		int ptr = s.size() - 1;
		int res = 0;
		while (ptr != -1)
		{
			if (s[ptr] == '+')
			{
				ptr--;
				continue;
			}
			int ptr2 = 0;
			while (s[ptr2] == '+')
			{
				ptr2++;
			}
			for (int i = 0; i < ptr2; ++i)
				s[i] = '-';
			if (ptr2 > 0)
				res++;
			reverse(s.begin(),s.begin() + ptr + 1);
			for (int i = 0; i < ptr + 1; ++i)
			{
				if (s[i] == '-')
					s[i] = '+';
				else
					s[i] = '-';
			}
			res++;
		}
		printf("Case #%d: %d\n",t + 1,res);	
	}
	return 0;
}