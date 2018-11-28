#include<iostream>
#include<fstream>
#include<conio.h>
#include<iomanip>
using namespace std;
int test;
double C[100];
double F[100];
double X[100];


double calculate(int testcase)
{
	double time = 0.0;
	double rate = 2.0;
	double Xtime = X[testcase]/rate;
	double FTime = C[testcase]/rate;
	double temp_rate = rate+F[testcase];
	double temp_xtime = time + Xtime;
	double temp_ftime = time + FTime;
	
	while(temp_xtime > temp_ftime)
	{
		time  +=FTime;
		rate = temp_rate;
		FTime = C[testcase]/rate;
		Xtime = X[testcase]/rate;
		temp_xtime = time+Xtime;
		temp_rate = rate + F[testcase];
		temp_ftime = time+FTime+(X[testcase]/temp_rate);
		
	}
    time+=Xtime;
	return time;
}
void main()
{
	ifstream read("C:\\Users\\SwatiSh\\Downloads\\2.txt");
	ofstream write;
	write.open("C:\\Users\\SwatiSh\\Downloads\\output.txt");
	read >> test;
    for (int i = 0; i < test; ++i)
	{
		read>>C[i]>>F[i]>>X[i];
		write<<"Case #"<<(i+1)<<": "<<fixed<<setprecision(7)<<calculate(i)<<endl;
	}
	read.close();
	write.close();
	getch();
}