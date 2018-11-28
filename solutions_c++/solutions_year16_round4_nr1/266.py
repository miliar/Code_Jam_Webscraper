#include <bits/stdc++.h>
using namespace std;
const int MAXN = (1<<15);
int n,r,p,s;
char A[MAXN];
string ans = "";
void expand(int pos)
{
	int c1 = 2*pos, c2 = 2*pos + 1;
	A[c1] = A[pos];
	if(A[pos] == 'R')
		A[c2] = 'S';
	if(A[pos] == 'P')
		A[c2] = 'R';
	if(A[pos] == 'S')
		A[c2] = 'P';
}
bool is_ok()
{
	int T = (1<<n), rc = 0, pc = 0, sc = 0;
	for (int i = T; i < 2*T; ++i)
	{
		if(A[i] == 'R')
			rc++;
		else if(A[i] == 'S')
			sc++;
		else
			pc++;
	}
	if(rc != r || sc != s || pc != p)
		return false;
	return true;
}
void ssort(int pos, int lm, int rm)
{
	if(lm == rm)
		return;
	int m = (lm + rm)/2;
	ssort(2*pos, lm, m);
	ssort(2*pos + 1, m+1, rm);
	bool flag = false;
	for (int i = lm, j = m+1; i <= m; ++i, ++j)
	{
		if(A[i] > A[j])
		{
			flag = true;
			break;
		}
		else if(A[i] < A[j])
		{
			flag = false;
			break;
		}
		else
			continue;
	}
	if(flag)
	{
		for (int i = lm, j = m+1; i <= m; ++i, ++j)
			swap(A[i],A[j]);
	}
}
string getstr()
{
	string ret = "";
	int T = (1<<n);
	for (int i = T; i < 2*T; ++i)
		ret+=A[i];
	return ret;
}
void f(char ch)
{
	int T = (1<<n);
	A[1] = ch;
	for (int i = 1; i < T; ++i)
		expand(i);
	if(is_ok())
	{
		ssort(1, T, 2*T-1);
		if(ans == "IMPOSSIBLE")
			ans = getstr();
		else
			ans = min(ans,getstr());
	}
}
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	for (int tc = 1; tc <= t; ++tc)
	{
		cin>>n>>r>>p>>s;
		ans = "IMPOSSIBLE";
		f('R');
		f('P');
		f('S');
		cout<<"Case #"<<tc<<": "<<ans<<"\n";
	}
	return 0;
}