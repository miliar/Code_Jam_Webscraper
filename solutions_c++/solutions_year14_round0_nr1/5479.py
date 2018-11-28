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

		//	 Get first answer:
		int ans1;
		iss >> ans1;

		//	Cue up location.
		for (int i = 0; i < ans1; i++)
		{
			getline(fin, str);
		}
		iss.clear(); iss.str(str);
		vector <int> first_guess;
		
		for(int i = 0; i < 4; ++i)
		{
			int A;
			iss >> A;
			first_guess.push_back(A);
		}

		//	Cue up location.
		for(int i = ans1; i < 4; ++i)
		{
			getline(fin, str);
		}

		//	 Get second answer:
		getline(fin, str);
		iss.clear(); iss.str(str);
		int ans2;
		iss >> ans2;

		for (int i = 0; i < ans2; i++)
		{
			getline(fin, str);
		}

		iss.clear(); iss.str(str);
		vector <int> second_guess;

		for(int i = 0; i < 4; ++i)
		{
			int A;
			iss >> A;
			second_guess.push_back(A);
		}

		//	Cue up location.
		for(int i = ans2; i < 4; ++i)
		{
			getline(fin, str);
		}

		bool found_one (false);
		int ans = -1;
		for(auto it : first_guess)
		{
			for(auto it_it : second_guess)
			{
				if (it == it_it) 
				{
					if(found_one == false)
					{
						ans = it;
						found_one = true;
					}
					else
					{
						ans = -1;
						break;
					}
				}
			}
		}
		if (found_one && ans == -1)
		{
			fout << "Case #" << aaa+1 << ": " << "Bad magician!" << endl;
		}
		else if (found_one)
		{
			fout << "Case #" << aaa+1 << ": " << ans << endl;
		}
		else
		{
			fout << "Case #" << aaa+1 << ": " << "Volunteer cheated!" << endl;
		}
	}	

	fin.close(); fout.close();
	return 0;
}
