#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	double time_to_wait = 0;
	double time_to_buy = 0;
	int j = -1;
	ifstream inputfile("input2.txt");
	char s[100];
	double c = 0;
	double f = 0;
	double x = 0;
	string output = "";

	inputfile.getline(s,4);
	int k = atoi(s);

	for(int n=0;n<k;n++)
	{
		output += "Case #"+to_string(n+1) +": ";
		double least_time = 10000000000;
		inputfile.getline(s,100);
		int counter = 0;
		string number = "";
		j = -1;
		for(int m=0 ; s[m]!=0 ; m++ )
		{
			if(s[m] != ' ')
			{
				number += s[m];
			}
			else
			{
				if(counter == 0)
				{
					c = atof(number.c_str());
					number = "";
					counter ++;
				}
				else if(counter == 1)
				{
					f = atof(number.c_str());
					number = "";
					counter ++;
				}
			}
		}
		x = atof(number.c_str());
		while (true)
		{
			bool finish = false;
			double total_time = 0;
			int i=0;
			double gain = 2;
			while(!finish)
			{
				time_to_buy = (c/gain);
				time_to_wait = (x/gain);
				if(i <= j)
				{
					total_time += time_to_buy;
					gain += f;
				}
				else
				{
					total_time += time_to_wait;
					finish = true;
				}
				i ++ ;
			}
			if(total_time < least_time)
			{
				least_time = total_time;
			}
			else
			{
				break;
			}
			j++;
		}

		cout << least_time << endl;
		output += to_string(least_time)+"\n";
	}

	ofstream outputfile("out2.txt");
	outputfile << output ; 

	system("pause");

	return 0;
}