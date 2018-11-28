#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

struct numo
{
	double value;
	bool naomi;
};

double getNextLarge(vector<numo> list, double numo::*value, double a)
{
	for(int i = 0; i < list.size(); i++)
	{
		if(!list[i].naomi && list[i].value > a)
		{
			return i;
		}
	}
	return -1;
}



bool getVal(numo a, numo b)
{
	return a.value < b.value;
}

bool largerThanAll(double val, vector<numo> *list, double numo::*value)
{
	for(int i = 0; i < list->size(); i++)
	{
		if(!(*list)[i].naomi && (*list)[i].value < val)
		{
			(*list)[i].naomi = true;
			return true;
		}
	}
	return false;
}

int main()
{
	string line;
	ifstream myfile ("test.txt");
	ofstream ofile;
	int numOfTestCases = 0;
	vector<numo> naomi;
	vector<numo> ken;
	int result = 0;
	int cheat = 0;
	ofile.open("result.txt");
	ofile.precision(7);
	ofile.setf( std::ios::fixed, std:: ios::floatfield );
	if (myfile.is_open())
	{
		getline(myfile, line);
		numOfTestCases = atoi(line.c_str());
		for(int i = 0; i < numOfTestCases; i++)
		{	
			int num;
			getline(myfile, line);
			num = atoi(line.c_str());
			getline(myfile, line);
			std::istringstream is( line );
			double n;
			
			for(int j = 0; j < num; j++)
			{
				numo a;
				is >> n;
				a.value = n;
				a.naomi = true;
				naomi.push_back(a);
			}
			getline(myfile, line);
			std::istringstream is1( line );
			for(int j = 0; j < num; j++)
			{
				numo a;
				is1 >> n;
				a.value = n;
				a.naomi = false;
				ken.push_back(a);
			}
			sort(naomi.begin(), naomi.end(), getVal);
			sort(ken.begin(), ken.end(), getVal);

			

			for(int j = 0; j < naomi.size(); j++)
			{
				if(largerThanAll(naomi[j].value, &ken, &numo::value))
				{
					cheat++;
				}
			}

			for(int j = 0; j < ken.size(); j++)
			{
				ken[j].naomi = false;
			}

			for(int j = 0; j < naomi.size(); j++)
			{
				double large = getNextLarge(ken, &numo::value, naomi[j].value);
				if( large == -1 )
				{
					result++;
				}
				else
				{
					ken[large].naomi = true;
				}
			}

			ofile << "Case #" << i + 1 << ": " << cheat << " " << result;
			naomi.clear();
			ken.clear();
			result = 0;
			cheat = 0;
			ofile << endl;
		}
		myfile.close();
	}

	else cout << "Unable to open file"; 
	ofile.close();
	return 0;
}


