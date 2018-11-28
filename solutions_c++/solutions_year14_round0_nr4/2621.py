#include <iostream>
#include <sstream>
#include <fstream>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in;
	in.open ("D-large.in");
	
	ofstream out;
	out.open ("output_large.txt");
	
	int t;
	in >> t;
	
	int length = 0;
	int count_D = 0;
	int count_W = 0;
	
	for (int i=0; i<t; i++)
	{
		count_D = 0;
		int count_W = 0;
		
		in >> length;
		double naomi[length];
		double ken[length];
		
		for (int j=0; j<length; j++)
		{
			in >> naomi[j];
		}
		for (int j=0; j<length; j++)
		{
			in >> ken[j];
		}
		
		sort (naomi, naomi+length);
		sort (ken, ken+length);

		for (int j=0, k=0; j<length; j++)
		{
			for (; k<length; k++)
			{
				if (ken[j] < naomi[k])
				{
					count_D++;
					k++;
					break;
				}
			}
		}
		for (int j=0, k=0; j<length; j++)
		{
			for (; k<length; k++)
			{
				if (naomi[j] < ken[k])
				{
					count_W++;
					k++;
					break;
				}
			}
		}
		
		out << "Case #" << i+1 << ": " << count_D << " " << length-count_W << endl;
	}
	
	in.close();
	out.close();
	
	return 0;
}
