#include<iostream>
#include<fstream>
#include<iomanip>

void main()
{
	using namespace std;
	ifstream fin("b_small_in.txt");
	ofstream fout("b_small_out.txt");
	fout<<fixed<<setprecision(7);

	int count;
	fin>>count;
	for(int i=1;i<=count;i++)
	{
		double C,F,X;
		fin>>C>>F>>X;
		double total_time=X/2;
		double a=0;
		int farms=0;
		bool con=1;

		do
		{
			farms++;
			a=0;
			for(int j=0;j<farms;j++)
			{
				a=a+(double)C/(2+F*j);
			}
			a=a+(double)X/(2+F*farms);
			if(total_time>=a)
			{
				double x;
				x=total_time;
				total_time=a;
				a=x;
			}
			else
			{
				con=0;
			}

			
		}while(con);
		
		fout<<"Case #"<<i<<": "<<total_time<<endl;
	}
}