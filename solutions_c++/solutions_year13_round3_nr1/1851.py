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

unsigned int iter_factorial()
{
    return 0;
}


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
	
	const int T = atoi(str.c_str());

	for( int aaa = 0; aaa < T ; aaa++)
	{
		getline(fin, str);
		istringstream iss(str);

		//	 Data
		string str_in;
		int n;
		iss >> str_in >> n;
		//cout << str_in << " " << n << endl;


		int answer [100][100];
		int ans = 0;

		for (int str_start = 0; str_start <= str_in.length() - n; ++ str_start)
		{
			if(str_in.substr(str_start, n).find_first_of("aoeui") == string::npos)
			{
				answer[n][str_start] = 1;
				//cout << str_start << endl;
			}
			else
			{
				answer[n][str_start] =0;
			}
		}

		for (int str_leng = n+1 ; str_leng <= str_in.length() ; ++str_leng)
		{
			for (int str_start = 0; str_start <= str_in.length() - str_leng; ++str_start)
			{
				int str_lo, str_mid, str_hi;

				str_mid = str_start;
				str_hi = str_start+1;


				answer[str_leng][str_start] = max(
					answer[str_leng-1][str_mid], 
					answer[str_leng-1][str_hi]);
				if (answer[str_leng][str_start] !=0)
				{
					answer[str_leng][str_start]=1;
					//cout << str_leng << " " << str_start << " " << str_mid << " " << str_hi << endl;
				}
			}
		}

		int fin_ans =0 ;
		for (int str_leng = n ; str_leng <= str_in.length() ; ++str_leng)
		{
			for (int str_start = 0; str_start <= str_in.length() - str_leng; ++str_start)
			{
				if(answer[str_leng][str_start] != 0)
				{
					//cout << answer[str_leng][str_start] << endl;
					fin_ans++;
				}
			}
		}


		fout << "Case #" << aaa+1 << ": " << fin_ans << endl;
		//fout << fixed << setprecision(10) << "Case #" << aaa+1 << ": " << setprecision(10) << static_cast<double>(prob)<< setprecision(10) <<  endl;

	}	

	fin.close(); fout.close();
	return 0;
}
