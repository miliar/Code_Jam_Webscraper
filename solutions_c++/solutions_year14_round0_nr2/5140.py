#include<iostream>
#include<fstream>
using namespace std;

int main()
{
  

ifstream in;
in.open("a.txt");
ofstream out;
out.open("output.txt");


int N;
double C;
double F;
double X;
int I=0;
int a=1;

double w, wf;
in>>N;
double rate=2;
double t=0;

for(int n=0; n<N; n++)
{
	in>>C;
	in>>F;
	in>>X;
	while(a)
	{
			w=( X/rate ) + t;
			wf=((C/rate) + ( X/(rate+F)) ) + t;
			if(wf<w)
			{
				t+=C/rate;
				rate+=F;
			}
			else
			{
				a=0;
				t=w;	
			}
			
	}
	
	
	
	out.precision(7);
	out<<"Case #"<<fixed<<n+1<<": "<<t<<"\n";
	
	rate=2;
	t=0;
	a=1;
}

}	

