//#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
#define min(a,b) a>b ?a:b
double C,F,X;

double solve()
{
	
	double old=0, current=0;
	double time;
	double slope=2;
	old=X/slope;
	current=old;
	while(current<=old)
	{
		old=current;
		current=old-X/slope+C/slope;
		slope+=F;
		current+=X/slope;

	}
	return old;
}
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("B.txt");
	cout.open("large_output.txt");
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{

		cin>>C>>F>>X;
		cout<<"Case #"<<i+1<<": "<<setprecision(32)<< solve()<<endl;
	}
	cin.close();
	cout.close();
	return 0;
}