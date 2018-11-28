#include <vector>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <map>
#include <queue>
#include <climits>
#include <bitset>
#define LL long long
#define INFI 100000000000
#define D double
using namespace std;
#include <iomanip>


int main()
{
	
	LL t;
	cin>>t;
	LL tt=0;
	while(tt<t)
	{
		LL n;
		cin>>n;
		vector<LL> a(n);
		LL r= 0;
		for(LL i=0; i<n; i++)
		{
			cin>>a[i];
			r = max(r,a[i]);
		}
		LL ans=r;
		for(LL i=1; i<=r; i++)
		{
			LL c = 0;
			LL m = 0;
			for(LL j=0; j<n; j++)
			{
				if(a[j] > i)
				{
					c+=a[j]/i;
					if(a[j]%i == 0)
					{
						c--;
					}
				}
			}
			ans = min(ans,c+i);
		}		
		//cout<<endl;
		cout<<"Case #"<<tt+1<<": "<<ans<<endl;
		tt++;
	}
	return 0;
	
}


//6 4
//1 3 2 3 4 1