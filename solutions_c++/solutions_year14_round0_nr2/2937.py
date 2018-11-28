#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;
int main(){
	cout<<fixed;
	int t;
	cin >>t ;
	for (int it = 1; it <= t ; it++)
	{
		double c,f,x,ans=0,r=2.0;
		cin>>c>>f>>x;
		while(1){
			double tm1,tm2;
			tm1=x/r;
			tm2=(c/r)+(x/(r+f));
			if(tm1<tm2)
			{
				ans+=tm1;
				break;
			}
			ans+=c/r;
			r+=f;
		}
		cout<<"Case #"<<it<<": "<<setprecision(7)<<ans<<"\n";
	}
	
	return 0;
}

