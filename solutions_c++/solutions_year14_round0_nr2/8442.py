#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
ifstream inFile;
ofstream outputFile;
void main()
{
int i=1,t;
double c,f,x;
inFile.open("inputL.txt", ios::in);
outputFile.open("output.txt",ios::out|ios::trunc);
outputFile<<setprecision(7)<<fixed;
inFile>>t;
while(inFile>>c>>f>>x)
{
	double time =2.0,min=0.0,cur=0.0,total=0.0;
	int flag=1;
	min=x/time;
	while(flag)
	{
		cur=total;
		cur=cur+(c/time);
		time=time+f;
		cur=cur+(x/time);
		if(cur<=min)
		{
			min=cur;
			total+=c/(time-f);
		}
		else
		{
			total+=x/(time-f);
			flag=0;
		}
	}
	outputFile<<"Case #"<<i++<<": ";
	outputFile<<total<<endl;
}
}
