
#include <bits/stdc++.h>
#define fi "a.inp"
#define fo "a.out"
#define For(i,a,b) for(int i=a;i<=b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define All(x) x.begin(),x.end()
#define st first
#define nd second
#define It interator

using namespace std;

typedef pair<int,int> II;
typedef pair<int,II> III;
typedef long long ll;
typedef pair<ll,ll> LL;
set <II> th;
struct Point 
{
	int x,y;
	bool operator <(const Point &T)
	{
			if (x==T.x) return (y<T.y);
			return (x<T.x);
	}
};
string s;

int main()
{
	freopen (fi, "r", stdin);
	freopen (fo, "w", stdout);
	int test = 0;

	scanf("%d", &test);
	For(Test,1,test)
	{
		int ans = 0;
		cin>>s;
		Ford(i,s.length()-1,0)
		{
			if (s[i]=='+')
			{
				if (ans%2==1)
				{
					ans++;
				}
			}
			if (s[i]=='-') {
				if (ans%2==0) {
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",Test,ans);
	}
	return 0;
}
