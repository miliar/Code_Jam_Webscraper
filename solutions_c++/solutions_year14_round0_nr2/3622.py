#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

double last_try_time;
double this_try_time;
double last_farm_time;
double salary;

int main()
{
	ifstream input_file;
	ofstream output_file;
	string line;
	int case_num = 0;

	input_file.open("test.in");
	if (!input_file)
	{
		cout<<"No File \"test.in\" Found!"<<endl;
	}
	output_file.open("test.out");
	if (!output_file)
	{
		cout<<"No File \"test.out\" Created!"<<endl;
	}
	input_file>>case_num;
	cout<<"Num:"<<case_num<<endl;

	for (int n = 1; n <= case_num; n++)
	{
		double c, f, x;
		input_file>>c>>f>>x;
		salary = 2.0;
		last_try_time = x / salary;
		last_farm_time = 0.0;
		this_try_time = 0.0;

		while(true)
		{
			this_try_time += c / salary;
			salary += f;
			last_farm_time = this_try_time;
			this_try_time += x / salary;

			if (this_try_time < last_try_time)
			{
				last_try_time = this_try_time;
				this_try_time = last_farm_time;
				continue;
			}
			else
			{
				break;
			}
		}

		output_file<<"Case #"<<n<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<last_try_time<<endl;
	}

	input_file.close();
	output_file.close();
	system("pause");
	return 0;
}