#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>

using namespace std;

bool myfunc(string a,string b)
{
	return a.length()<b.length();
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int caset=1;caset<=t;caset++)
	{
		int a,b,k,ans=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
					ans++;
			}
		}
		cout << "Case #" << caset << ": " << ans << endl;
	}
	return 0;
}