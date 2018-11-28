#include <iostream>
#include <iomanip>
#include<math.h>
#include<algorithm>
#include<cstdio>
#include<stdlib.h>
#include<string.h>
#include<vector>

using namespace std;

int main() {
	int T,a=0; long double c,f,x,time,ptime,rate,temp,one=1,mintime=999999;
	 freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>T;
	while(T--)
	{
		a++;

		time=0;
		rate=2;
		cin>>c>>f>>x;
		time+=c/rate;
		rate+=f;
		ptime=x/2;
		cout<<"Case #"<<a<<": ";

		while(1)
		{
			if(x<=2)
			{
				cout<<std::fixed;
				cout<<std::setprecision(7)<<x/2<<endl;
				break;
			}

			if(ptime<(time+(x/rate)))
			{
				cout<<std::fixed;
				cout<<std::setprecision(7)<<ptime<<endl;
					break;
			}
			else
			ptime=time+(x/rate);
			time+=(c/rate);
			rate+=f;
			}

	}
	return 0;
}
