#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int>PII;
typedef pair<ll, ll>PLL;

const int MAX = 100005;
const ll MOD = 1000000007;

void solve(int C)
{
	int i , j, len;

	cout<<"Case #"<<C<<": ";

	string S, A;
	char prev;

	cin>>S;
	A = "";
	len = S.length();
	A = S[0];

	prev = S[0];
	for(i = 1 ; i < len ; i++)
	{
		if(S[i] >= prev)
		{
			A = S[i]+ A;
			prev = S[i];
		}
		else
			A += S[i]; 
	}

	cout<<A<<endl;

	return;
}
int main()
{
	int t, i;
	scanf("%d", &t);

	for(i = 1 ;i <= t ; i++)
	{
		solve(i);
	}
	return 0;
}