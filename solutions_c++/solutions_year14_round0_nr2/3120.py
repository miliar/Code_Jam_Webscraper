#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int T,no=1;
	cin>>T;
	double c,f,x,speed,time;
	while(T--)
	{
		cin>>c>>f>>x;
		speed=2.0;
		time=0.0;
		while(1)
		{
			double buyfarm=c/speed;
			double buyfarmwin=buyfarm+x/(speed+f);
			double win=x/speed;
			if(win>buyfarmwin){
				speed+=f;
				time+=buyfarm;
			}else{
				time+=win;
				break; 
			}
		}
		cout<<"Case #"<<no<<": ";
		cout<<fixed<<setprecision(7)<<time<<endl;
		no++;
	}
}

