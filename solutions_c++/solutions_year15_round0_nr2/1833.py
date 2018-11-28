#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;
int n;
int d[1000];
bool test(int med)
{
	for (int low = 1; low <= med;low++)
	{
		int cnt = 0;
		for (int i=0;i<n;i++)
		{
			if (d[i]>low)
			{
				int c = 2;
				while (d[i]/c+(d[i]%c!=0) >low)
					c++;
				cnt+=c-1;

			}
			else
				continue;
		}
		if (cnt+low<=med)
			return true;
	}
	return false;
}
void go()
{	
	cin>>n;
	for (int i=0;i<n;i++)
	{
		cin >> d[i];
	}
	int l = 1;
	int r = 1001;
	int ans = r;
	while (l+1<r)
	{
		int med = (l+r)/2;
		if (!test(med))
			l = med+1;
		else
		{
			ans = med;
			r = med;
		}
	}
	if (test(l))
		ans = l;
	cout<<ans;
}
int main()
{	
	freopen("B-large.in","r",stdin);
	freopen("2.out","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		if (curcase!=cases)
			cout<<"\n";
	}
	return 0;
}
