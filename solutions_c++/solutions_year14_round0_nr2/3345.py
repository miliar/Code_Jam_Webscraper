#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include <iomanip>
#include<fstream>

using namespace std;
double output_test[100];

double output(double C,double F,double X)
{
	double time = 0.0000000;
	double time1 = X/2.0;
	double time2 = C/2.0 + X/(2.0+F);
	double per_second = 2.0;
	//int count = 1;
	while(true)
	{
	    if(time1 > time2)
	    {
			//cout<<count++<<endl;
		    time = time + C/per_second;
			per_second = per_second + F;
			time1 = X/per_second;
			time2 =  C/per_second + X/(per_second + F);
	    }
		else
		{
			time = time + X/per_second;
			break;
		}
	}
	
	return time;
}
int main(int argc, char* argv[])
{
	int m;
	fstream file1;
	double C,F,X;
	file1.open("e:\\B-small-attempt2.txt",ios::in);
	file1>>m;
	for(int i = 0;i < m;i++)
	{
		file1>>C;
		file1>>F;
		file1>>X;
		output_test[i] = output(C,F,X);		
		cout<<setprecision(5)<<output_test[i];
	}
	ofstream file2;
	file2.open("e:\\a-out.txt",ios::out);
	file2.setf(file2.showpoint);
	file2.precision(6);
	file2.setf(ios::fixed);
	for(int j = 0;j < m;j++)
	{
		file2<<"Case #";
		file2<<j+1;
		file2<<": ";
		file2<<output_test[j];
		
		file2<<"\n";
	}
	file2.close();
	system("pause");
	return 0;
}

