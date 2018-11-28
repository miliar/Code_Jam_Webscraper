#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#include <cmath>

using namespace std;


int main()
{

	int n;
	
	
	ofstream fout;
	ifstream fin ("input.in");
	fout.open("reault.out ");
	fin>>n;

	int start,end;

	int a = 10;
	stringstream ss;
	ss << a;
	string str ;
	bool fairSquare=true;
	
	for(int u=0;u<n;u++)
	{
		fin>>start;
		fin>> end;
		fairSquare=true;
		int count=0;
		for(int i=start;i<=end;i++)
		{
			fairSquare=true;
			stringstream ss;
			ss<<i;
			str = ss.str();
			if(str.size()%2!=0)
			{
				for(int r=0;r<1+(str.size()/2);r++)
				{
					if(str[r]!=str[str.size()-r-1])
						fairSquare=false;

				}
				if(fairSquare)
				{
					double root=sqrt(double(i));
					stringstream sr;
					sr<<root;
			
					str = sr.str();
			
					if(str.size()%2!=0 ||str.size()==2)
					{
						for(int r=0;r<1+(str.size()/2);r++)
						{
							if(str[r]!=str[str.size()-r-1])
						
								fairSquare=false;
						}
					}
					else 
						fairSquare=false;
				}
			}
			else 
				fairSquare=false;

			if(fairSquare)
			
				count++;
			


	}
		fout<<"Case #"<<u+1<<": "<<count<<endl;

	}

	return 0;	
}