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


int find_moves(const vector<int> & l, int a)
{
	int ret = 0;
	for(auto it_l : l)
	{
		ret += abs(it_l - a);
	}
	return ret;
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
	
	//	Number of test cases.
	const int T = atoi(str.c_str());

	//	Loop across each file.
	for( int aaa = 0; aaa < T ; aaa++)
	{
		getline(fin, str);
		istringstream iss(str);

		//	 Data
		string str_in;
		int N;
		iss >> N;

		bool solveable = true;
		vector<string> list_strings;
		vector<vector<int> > count_char;
		vector<char> char_order_true;
		for(int bbb = 0; bbb < N ; ++bbb)
		{
			getline(fin, str);		iss.clear(); iss.str(str);
			list_strings.push_back(str);

			//	Read char:
			//	ALso count char.
			vector<char> char_order;
			vector<int> count_char_single;
			char last_char = '-';
			int last_char_count = 1;
			for(int loop_c = 0; loop_c < str.size(); ++loop_c)
			{
				if(last_char != str[loop_c])
				{
					char_order.push_back(str[loop_c]);
					if(last_char != '-')
					{
						count_char_single.push_back(last_char_count);
					}
					last_char = str[loop_c];
					last_char_count = 1;
				}
				else
				{
					last_char_count++;
				}

				if(loop_c == str.size() - 1)
				{
					count_char_single.push_back(last_char_count);
				}
			}

			count_char.push_back(count_char_single);

			if(bbb == 0)
			{
				char_order_true = char_order;
			}
			//	Test if order same:
			else
			{
				if (char_order_true.size() != char_order.size())
				{
					solveable = false;
					break;
				}
				for(int loop_order = 0; loop_order < char_order.size(); ++loop_order)
				{
					if(char_order[loop_order] != char_order_true[loop_order])
					{
						solveable = false;
							break;
					}
				}
				if (!solveable)
				{
					break;
				}
			}
		}

		//	Test the count:
		int moves_needed = 0;

		//	Loops across characters.
		for(int loop_c = 0; loop_c < char_order_true.size(); ++loop_c)
		{
			int minVal = 1000;
			//	Loops across each possible option.
			for(int loop_cc = 0; loop_cc < count_char.size(); ++loop_cc)
			{
				//	From vec:
				vector<int> temp;
				//	Same as above.
				for(int ccc = 0; ccc < count_char.size(); ++ccc)
				{
					temp.push_back(count_char[ccc][loop_c]);
				}
				minVal = min(minVal, find_moves(temp, count_char[loop_cc][loop_c]));
			}
			moves_needed += minVal;
		}


		if(solveable)
		{
			fout << "Case #" << aaa+1 << ": " << moves_needed << endl;
		}
		else
		{
			fout << "Case #" << aaa+1 << ": " << "Fegla Won" << endl;
		}
		//fout << fixed << setprecision(10) << "Case #" << aaa+1 << ": " << setprecision(10) << static_cast<double>(prob)<< setprecision(10) <<  endl;

	}	

	fin.close(); fout.close();
	return 0;
}
