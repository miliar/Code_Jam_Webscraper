#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin("B-small-attempt1.in",ios::in);
    ofstream fout("B-small.out",ios::out);
    
    double cur_r=2.0;int cur_co=0;
    double rate,farm,win,x1,x2,x3,x4;
	
	int cur=0,T;
    fout<<setprecision(7)<<fixed;
	fin>>T;
    double time[T];
    for(int i=0;i<T;i++)
    time[i]=0.0;
	while(cur++<T)
	{
	time[cur]=0.0,cur_r=2.0,cur_co=0;
	fin>>farm>>rate>>win;
	
	do
	{				//loop for seconds
	cur_co=(double)cur_co+cur_r;
	if(farm<=cur_co )
	{
	//cout<<"\n"<<cur_co <<" " <<cur_r;
	time[cur]=time[cur]+(farm/cur_r);	
	cur_co=(double)cur_co-farm;
	cur_r=cur_r+rate;
	}
	x1=farm/cur_r;
	x4=cur_r+rate;
	x2=win/x4;
	x3=win/cur_r;
	}
	while((x1+x2)<x3);
	time[cur]=time[cur]+x3;
	fout<<"\nCase #"<<cur<<": "<<time[cur];
	}
getch();
return 0;
}
	
    

