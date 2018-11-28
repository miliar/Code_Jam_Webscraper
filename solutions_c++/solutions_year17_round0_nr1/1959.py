#include<iostream>
#include<cstdio>
using namespace std;
#define LLN 10000000

int getMoves(string& s, int l, int r, int K)
{
	if(r-l+1 <= K)
	{
		bool eq = r-l+1 == K;
		for(int i=l+1;i<=r;i++)
		{
			if(s[i] != s[i-1])return LLN;
		}
		if(eq)
			return s[l] == '+' ? 0 : 1;
		else
			return s[l] == '+' ? 0 : LLN;
	}
	int ans = 0;
	if(s[l] != '+')
	{
		for(int i=l;i<l+K;i++) s[i] = s[i] == '+' ? '-' : '+';
		ans++;
	}
	if(s[r] != '+')
	{
		for(int i=r;i>r-K;i--) s[i] = s[i] == '+' ? '-' : '+';
		ans++;
	}
	return ans + getMoves(s, l+1, r-1, K);
}

int main()
{
	freopen("A-large.in", "r",stdin);
	freopen("output.txt", "w",stdout);
	int T,K;
	string S;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>S>>K;
		int numMoves = getMoves(S,0,S.length()-1,K);
		
		cout<<"Case #"<<i<<": ";
		if(numMoves < LLN)
			cout<<numMoves<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
	}
}
		
