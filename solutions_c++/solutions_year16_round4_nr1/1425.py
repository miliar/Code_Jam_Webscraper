#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define LEFT(pos) (2*pos + 1)
#define RIGHT(pos) (2*pos + 2)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int N = (1 << 12) + 10;
string tree[4*N];
int rr, ss, pp;
int n;

string solve(int start, int end, int cur, int pos)
{
	if (start == end)
	{
		if (cur == 'R')
			rr++;
		else if (cur == 'S')
			ss++;
		else
			pp++;


		string ret;
		ret.push_back((char)cur);
		return tree[pos] = ret;
	}


	int mid = (start+end)/2;
	string left, right;

	if(cur == 'R')
	{
		left = solve(start, mid, 'S', LEFT(pos));
		right = solve(mid+1, end, 'R', RIGHT(pos));
	}
	else if (cur == 'S')
	{
		left = solve(start, mid, 'P', LEFT(pos));
		right = solve(mid+1, end, 'S', RIGHT(pos));
	}
	else
	{
		left = solve(start, mid, 'P', LEFT(pos));
		right = solve(mid+1, end, 'R', RIGHT(pos));
	}

	if ((left + right) < (right + left))
		return left + right;
	
	return right + left;
}

int main()
{
	int T, casecnt = 0;

	scanf("%d", &T);

	while(T--)
	{
		int r, p, s;
		string ans, cur;

		scanf("%d %d %d %d", &n, &r, &p, &s);
		
		n = (1 << n);

		printf("Case #%d: ", ++casecnt);
		
		rr = pp = ss = 0;
		cur = solve(0, n-1, 'R', 0);

		if (rr == r and pp == p and ss == s)
			ans = cur;	

		rr = pp = ss = 0;
		cur = solve(0, n-1, 'S', 0);
		if (rr == r and pp == p and ss == s)
		{
			if (ans.size() == 0)
				ans = cur;
			else
				ans = min(ans, cur);
		}

		rr = pp = ss = 0;
		cur = solve(0, n-1, 'P', 0);
		if (rr == r and pp == p and ss == s)
		{
			if (ans.size() == 0)
				ans = cur;
			else
				ans = min(ans, cur);
		}

		if (ans.size() == 0)
			printf("IMPOSSIBLE\n");
		else
		{
			printf("%s\n", ans.c_str());
		}
	}
	return 0;
}


