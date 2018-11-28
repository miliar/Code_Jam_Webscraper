#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define PI 3.14159265359
#define endl '\n'

using namespace std;

const int MAX = 1e6; // 1e8
int n,m,test,ans;
ll cur[11],p[MAX],po[11][32];
bool mask[32];

inline ll div(ll x)
{
	if(x < MAX)
		return p[x];
	for(ll i=2;i*i<=x;i++)
		if(!(x%i))
			return i;
	return 0;
}

void f(int x)
{
	if(ans == m)
		return;
	if(x == n-1)
	{
		for(int i=2;i<=10;i++)
			if(!div(cur[i]))
				return;
		++ans;
		for(int i=n-1;i>=0;i--)
			cout << mask[i];
		cout << " ";
		for(int i=2;i<=10;i++)
			cout << div(cur[i]) << " ";
// 		cout << ans;
		cout << endl;
		return;
	}
	
	if(ans == m)
		return;
	f(x+1);
	if(ans == m)
		return;
	mask[x] = 1;
	// stuff to do. powers to precompute.
	for(int i=2;i<=10;i++)
		cur[i] += po[i][x];
	f(x+1);
	if(ans == m)
		return;
	mask[x] = 0;
	// stuff to do. powers to precompute.
	for(int i=2;i<=10;i++)
		cur[i] -= po[i][x];
// 	f(x+1);
}

int main()
{
// 	ios_base::sync_with_stdio(0);
	
	// Crible.
	for(int i=2;i*i<MAX;i++)
		if(!p[i])
			for(int j=2*i;j<MAX;j+=i)
				p[j] = i;
	
	// Precompute powers.
	for(int i=2;i<=10;i++)
	{
		po[i][0] = 1;
		for(int j=1;j<32;j++)
			po[i][j] = po[i][j-1]*i;
	}
			
	cin >> test;
	for(int te=1;te<=test;te++)
	{
		cin >> n >> m;
		cout << "Case #" << te << ": " << endl;
		ans = 0;
		for(int i=2;i<=10;i++)
			cur[i] = 1 + po[i][n-1];
		for(int i=0;i<n;i++)
			mask[i] = 0;
		mask[0] = mask[n-1] = 1;
		f(1);
	}
	
	return 0;
}