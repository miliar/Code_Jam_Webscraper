#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <fstream>

using namespace std;


int main()
{
	ifstream infile;
	ofstream myfile;
	myfile.open("output.txt");
	infile.open("C-small-attempt0.in");

	bool fair, square, flag = true;
	long long unsigned n, a, b, count;
	//cin>>n;
	string line;
	infile>>n;

	for(int k =1; k<=n; k++)
	{
		infile>>a>>b;
		count = 0;		
		for(int i = a; i<=b; i++)
		{
			fair = false, square = false;
			if(i<10)
			{
				if(i==1)
					count++;
				else
					if(i==4)
						count++;
					else
						if(i==9)
							count++;
			}
			else
			if(i<100)
			{
				ostringstream ss;
				ss << i;
				line = ss.str();
				if(line[0] == line [1])
				{
					fair = true;
				}
				if(fair)
				{
					double d_sqrt = sqrt(double(i));
					int i_sqrt = d_sqrt;
					if ( d_sqrt == i_sqrt )
						square = true;
				}
				if(square)
					count++;
			}
			else
				if(i<1000)
				{
					ostringstream ss;
					ss << i;
					line = ss.str();
					if(line[0] == line [2])
					{
						fair = true;
					}
					if(fair)
					{
						double d_sqrt = sqrt(double(i));
						int i_sqrt = d_sqrt;
						if ( d_sqrt == i_sqrt )
						{
							ostringstream ss;
							ss << i_sqrt;
							line = ss.str();
							if(line[0] == line [1])
								square = true;
						}
					}
					if(square)
						count++;
				}
				else
					if(i==1000)
						break;
		}
		//cout<<count<<endl;
		myfile<<"Case #"<< k <<": "<<count<<endl;
	}
	infile.close();
	myfile.close();
	return 0;
}