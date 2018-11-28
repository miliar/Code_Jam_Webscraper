#include<iostream>
#include<stdio.h>
#include <iomanip>

using namespace std;
int main()
{
    int t;
	cin>>t;
	std::cout << std::setprecision(12);
    int k=1;
    for(k=1;k<=t;k++)
    {
        double x,y,z;
		cin>>x>>y>>z;
        double ans=0;
        double cnt=2.0;
		//std::cout << std::setprecision(9) <<z/cnt<< '\n';
        while(z/cnt>x/cnt+z/(cnt+y)){
        ans+=x/cnt;
        cnt+=y;
        }
        ans+=z/cnt;
        cout<<"Case #"<<k<<": "<<ans<<'\n';
    }
}
