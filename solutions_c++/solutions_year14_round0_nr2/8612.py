#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;
	ifile.open("A-small-attempt0.in");
	if (ifile.fail())
	{
		exit(1);
	}
	ofile.open("cookie_output.in");
	if (ofile.fail())
	{
		exit(1);
	}
	int test_case;
	ifile >> test_case;
	
	bool bflag = false;
	for (int i = 1; i <= test_case; i++)
	{
		ofile << setprecision(12);
		double cost = 0.0, time = 0.0, rate = 0.0, rate1 = 2, time_comp = 0.0, temp_time = 0.0, target = 0.0;
		ifile >> cost >> rate >> target;
		time_comp = target;
		bflag = true;
		temp_time = target*1.0 / rate1;
		while (bflag == true)
		{
			if (temp_time < time_comp)
			{
				time_comp = temp_time;
				time += (cost*1.00 / (rate1*1.00));
				rate1 += rate;
				temp_time = target*1.0 / (rate1*1.0) + time;
			}
			else
				bflag = false;
		}
		ofile << "Case #" << i << ": " << time_comp << endl;
	}
	ifile.close();
	ofile.close();
	return 0;
}