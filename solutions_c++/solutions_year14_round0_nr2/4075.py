#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;


int main ()
{
	ifstream ifile;
	ifile.open("B-large.in");
	ofstream ofile;
	ofile.open("outputB.txt");

	int total;
	
	ifile>>total;

	double C , F ,X , rate = 2 , time=0 , curr=0;

	for(int i=0  ; i<total ; i++)
	{
		rate = 2;
		curr = time = 0;
		ifile>>C>>F>>X;

		while(true)
		{
			
			if((X-C)/rate <= X/(rate+F))
			{
				time+=X/rate;
				break;
			}
			else
			{
				time += C/rate;
				rate += F;
			}

		}
		/*a=time;
		b=(time-a)*1000000000;*/
		/*ofile<<"Case #"<<i+1<<": "<<a<<".";
		if(!b)
			ofile<<"0000000"<<endl;
		else ofile<<b<<endl;*/
		//cout<<fixed<<setprecision(7)<<time<<endl;
		ofile<<"Case #"<<i+1<<": "<<fixed<<setprecision(10)<<time<<endl;
	}
	ofile.close();
	ifile.close();
	return 0;
}