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

void go()
{	
	int n,x;
	cin>>n>>x;
	vector<int> v(n);
	vector<int> used(n);
	for (int i=0;i<n;i++)
		cin>>v[i];
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	int res=0;
	for (int i=0;i<n;i++)
	{
		if (used[i]==0)
		{
			res++;
			used[i]=1;
			for (int j=i+1;j<n;j++)
			{
				if (used[j]==0 && v[i]+v[j]<=x)
				{
					used[j]=1;
					break;
				}
			}
		}
	}
	cout<<res;

}
int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		cout<<"\n";
	}
	return 0;
}
