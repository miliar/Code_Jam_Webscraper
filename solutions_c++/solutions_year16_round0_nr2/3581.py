#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007
#define MS0(x) memset(x, 0, sizeof(x))
#define ll long long int
#define in(x) scanf("%I64d", &x)
#define ind(x) scanf("%d", &x)
 
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input1.in", "r", stdin);
    freopen("output.txt","w",stdout);
#endif
 ios_base::sync_with_stdio(false);
cin.tie(NULL);
 int t,tc;
 cin>>tc;

 for(t=0;t<tc;t++)
 {
 	string s;
 	cin>>s;
 	ll len=s.length(),i;
 	ll ans=0;
 	if(s[len-1]=='-')
 	{
 		ans++;
 	}
 	for(i=0;i<len-1;i++)
 	{
 		if((s[i]=='-'&&s[i+1]=='+')||(s[i]=='+'&&s[i+1]=='-'))
 		{
 			ans++;
 		}
 	}
   cout<<"Case #"<<(t+1)<<": "<<ans<<"\n";
 }
 
	return 0;
}