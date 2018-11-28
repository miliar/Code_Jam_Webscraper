#include <iostream>
#include <iomanip>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	long long r,t,first,last,mid;
	long long cases;
	cin>>cases;
	for(long long kase=1;kase<=cases;kase++)
	{
		cin>>r>>t;
		mid=(1-2*r+sqrtl((2*r-1)*(2*r-1)+8*t))/4;
		/*last=sqrtl(t);
		first=0;
		while(true)
		{
			mid=(first+last)/2;
			if(mid*(2*mid+2*r-1)==t)
			{
				break;
			}
			if(mid*(2*mid+2*r-1)>t)
			{
				if((mid-1)*(2*mid+2*r-1)<t)
				{
					mid--;
					break;
				}
				last=mid-1;
			}
			else
			{
				if((mid+1)*(2*mid+2*r-1)>t)
				{
					break;
				}
				first=mid+1;
			}
			
		}*/
		cout<<"Case #"<<kase<<": ";
		cout<<mid<<"\n";
	}
	return 0;
}
