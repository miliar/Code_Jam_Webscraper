#include <iostream>
#include <fstream>
#include <string>
#include<iomanip>

using namespace std;

class hey
{
	int nos,nums;
	
public:
	void get_data(void)
	{
	double input;
	double result;
	ifstream myfile; 
	int firstt=0;
	int i,j,k,count2=0;
	double p,q,r;
	myfile.open ("B-large.in");
	ofstream a_file ( "example.txt" );
	if (myfile.is_open())
	{
			while(myfile.eof() == false)
			{
				
				if(firstt==0)
				{		
					//	cout << "first \n";
						myfile>>input;
						nos=input;
						nums = nos*3;
						cout << "nos is " << nos  << "\n";
						firstt++;
				}
				/*
				else
				{
					for(i=0;i<nums;i++)
					{
						myfile >> input;
						p=input;
						cout << p << "\n";
					}
				}  */
				  
				for(i=0;i<nums;i+=3)
				{
					count2++;
					myfile >> p;
					myfile >> q;
					myfile >> r;
				//	cout << p << " " << q << " " << r << "\n";
					a_file << "Case #" << count2 << ": " ;
					a_file << fixed << setprecision(7) << processdata(p,q,r) << "\n";
				//	cout << processdata(p,q,r) << "\n";
				}
					myfile.close();
					a_file.close();
			}
	}	
	else
				cout << "Error opening file\n";
	}

	double processdata(double x, double y, double z)
	{
	//	cout << x << " "<< y <<" " << z << "\n";
		double time=0.0;
		double farm=0.0;
		double rate, towin, tofarm;
	while(1)
	{
		rate = 2+farm*y;
			tofarm=x/rate+z/(rate+y);
			towin=z/rate;	
		if(tofarm<towin)
		{
			farm=farm+1.0;
			time=time+x/rate;
		//	cout << "farm,time = " << farm << time << "\n";
		}
		else
		{
			time = time + towin;
			return time;
		}
	}
	}
	
	
	
}prog1;

int main()
{
	prog1.get_data();
}

