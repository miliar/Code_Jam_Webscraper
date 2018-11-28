#include <iostream>
#include <string>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

unsigned long long r2, area, paintremaining;

int main()
{
	int testCasesCount = 0, nTestCases;
	cin>>nTestCases;

	unsigned long long r, t, count = 0;
	while(cin>>r>>t)
	{
//		cout<<"Read r and t : "<<r<<" "<<t<<endl;
		testCasesCount++ ;
		int r1 = r;
		paintremaining = t;
		r2 = r1 + 1;
		area = (r2*r2) - (r1*r1);
		cout<<"area = "<<area<<"\tpaintremaining = "<<paintremaining<<endl;
		count = 0;
		while(area <= paintremaining)
		{
			paintremaining = paintremaining - area;
			r1 = r2 + 1;
			r2 = r1 + 1;
			area = (r2*r2) - (r1*r1);
			count = count + 1;
		}		
		cout<<"Case #"<<testCasesCount<<": "<<count<<endl<<endl;
	}
}