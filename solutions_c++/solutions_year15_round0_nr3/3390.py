#include<bits/stdc++.h>
using namespace std;

#define pb push_back 
#define mp make_pair
#define fi first
#define se second

#define MAX 10005
#define MAX2 4
#define MAX3 2
#define MAX4 3

#define ONE 0
#define I 1
#define J 2
#define K 3

int t;
int dp[MAX][MAX2][MAX3][MAX4];
vector<char> s;
char in[MAX];

int id(char c)
{
	if(c == 'i') return I;
	if(c == 'j') return J;
	if(c == 'k') return K;
	return ONE;
}
pair<int, int> prod(int id1, int isNeg1, int id2)
{
	int id, isNeg = 0;

	if(id1 == ONE) id = id2;
	else if(id1 == I)
	{
		if(id2 == ONE) id = I;
		else if(id2 == I) id = ONE, isNeg = 1;
		else if(id2 == J) id = K;
		else if(id2 == K) id = J, isNeg = 1;
	}
	else if(id1 == J)
	{
		if(id2 == ONE) id = J;
		else if(id2 == I) id = K, isNeg = 1;
		else if(id2 == J) id = ONE, isNeg = 1;
		else if(id2 == K) id = I;
	}
	else if(id1 == K)
	{
		if(id2 == ONE) id = K;
		else if(id2 == I) id = J;
		else if(id2 == J) id = I, isNeg = 1;
		else if(id2 == K) id = ONE, isNeg = 1;
	}

	return mp(id, ((!isNeg1 && isNeg) || (isNeg1 && !isNeg)));
}

int opt(int i, int actual, int actualIsNeg, int pos)
{
	if(pos > 2) return 0;
	if(i == (int)s.size()) return (pos == 2 && actual == K && actualIsNeg == 0);
	int &state = dp[i][actual][actualIsNeg][pos];
	if(state != -1) return state;	
	
	pair<int, int> p = prod(actual, actualIsNeg, id(s[i]));
	actual = p.fi; actualIsNeg = p.se;

	state = opt(i+1, actual, actualIsNeg, pos);
	if(!state)
	{
		if(pos == 0 && actual == I && !actualIsNeg) state = opt(i+1, ONE, 0, pos+1);
		if(pos == 1 && actual == J && !actualIsNeg) state = opt(i+1, ONE, 0, pos+1);
	}
	
	//printf("i= %d, actual= %d, actualIsNeg= %d, pos= %d\n", i, actual, actualIsNeg, pos);

	return state;
}

int main()
{
	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		s.clear();
		int l, x;
		scanf("%d %d %s ", &l, &x, in);
		for(int i=0; i<x; ++i)
			for(int j=0; j<l; ++j)
				s.pb(in[j]);

		memset(dp, -1, sizeof(dp));
		int sol = opt(0, ONE, 0, 0);
		printf("Case #%d: %s\n", tc, (sol == 1) ? "YES" : "NO");
	}

	return 0;
}
