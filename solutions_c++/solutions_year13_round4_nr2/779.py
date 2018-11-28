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
vector<int> tmp;
int n,p;
int curplace;
bool f1(int cur)
{
	if (tmp.size() == 0)
		return curplace < p;
	vector<int> news;
	if (cur<tmp[0])
	{
		for (int i=1;i<tmp.size();i+=2)
		{
			news.push_back(min(tmp[i],tmp[i+1]));
		}
	}
	else
	{
		curplace+= tmp.size()/2+1;
		for (int i=1;i<tmp.size();i+=2)
		{
			news.push_back(max(tmp[i],tmp[i+1]));
		}
	}
	tmp = news;
	return f1(cur);
}
int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int testcnt;
	cin>>testcnt;
	for (int curtest = 1; curtest<=testcnt;curtest++)
	{
		cout<<"Case #"<<curtest<<": ";
		
		cin>>n>>p;
		int ares=0,bres=0;
		for (int cur=0;cur<(1<<n);cur++)
		{
			bool ok1 = true,ok2 = true;
			tmp.resize(0);
			for (int j=0;j<(1<<n);j++)
			{
				if (j!=cur)
					tmp.push_back(j);
			}
			curplace = 0;
			if (f1(cur))
				ares = max(ares, cur);
			else
				ok1 = false;

			tmp.resize(0);
			
			curplace = 0;
			for (int j=(1<<n)-1;j>=0;j--)
			{
				if (j!=cur)
					tmp.push_back(j);
			}
			
			if (f1(cur))
				bres = max(bres, cur);
			else
				ok2 = false;
			if (!ok1 && !ok2)
				break;

		}
		cout<<ares<<' '<<bres;



		cout<<"\n";
	}
	return 0;
}
