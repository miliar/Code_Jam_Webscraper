#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <ctype.h>
#include <algorithm>
#include <math.h>
#include <conio.h>
using namespace std;

int main()
{
	ifstream in;
	in.open("C-small-attempt0.in");
	
	ofstream out;
	out.open("output.txt");
	
	int noc;
	in >> noc;
	
	int start = 0, limit = 0;
	int flag = 0;
	int count = 0;
	double root;
	
	for (int i=0; i<noc; i++)
	{
		in >> start;
		in >> limit;
		count = 0;
		
		for (int j=start; j <= limit; j++)
		{
			flag = 0;
			
			stringstream buffer;
			buffer << j;
			string num = buffer.str();
			
			//cout << num << endl;
			
			
			//for (int a=0, b=num.length()-1; a<num.length()/2 && b>num.length()/2; a++, b--)
			for (int a=0, b=num.length()-1; a<b; a++, b--)
			{
				if (num[a] == num[b])
					continue;
				else
				{
					flag = 1;
					break;
				}
			}
			if (flag == 0)
			{
				root = sqrt(j);
				
				stringstream buffer1;
				buffer1 << root;
				string numroot = buffer1.str();
				
				//unsigned found = numroot.find(".");
				//if (found==string::npos)
				//{
				//	for (int a=0, b=numroot.length()-1; a<numroot.length()/2 && b>numroot.length()/2; a++, b--)
					for (int a=0, b=numroot.length()-1; a<b; a++, b--)
					{
						if (numroot[a] == numroot[b])
							continue;
						else
						{
							flag = 1;
							break;
						}
					}
				//}
				//else
				//	flag = 1;
			}
			if (flag == 0)
				count++;
		}
		
		out << "Case #" << i+1 << ": " << count << endl;
		
	}
	
	return 0;
}
