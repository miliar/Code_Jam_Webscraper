#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	double test,costoffarm,ratepersecond,requiredcookies,i,j,x,time=0,counter;
	int k=1,x1;
	ofstream fout;
	ifstream fin; 
	fout.open("output.txt");
	fin.open("B-large.in");
	fin>>test;
	fout.precision(7);
	while(test--)
	{
		fin>>costoffarm>>ratepersecond>>requiredcookies;
		if(costoffarm-requiredcookies>=0)
		{
			x=requiredcookies/2;
			fout<<"Case"<<" "<<"#"<<k<<":"<<" "<<fixed<<x<<"\n";
		}
		else
		{
			counter=2;
				while(1)
		
		{
				if(requiredcookies/counter > ((costoffarm/counter)+requiredcookies/(counter+ratepersecond)))
				{
				time=time+(costoffarm/counter);
			//	cout<<time<<"\n";
				counter=ratepersecond+counter;
				}
			else
				break;
				
			}
		
			
			time=time+(requiredcookies/counter);
			fout<<"Case"<<" "<<"#"<<k<<":"<<" "<<fixed<<time<<"\n";
		}
		k++;
		time=0;
		counter=0;
	}
	return 0;
}

