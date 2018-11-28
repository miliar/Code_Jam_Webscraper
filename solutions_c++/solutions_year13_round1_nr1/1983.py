#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

#define PI 3.14

using namespace std;

int main()
{
	int cases;
	long double r, t;
	cin >> cases;
	int c = 0;
	while(cases--)
	{
		long long int inner=0,outer=0,ans=0;
		cin >> r >> t;
		inner = r;
		outer = r+1;
		for(int i=0;t>=0;i++)
		{
			//cout<<"loopcount :"<<i+1<<endl;
			t -= (outer*outer) - (inner*inner);
			//cout<<"inner : "<<inner<<" outer : "<<outer<<" tvalue : "<<t<<" area : "<<(PI*outer*outer) - (PI*inner*inner)<<endl;
			if(t < 0)
			{
				break;
			}			
			outer+=2;
			inner+=2;
			ans++;
		}
		c = c+1;
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}