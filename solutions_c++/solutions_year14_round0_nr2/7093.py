#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
void main()
{
	double c=0.0, f=0, x=0.0;
	double mintime=0.0, lasttime=0.0, next=0.0;
	ifstream myfile ("B-large.in");
	ofstream out ("output.txt",ios::out);
	int testnum;
	int nn=0;

	myfile>>testnum;
	while(testnum>0)
	{
		nn++;
		myfile>>c;
		myfile>>f;
		myfile>>x;
		
		int forms=0;
		lasttime=0.0;
		mintime= x / 2 ;
		
		while(1){
			forms++;
			next=lasttime+(c/(((forms-1)*f)+2))+(x/((forms*f)+2));
			lasttime=lasttime+(c/(((forms-1)*f)+2));
			if(next<mintime){
				mintime=next;
			}
			else{
				break;
			}
		}
		out<<"Case #"<<nn<<": ";
		out.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed
		out << std::setprecision(9)<<mintime;
		out<<endl;
		testnum--;
	}
}