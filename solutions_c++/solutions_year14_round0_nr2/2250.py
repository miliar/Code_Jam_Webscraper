#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{

	ifstream fin;
	fin.open("B-large.in");
	
	ofstream fout;
	fout.open("output.txt");

	
	short int t;
	
	double C,F,X,score,gain;
	double time;
	
	
	
	fin>>t;
	
	for(int i=0;i<t;i++)
	{
		
		score = time =0;
		gain= 2;
		
		fin>>C>>F>>X;
		
		
		while(score<X)
		{
			if(X/gain > (C/gain + X/(gain+F)))
			{
				// buy farm
				
				score = 0;
				time += C/gain;
				
				gain+=F;
				
				
				
			}
			
			else
			{
				time+= X/gain;
				score =X;
				
				
				
			}
			
			
			
			
			
			
		}
		
		
		
		fout<<"Case #"<<i+1<<": ";
		fout<<setprecision(7)<<showpoint<<fixed<<time;
		fout<<endl;
		
		
		
	}
	
	
	
	
	
	
	
	

	
}
