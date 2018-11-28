//#include <iostream>
#include <fstream>

using namespace std;

ifstream cin;
ofstream cout;

double search(double c, double f, double x)
{
	double time;
	double sum=0;
	double perCook = 2.0;
	time = x / perCook;
	while(true)
	{
		sum = sum + c / perCook;
		perCook += f;
		double tempTime = sum + x / perCook;
		if(time < tempTime)
		{
			break;
		}
		time = tempTime;
	}
	return time;
}

int main()
{
	cin.open("B-large.in");
	cout.open("B-large.out");
	int t;
	double c, f, x;
	cin>>t;
	cout << fixed << showpoint;         //fixedʹ�ö���С����ʽ, showpoint-ǿ����ʾС�����Լ�С������λ��.
	//cout << setprecision(2); 
	cout.precision(7);
	for(int i=0; i<t; ++i)
	{
		cin>>c>>f>>x;
		double res = search(c, f, x);
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}