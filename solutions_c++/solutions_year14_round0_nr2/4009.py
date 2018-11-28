#include <iostream>
#include <string>

#include <fstream>
#include <iomanip>
using namespace std; 

const int arr_size=4;


inline long double do_something (long double C, long double X, long double F,int y, long double& time_elapsed_completed_farms,int &complete_farms)
{
	long double time = X/((F*complete_farms) +2.000);
	time+=time_elapsed_completed_farms;

	
	time_elapsed_completed_farms+= C/((F*complete_farms) +2.000); //time taken to make 1 more farm
	complete_farms++;

	
	return time;
}

//
//bool is_it_time_to_end (vector<long double> times, node * my,int y,int& answer)
//{
//	if (y>500)
//	{
//		int smallest=0;
//		int index=0;
//		for (int x=1;x<times.size();x++)
//		{
//			if (times[x-1] <= times[x])
//			{
//				smallest++;
//			}
//			else
//			{
//				smallest=0;
//				answer=x;
//			}
//
//		}
//
//		if (smallest>20)
//		{
//			return true;
//		}
//		return false;
//	}
//	else
//		return false;
//}

int main ()
{
	
	try{
		ifstream fin;
		ofstream fout;
		fout.open("output.txt");
		fin.open("B-large.in");
		
		if (!fin.is_open() || !fout.is_open())
			throw "Input or output file not opening exception";
		else
		{
			int size=0;
			fin >> size;

			for (int x=0;x<size && fin.good();x++)
			{
				long double C;
				long double X;
				long double F;
				fin >> C;
				fin >> F;
				fin >> X;
				//vector<long double> times;
				long double time_elapsed_completed_farms=0;
				int complete_farms=0;


				long double min=LDBL_MAX;
				int lead=-1;
				for (int y=0;y<5000 || lead <2000;y+=1) // checks for a lead of 20
				{

					if (X<C)
					{
							min = X/2.000;
							break;
					}
					long double c = do_something(C,X,F,y,time_elapsed_completed_farms,complete_farms);
					if(c < min)
					{
						min=c;
						lead=0;
					}
					else
						lead++;

					if (y==4999)
					{
						lead=0;
					}

			
					

				}


				fout <<"Case #" <<x+1<<": ";
				fout << setprecision(10) <<min*1.0000000 <<endl;
				
			}
		}
	}
	catch (string a)
	{
		cout <<endl << "EXCEPTION : " << a <<endl;
	}
	return 0;
}
