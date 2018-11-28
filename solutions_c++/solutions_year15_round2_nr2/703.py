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

int r,c,n;
void go()
{	
	cin>>r>>c>>n;
	vector<vector<bool> > used(r, vector<bool>(c));
	int res = (r+1)*(c+1);
	for (int msk=0;msk<(1<<(r*c));msk++)
	{
		int q = 0;
		int l = 0;
		for (int i=0;i<r;i++)
		{
			for (int j=0;j<c;j++)
			{
				if (msk&(1<<q))
				{
					used[i][j]=1;
					l++;
				}
				else
					used[i][j] = 0;
				q++;
			}
		}
		if (l!=n)
			continue;
		
		int cur = 0;
		for (int i=0;i<r;i++)
		{
			for (int j=0;j<c;j++)
			{
				if (i+1<r && used[i+1][j]&& used[i][j])
					cur++;
				if (j+1<c && used[i][j+1]&& used[i][j])
					cur++;
			}
		}
		res= min(res, cur);
	}
	cout<<res;
}
int main()
{	
	freopen("B-small-attempt0(1).in","r",stdin);
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
