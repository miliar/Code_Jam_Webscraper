#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <set>
#include <utility>
#include <stack>
#include <cassert>
using namespace std;
typedef long long int ll;

ll tt,t,s,a[111111],standing,ans;
char c;

int main()
{
	cin>>t;
	tt = 1;
	while(t--)
	{
		cin>>s;
		for(int i=0;i<=s;i++)
		{
			cin>>c;
			a[i] = c-'0';
		}
		standing = 0;
		ans = 0;
		for(int i=0;i<=s;i++)
		{
			if(standing>=i)
			{
				standing = standing + a[i];
			}
			else
			{
				ans = ans + i - standing;
				standing = standing + i - standing + a[i];
			}
		}
		cout<<"Case #"<<tt++<<": "<<ans<<"\n";
	}
}
	