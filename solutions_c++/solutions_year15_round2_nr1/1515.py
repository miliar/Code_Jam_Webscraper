#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long long int lli;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<long> si;
typedef multiset<long> msi;
typedef map<string,long> maps;                               

#define Clear(a) memset(a,0,sizeof a);
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
 
#define MAX 1111111

 
int dp[MAX];
 
int rev(int n)
{
	string s=to_string(n);
	reverse(s.begin(),s.end());
	int x=stoi(s);
	return x;
}

 
queue<int> ns;
int main()
{
	Clear(dp);
    int a,b,c;
	dp[1] = 1;
	ns.push(1);
	while (!ns.empty())
	{
		int x = ns.front();
		ns.pop();
		if (x + 1 < MAX and dp[x + 1] == 0)
		{
			dp[x + 1] = dp[x] + 1;
			ns.push(x + 1);
		}
		if (rev(x) < MAX and dp[rev(x)] == 0)
		{
			dp[rev(x)] = dp[x] + 1;
			ns.push(rev(x));
		}
	}
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++)
	{
		long long n;
		cin >> n;
		printf("Case #%d: %d\n", t, dp[n]);
	}
}
 