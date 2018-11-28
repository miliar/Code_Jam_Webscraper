#include<iostream>
#include<fstream>
using namespace std;

int main()
{
 ifstream input;
 input.open("B-large.in");
 ofstream output;
 output.open("output.txt");
 int T;
 input>>T;
 int t=1;
 double c,f,x;
 

 while(t<=T)
	{
	 input>>c>>f>>x;
	 double i=2.0;
	 double time=0.0;
	 while(true)
	 	{
		 if(x/i<=(c/i+(x/(i+f))))
		 	{
			 time+=x/i;
			 break;
			}
		 else
			{
			 time+=c/i;
			 i=i+f;
			}
		}
	output.precision(7);

	output.setf( std::ios::fixed, std:: ios::floatfield ); 
	 output<<"Case #"<<t<<": "<<time<<endl;
	 t++;
	}
 return 0;
}
	 
