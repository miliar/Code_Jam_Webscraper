#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
		int test;
		cin>>test;
		int ct=0;
		cout<<fixed<<setprecision(7);
		while(ct<test)
		{
				ct++;
				double c,f,x;
				cin>>c>>f>>x;
				double time=0;
				double speed=2;
				while(c/f*(speed+f)<x+0.01)
				{
						time+=c/speed;
#ifdef DEBUG	
						cout<<"SPEED "<<c/speed<<endl;
#endif

						speed+=f;
#ifdef DEBUG
						cout<<"BUG "<<speed<<endl;
#endif
				}
				time+=x/speed;
				cout<<"Case #"<<ct<<": ";

				cout<<time<<endl;
		}
		return 0;
}

