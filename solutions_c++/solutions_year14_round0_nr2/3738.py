#include<iostream>
#include<cmath>
#include <iomanip>
#include<vector>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	double c,f,x,F,cur,temp,val,pre;
	
	long count=1,cases;
	vector<double> values;
	cin>>cases;
	while(cases--)
	{
		cin>>c>>f>>x;
		
		F = 2.0;

		pre = 0;
		val = pre+x/F;
		
		while(true)
		{
			pre+=c/F;
			F+=f;
			temp = pre+x/F;
			if(val>=temp)
				val = temp;
			else if(val<temp)
				break;
		}


		cout<<"Case #"<<count<<": "<<fixed<<setprecision(7)<<val<<endl;
		count++;
	}
	return 0;
}