/*input
100
-
-+
+-
+++
--+-
+--
+-++--++-+
--+++-+---
--++--+
+---+-+-++
+-+-++-+-+
--++++-+
-+---++---
--+---+--+
+-+--
+-+
++
+---++-+-+
+-+++----+
+-+++-+++-
-+-+
-++----++-
+-+-
+-+-+--
++-+
++++-+++-+
----
-++--++-+
-+-++-+++-
+++-+-+++-
-+--++++--
-+++
+-++
--+
---+--+---
++++-+-+-+
-+-+-+-+-+
-++++++++-
++-++++++-
+++++
-++++--+--
-+-+-+--+
++++
+---
------+--+
++++---+-+
++-+-+--+-
+-+-+++
-++
--++-+-
--++
--+-++-
-+--++--++
-+---+++++
-++-++---+
-+-
---+---++-
-+-+--+++-
++---+--++
++----+++-
+-+--+
+-++---
+-+-++++++
+-+-+-
-+++--+--+
--+++-++-+
+-++++-
+++-++--+-
-+--
+++-++-+++
+-++---+
-------+-+
-++-
--+-+--+--
+++------+
----+--+-+
+-----+++-
+-+-++++-+
---
----++-+-+
++--
++-+-----+
---++++---
++-
+--+
+
-++-----+-
---+++----
-+++----+-
-++-++-+-+
+--------+
+-+-+-+-+-
---+
--
-----
+++-
--++-+--++
-+--+-+-+-
+-----+---
-++-+---++

*/
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define pii pair<long long,long long>
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define INF 1000000009
#define mod 1000000007

bool check(char s[])
{
	ll count=0;
	for(ll i=0;i<strlen(s);i++)
			if(s[i]=='+')
				count++;
		if(strlen(s)==count)
			return true;
		else
			return false;
}
int main() 
{
    std::ios::sync_with_stdio(false);
  	ll t;
	cin>>t;
	for(ll r=1;r<=t;++r)
	{
		char s[101];
		cin>>s;
		ll count=0;
		if(check(s))
		{
			cout<<"Case #"<<r<<": 0\n";
			continue;
		}
		count=0;
		ll ans=0;
		while(count!=strlen(s))
		{
			count=0;
			if(s[0]=='+')
			{
				ll index=0,w=0;
				for(ll i=1;i<strlen(s);i++)
				if(s[i]=='-')
				{
					index=i;
					break;
				}
				if(index==0)
				    break;
				for(ll i=0;i<index;i++)
				{
					s[i]='-';
					w=1;
				}
				if(w==1)
				ans++;
			}
			else
			{
				ll index=0,w=0;
				for(ll i=1;i<strlen(s);i++)
					if(s[i]=='+')
					{
						index=i;
						break;
					}
				if(index==0)
				{
				    ans++;
				    break;
				}
				for(ll i=0;i<index;i++)
				{
					s[i]='+';
					w=1;
				}
				if(w==1)
					ans++;
			}
			if(check(s))
				break;
		}
		cout<<"Case #"<<r<<": "<<ans<<endl;
	}
    return 0;
}