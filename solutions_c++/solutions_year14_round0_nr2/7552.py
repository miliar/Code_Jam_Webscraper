#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	cout<<setprecision(7)<<fixed;
	int n, t=1;
	cin>>n;
	for(int i=0; i<n; i++)
	{
		double c,f,x;
		double ir=2, ar=ir, fr;
		double t1, t2, ft=0;
		cin>>c>>f>>x;

		while(true)	
		{
			t1 = x / ar;
			t2 = (c/ar) + (x/(ar+f));
			if(t1 <= t2)
			{
				ft+=t1;
				break;
			}
			else
			{				
				ft += c/ar;
				ar += f;				
			}			
		}
		cout<<"Case #"<<t<<": "<<ft<<endl;
		t++;
	}
	
	return 0;	
}