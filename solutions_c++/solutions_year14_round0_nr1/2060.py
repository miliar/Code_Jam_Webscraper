#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long ll;


 int main()
{
	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{

		printf("Case #%d: ",case_id);
		int r;
		cin>>r;
		map<int, int> ret;
		int ans=-1;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				int tmp;
				cin>>tmp;
				if(i==r)
					ret.insert(make_pair(tmp,1));
			}
		cin>>r;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				int tmp;
				cin>>tmp;
				if(i==r)
				{
					if(ret.count(tmp)>0)
					{
						if(ans==-1)
							ans=tmp;
						else if(ans>0)
							ans=-2;
					}
				}
			}
		if(ans>0)
			cout<< ans;
		if(ans==-1)
			cout<<"Volunteer cheated!";
		if(ans==-2)
			cout<<"Bad magician!";
		printf("\n");
	}
	return 0;
}