// ccc.cpp : 定义控制台应用程序的入口点。
//
#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
const int MAX=100005;
double fun1(double C,double F,double X)
{
	double v=2.0;
	double time=0.0;
	while(1)
	{
		if( (X/(v+F)+C/v) < (X/v) )
		{
			time+=C/v;
			v+=F;
			
		}
		if((X/(v+F)+C/v) >= (X/v))
		{
		    time+=X/v;
			break;
		}
	}
	return time;
}
void write1()
{  
  ifstream fileinput;
  fileinput.open("d:\\1a.in");
  ofstream output;
  output.open("d:\\output.in");
  int Num=0;
  double re[MAX];
  fileinput>>Num;
  cout<<Num<<endl;
  double aa=0,bb=0,cc;
   int n=0;
   for(int i=0;i<Num;i++)
    {
       fileinput>>aa>>bb>>cc;
	   output<<fixed<<setprecision(7)<<"Case #"<<i+1<<": "<<fun1(aa,bb,cc)<<endl;
    }
  fileinput.close();
  output.close();
}

int main()
{
	write1();
}
