#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <functional>
#include <numeric>
#include <iomanip>
using namespace std;


int main(int argc, char * argv[])
{
	ifstream fin("input.txt"); 
	ofstream fout("output.txt");
	
	if(!fin.good())
	{
		cout << "opps" << endl;
	}

	string str;
	getline(fin, str);
	
	//	Number of test cases.
	const int T = atoi(str.c_str());

	//	Loop across each file.
	for( int aaa = 0; aaa < T ; aaa++)
	{
		getline(fin, str);
		istringstream iss(str);
		//iss.clear(); iss.str(str);

		//	 Data
		long double C,F,X;
		iss >> C >> F >> X;

		//	Number of farms:
		long double temp = (2 + F ) / X - 2 / (X - C);
		long double divideby = F / (X - C ) - F / X;
		long double farms = temp / divideby; 
		//int farms_true = max(int(std::ceil (farms)), 0);
		int farms_true = max(int(-std::floor (-farms)), 0);

		if ( C > X ) 
		{
			farms_true = 0;
		}

		//	Compute time to get farms_true:
		long double current_time(0.0);
		for (int i = 0; i < farms_true; i++)
		{
			current_time += C / (2 + i * F);
		}
		current_time += X / (2 + farms_true * F);

		cout << fixed << setprecision(10) << "Case #" << aaa+1 << ": " << setprecision(10) << static_cast<long double>(current_time)<< setprecision(10) <<   "\t" << farms_true << endl;
		//fout << "Case #" << aaa+1 << ": " << fin_ans << endl;
		//fout << fixed << setprecision(10) << "Case #" << aaa+1 << ": " << setprecision(10) << static_cast<long double>(current_time)<< setprecision(10) <<  "\t" << farms << "\t" << farms_true << endl;
		fout << fixed << setprecision(10) << "Case #" << aaa+1 << ": " << setprecision(10) << static_cast<long double>(current_time)<< setprecision(10) << endl;
	}	

	fin.close(); fout.close();
	return 0;
}
