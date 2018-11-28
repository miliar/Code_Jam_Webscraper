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

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int cases;
	double c,f,x,sum,prevT,currT;
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>c>>f>>x;
		sum=0;
		prevT=x/2;
		for(int i=1;;i++)
		{
			sum+=c/(2+(i-1)*f);
			currT=x/(2+i*f)+sum;
			if(currT>prevT)
			{
				break;
			}
			prevT=currT;
		}
		cout<<"Case #"<<kase<<": "<<fixed<<setprecision(7)<<prevT<<"\n";
	}
	return 0;
}