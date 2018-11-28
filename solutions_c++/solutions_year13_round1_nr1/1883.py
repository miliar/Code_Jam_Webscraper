#include <iostream>
#include <fstream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int cases,rings=0;
	unsigned long long r,t,req;
	double white,black;
	string line,temp;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
	cin>>cases;
	//getline(cin,line);
	for (int x=0; x < cases ; x++)
	{
		rings=0;
		r=0;
		t=0;
		white=0;
		black=0;
		req=0;
		//int count=0;
		//cin>>n;
		/*for (int i = 0; i < n; i++)
		{
			cin>>a[i]>>b[i];
		}*/

		cin>>r>>t;
		while(t>0)
		{
			white=pow(r,2);
			black=pow(r+1,2)-white;
			req=black;
			if (req<=t)
			{
				t=t-req;
				rings++;
			}
			else
			{
				break;
			}
			r=r+2;
		}


		/*for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < j; k++)
			{
				if ((a[j]<a[k] && b[j]>b[k] ) || (a[j]>a[k] && b[j]<b[k]))
				{
					count++;
				}
			}
		}*/
		cout<<"Case #"<<x+1<<": "<<rings<<endl;
	}
	return 0;

}