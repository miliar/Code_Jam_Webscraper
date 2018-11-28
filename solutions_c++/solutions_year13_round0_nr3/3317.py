#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

int main () {
	string line;
	int noOfCase;
	  
	ifstream myfile ("C-small-attempt0.in");
	if (myfile.is_open())
	{   
		ofstream myfileOut;
		myfileOut.open("output.out");
		getline(myfile,line);
		
		istringstream(line) >> noOfCase;
		
		for(int k=0;k<noOfCase;k++)
		{
			long long count=0;
			double A,B;
			getline(myfile,line);
			istringstream(line) >> A>>B;
			
			long long begin= (long long) floor(sqrt(A));
			long long end= (long long) ceil(sqrt(B));
			
			for (long long i=begin;i<=end;i++)
			{
				long long test=i*i;
				// check original no.
				bool valid=false;
				string testString;
				stringstream strstream;
				strstream<<i;
				strstream>>testString;
				double length =(double) testString.length();
				if (length==1)
				{
					valid=true;
				}
				else
				{
					
					string topString=testString.substr(0,floor(length/2));
					string swapString="";
					for (long long j=0;j<floor(length/2);j++)
						swapString.append(1,topString[floor(length/2)-1-j]);
					if (swapString.compare(testString.substr(ceil(length/2)))==0)
					{
						valid=true;
					}
				}
				
				// check sq no.
				if ((A<=test)&&(test<=B)&& valid)
				{
					string testString;
					stringstream strstream;
					strstream<<test;
					strstream>>testString;
					double length =(double) testString.length();
					if (length==1)
					{
						// cout<<testString<<endl;
						count++;
					}
					else
					{
						
						string topString=testString.substr(0,floor(length/2));
						string swapString="";
						for (long long j=0;j<floor(length/2);j++)
							swapString.append(1,topString[floor(length/2)-1-j]);
						if (swapString.compare(testString.substr(ceil(length/2)))==0)
						{
							// cout<<testString<<endl;
							count++;
						}
					}
				}
			}
			
				cout<<"Case #"<<k+1<<": "<<count<<endl;			
				myfileOut<<"Case #"<<k+1<<": "<<count<<endl;
			
		}
		
		myfileOut.close();				
		myfile.close();
	}
	else cout << "Unable to open file";
	
	return 0;
}