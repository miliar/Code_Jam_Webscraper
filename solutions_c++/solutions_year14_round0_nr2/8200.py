#include<iostream>
#include<cstdlib>
#include<iomanip>
#include<conio.h>
using namespace std;
int tc;
double ans[100];

int main()
{
	cin>>tc;
	for(int z=0;z<tc;z++)
	{
		double coo,f_r,g,e,farm,temp,sum,r=2,t2=0;
	
		cin>>coo>>f_r>>g;
		
		while(1)
		{
			e = g/r;
			
			farm = coo/r;
			
			temp = g/(r+f_r);
			
			sum = farm+temp;
			
			if(e<sum)
			{
				t2 += e;
				break;
			}
			else
			{
				r += f_r;
				t2 += farm;
			}
		}
		ans[z]=t2;
	}
	
	cout.setf(ios::fixed,ios::floatfield);
	cout.setf(ios::showpoint);
	cout.precision(7);	
	
	for(int z=0;z<tc;z++)
	{
		cout<<"Case #"<<z+1<<": "<<ans[z]<<endl;
	}
	
	
	getch();	
	return 0;
}
