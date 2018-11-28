//THEM THAT STICK TO IT OUT, ARE THEM THAT WIN
//The closer you think you're, the less you will actually see.
#include "bits/stdc++.h"
#define sd(n) scanf("%d", &(n))
#define rep(i, x, n) for (int i = x, _n = (n); i < _n; ++i)
#define repV(i, v) for (i = v.begin(); i != v.end(); i++)
#define SZ(c) (int)(c).size()
#define lcm(a,b) (a*(b/__gcd(a,b)))
#define VI vector<int>
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mii map<int, int>
#define pii pair<int, int>
#define pip pair<int, pii>
#define F first
#define S second
#define mp make_pair
#define lli long long int
#define CLR(p) memset(p, 0, sizeof(p))
#define SET(p) memset(p, -1, sizeof(p))
#define INF 0x3f3f3f3f
using namespace std;

const int MOD = 1e9+7;
const int MAX = 100010;

int main()
{
	int t, n;
	string s;
	cin >> t;
	rep(cs, 1, t+1)
	{
		cin >> n;
		cin >> s;

		int ans = 0;
		int standing = (int)(s[0] - '0');

		/*
			we have a string s
			s[0] is number of ppl with shyness level 0
			s[i] is number of ppl iwht shyness level i

			any person wiht shyness level s will stand up only when s ppl have only stood up

			so s[0] ppl are initially standing

			s[1] ppl will stand only if no of standing ppl is >= 1
		*/
		rep(i, 1, n+1)
		{
//			printf("i is %d\n", i);
//			printf("standing is %d\n", standing);
			if(s[i] == '0')
			{
//				printf("skipping s[%d] = 0\n", i);
				continue;
			}
			if(standing >= i)
			{
//				printf("increasing standing by %d\n", s[i] - '0');
				standing += (s[i] - '0');
			}
			else
			{
//				printf("standing < i \n");
				int tmp = i - standing;
//				printf("tmp is %d\n", tmp);
				ans += tmp, standing += tmp;
				standing += s[i] - '0';
			}
		}
		printf("Case #%d: %d\n", cs, ans);
	}
    return 0;
}    



