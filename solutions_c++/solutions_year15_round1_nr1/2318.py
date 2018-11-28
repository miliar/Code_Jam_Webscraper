#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <string.h>
#include <sstream>
#include <ctime>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

ll cases,n,sum,rate,m[1010];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	std::ios::sync_with_stdio(false);
	
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>m[i];
		}
		cout<<"Case #"<<kase<<": ";
		sum=0;
		rate=0;
		for(int i=1;i<n;i++)
		{
			if(m[i]<m[i-1])
			{
				sum+=m[i-1]-m[i];
				if(m[i-1]-m[i]>rate)
				{
					rate=m[i-1]-m[i];
				}
			}
		}
		cout<<sum<<" ";
		sum=0;
		for(int i=0;i<n-1;i++)
		{
			if(m[i]<=rate)
			{
				sum+=m[i];
			}
			else
			{
				sum+=rate;
			}
		}
		cout<<sum<<"\n";
	}
	return 0;
}