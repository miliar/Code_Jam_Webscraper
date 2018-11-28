#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open("boutput2.txt");
	int cases;
	double time,rate,c,f,x;//c is cost of 1 farm, f is increase in cookie production, x is victory condition
	cin>>cases;
	for(int i=0;i<cases;i++)
	{
		time=1000000;
		cin>>c>>f>>x;
		double temp,n=0;//temp is time taken, n is number of farms tested
		for(;;)
		{
			temp=0;
			rate=2.0;
			for(int j=0;j<n;j++)
			{
				temp+=c/rate;
				rate+=f;
			}
			temp+=x/rate;
			if(temp<=time)
			{
				time=temp;
				n++;
				continue;
			}
			else if(temp>time)
			{
				break;
			}
		}
		myfile<<fixed<<setprecision(7)<<"Case #"<<i+1<<": "<<time<<endl;	
	}
	myfile.close();
	return 0;
}
