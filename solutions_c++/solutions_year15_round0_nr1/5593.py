//  Created by Chlerry in 2015.
//  Copyright (c) 2015 Chlerry. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define ll long long

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int T,n;
	string a;
	cin>>T;
for(int ca=0;ca<T;ca++)
{
	int ans=0,cnt=0;
	cin>>n>>a;
	for(int i=0;i<=n;i++)
	{
		if(i>cnt)
		{
			ans+=i-cnt;
			cnt=i;
		}
		cnt+=a[i]-'0';
	}
	cout<<"Case #"<<ca+1<<": "<<ans<<endl;
}
	return 0;
}


