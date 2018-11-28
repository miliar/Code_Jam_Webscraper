#include<iostream>
#include<cstdlib>
#include<iomanip>

using namespace std;
int tc;
double ans[100];

int main()
{
	cin>>tc;
	for(int z=0;z<tc;z++)
	{
		double c_f,f_r,g,et_c,et_farm,et_temp,et_total,c_r=2,el_time=0;
	
		cin>>c_f>>f_r>>g;
		
		while(1)
		{
			et_c = g/c_r;
			
			et_farm = c_f/c_r;
			
			et_temp = g/(c_r+f_r);
			
			et_total = et_farm+et_temp;
			
			if(et_c<et_total)
			{
				el_time += et_c;
				break;
			}
			else
			{
				c_r += f_r;
				el_time += et_farm;
			}
		}
		ans[z]=el_time;
	}
	
	cout.setf(ios::fixed,ios::floatfield);
	cout.setf(ios::showpoint);
	cout.precision(7);	
	
	for(int z=0;z<tc;z++)
	{
		cout<<"Case #"<<z+1<<": "<<ans[z]<<endl;
	}
	
	
		
	return 0;
}
