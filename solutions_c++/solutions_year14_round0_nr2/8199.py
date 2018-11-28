#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <istream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

int main(int argc,char* argv[])
{
	cout.setf(ios::fixed);
	ifstream infile;
        infile.open(argv[1]);
	string cases;
	getline(infile,cases);
	int count = atoi(cases.c_str());
	
	for(int tc_i=0;tc_i<count;tc_i++)
	{
		cout<<"Case #"<<tc_i+1<<": ";
		string line;
		getline(infile,line);

		char *temp;
       	 	char *str;

        	str = new char[line.length()];
        	for (int i2=0; i2< line.length(); i2++)
        	{
                	str[i2] = line[i2];
        	}

        	temp = strtok (str," ");
        	double to_buy = atof(temp);

                temp = strtok (NULL," ");
                double accrual_addition =  atof(temp);

		temp = strtok (NULL," ");
                double to_win = atof(temp);

		double accrual_rate = 2;
		double total_time = 0;
		
		double seconds_to_buy_farm = to_buy/accrual_rate;
		double total_time_to_buy_farm = seconds_to_buy_farm;
		double seconds_to_win = to_win/accrual_rate;
		double total_time_to_win = seconds_to_win;

		accrual_rate += accrual_addition;

		while(true)
		{
			seconds_to_buy_farm = to_buy/accrual_rate;
			double old_total_time_to_buy_farm = total_time_to_buy_farm;
			total_time_to_buy_farm = total_time_to_buy_farm + seconds_to_buy_farm;
			seconds_to_win = to_win/accrual_rate;
			double old_total_time_to_win = total_time_to_win;
			total_time_to_win = old_total_time_to_buy_farm + seconds_to_win;
			
			if(total_time_to_win>=old_total_time_to_win) 
			{
				cout << setprecision(7) << old_total_time_to_win <<endl;
				break;
			}

			accrual_rate += accrual_addition;

		}
		

	}
		
}
