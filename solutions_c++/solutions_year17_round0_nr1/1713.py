/*input
100
---+-++- 3
+++++ 4
-+-+- 4
---------- 3
-+- 2
++-- 2
+++++++ 7
-+++ 2
-++++++++- 9
-+++++++++ 2
+-+- 2
+++--- 3
-+++- 4
++-+ 2
--+ 3
+-+-+-+-+- 2
-++ 2
++- 3
+- 2
-------- 8
-+-+ 3
-+-- 3
-+-+ 2
++++ 3
+++ 3
+--- 2
+--+ 3
-++++++++- 10
-+ 2
++-+----+ 3
--------- 3
--+ 2
------+ 3
--+- 3
++++ 2
--++ 2
-+++++++-+ 2
-------+++ 7
--- 2
-++++-- 5
+-+- 3
--+- 2
+-+-+-+ 3
+-------- 8
++-+ 3
+++++ 5
+-+ 3
+-++ 3
-+-- 2
--+-- 2
-++++++++- 2
---------- 2
+-- 3
---- 3
---+ 2
+++ 2
-+- 3
+-+-+ 2
+-++++--+ 2
-++++++++- 8
-+++ 3
++- 2
+-+-+-+-+ 3
-++- 2
--++ 3
++---+---- 8
+--++++-+ 6
---+--- 7
-+++++-++- 9
++++++++++ 10
-+++++++-- 2
+--+ 2
---- 2
+-- 2
++-++++ 4
-++ 3
-++- 3
---------- 5
------ 6
+-+-+-+- 3
+-+++-++- 7
++-- 3
+-++-++ 2
-- 2
+-+ 2
-+++-+++- 8
+++- 2
++ 2
-++++++-++ 7
++--+++-- 5
+++- 3
---------- 10
+-+-+-+-+- 3
+--- 3
-+++++++-+ 8
---+ 3
+---+ 3
+-++ 2
--- 3
-+-+-+-+-+ 2

*/
#include <iostream>
#include <bits/stdc++.h>
#include <queue>
#include <vector>
#include <cmath>
#include <cstring>
#include <climits>
#include <set>
#include <algorithm>
#define inf LONG_MAX
#define MAX 100010
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define RESET(a,b) memset(a, b, sizeof a)
#define boost ios_base::sync_with_stdio(false);cin.tie(0) 
#define PII pair<ll,ll>
typedef long long int ll;
using namespace std;
ll a[MAX+5];
ll T;
ll M=1e9+7;
string s;
int main() {
	
	boost;	
	ll i,j,n,k,o=0;
	cin>>T;
	while(T--)
	{
		o++;
		ll count=0;
		cin>>s;
		cin>>k;
		ll n=s.length();
		for(i=0;i<n;i++)
		{
			if(s[i]=='+')
				a[i+1]=1;

			else
				a[i+1]=0;
		}

		for(i=1;i<=n-k+1;i++)
		{
			if(a[i]==0)
			{
				count++;
				for(j=i;j<=i+k-1;j++)
					a[j]^=1;
			}
		}

		ll flag=0;
		for(i=1;i<=n;i++)
		{
			if(a[i]==0)
			{
				flag=1;
				break;
			}
		}

		if(flag)
			cout<<"Case #"<<o<<": "<<"IMPOSSIBLE"<<endl;

		else
			cout<<"Case #"<<o<<": "<<count<<endl;

	}
	

}