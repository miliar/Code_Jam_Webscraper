#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void ProcessLine(string _line, double _arr[])
{
	int space_pos = _line.find(' ');
	_arr[0] = stod(_line.substr(0, space_pos).c_str());

	_line = _line.substr(space_pos + 1);
	space_pos = _line.find(' ');
	_arr[1] = stod(_line.substr(0, space_pos).c_str());

	_line = _line.substr(space_pos + 1);
	space_pos = _line.find(' ');
	_arr[2] = stod(_line.substr(0, space_pos).c_str());
}

int main()
{
	cout.precision(7);
	ofstream output;
	output.open("output.txt");

	ifstream input;
	input.open("B-large.in");

	string temp = "";
	getline(input, temp);

	int test_cases = atoi(temp.c_str());
	for (int test = 0; test < test_cases; ++test)
	{
		getline(input, temp);
		double line[3];
		ProcessLine(temp, line);

		double time = 0;
		double cookies = 0, cookies_per = 2, extra_cookies_per = line[1], cost_farm = line[0], max_cookies = line[2];
		while (true)
		{
			double time_for_farm_win = cost_farm / cookies_per + max_cookies / (cookies_per + extra_cookies_per);
			double time_for_win = max_cookies / cookies_per;

			//cout << "\tT4FW: " << time_for_farm_win << "\tTFW:  " << time_for_win << endl;

			if (time_for_win < time_for_farm_win)
			{
				time += max_cookies / cookies_per;
				//cout << "T: " << time << endl;
				break;
			}
			else
			{
				time += cost_farm / cookies_per;
				cookies_per += extra_cookies_per;
				//cout << "T: " << time << endl;
			}
		}
		output << "Case #" << test + 1 << ": " << fixed << time << endl;;
	}
	output.close();
	return 0;
}