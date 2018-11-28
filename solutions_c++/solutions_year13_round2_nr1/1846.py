#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
//#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int t,k=1,count;
	freopen("a.in","r",stdin);
	freopen("bb.txt","w",stdout);
	
	cin>>t;
	while(k <= t)
	{
		unsigned long long r,n,i;
		cin>>r>>n;
		vector<int> v(n);
		for(i = 0; i < n; i++)
		{
			cin>>v[i];
		}
		
		sort(v.begin(),v.end());
		count = v.size();
		int st=0;
		while(!v.empty())
		{
			if(r == 1)	break;
			while(r <= v[0]){
				r += r-1;
				st++;
			}
			for(i = 0;i<v.size();){
				if(r > v[i]){
					r += v[i];
					v.erase(v.begin()+i,v.begin()+i+1);
				}
				else	break;
			}
			
			if(count > st + v.size())	count = st + v.size();
		}
		
		printf("Case #%d: %d\n",k,count);
		k++;
	}
}
