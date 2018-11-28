#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<sstream>
#include<set>
#include<climits>
#define gc getchar
#define f first
#define s second
#define TEST ll T = scan(); for(int t=1; t<=T; t++)
#define D(x) ll x = scan()
using namespace std;
typedef long long ll;
#define rep(i, n) for(ll i=0; i<n; i++)
ll scan() 
{
  char c = gc();
  while(c<'0' || c>'9') c = gc();
  ll ret = 0;
  while(c>='0' && c<='9') {
    ret = 10 * ret + c - 48;
    c = gc();
  }
  return ret;
}
int main()
{
	TEST
	{
		D(n); 
		string s; cin>>s;
		ll ans = 0, count = s[0]-48;
		for(int i=1; i<s.length(); i++)
		{
			if(count < i)
				ans++, count++, count+=s[i]-48;
			else
				count += s[i]-48;
		}
		printf("Case #%d: %lld\n", t, ans);
	}
	return 0;
}
