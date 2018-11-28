#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <list>
#include <algorithm>

using namespace std;

int quaternions[5][5] = 
{
	{0, 0, 0 , 0 , 0 },
	{0, 1, 2 , 3 , 4 },
	{0, 2, -1, 4 , -3},
	{0, 3, -4, -1, 2 },
	{0, 4,  3, -2, -1}
};

int multiplicative_structure(int number1, int number2)
{
	int sign;
	if (number1 * number2 < 0) sign = -1;
	else									     sign =  1;

	return quaternions[abs(number1)][abs(number2)] * sign;
}

bool break_string(const string& s, long long x)
{
	int overal_string = 1;
	for (const char &ch : s) {	
		overal_string = multiplicative_structure(overal_string, ch - 'g');
	}

	int overal = 1;
	for (long long i = 0; i < x; i++) {
		overal = multiplicative_structure(overal, overal_string);
	}

	if (overal != -1)
		return false;

	int target = 2;
	int accum  = 1;
	for (long long i = 0; i < x; i++) {

		for (int j = 0; j < s.length(); j++)
		{
			accum = multiplicative_structure(accum, s[j] - 'g');
			if (accum == target) {

				if (target == 2) {

					accum  = 1;
					target = 3;
				}
				else {
					if (i == x - 1 && j == s.length() - 1)
						return false;

					return true;
				}
			}
		}
	}

	return false;
}

int main()
{
	//string file_name = "sample";

	string file_name = "C-small-attempt0";
	//string file_name = "A-large";	

	ofstream output_file(file_name + ".out");
	ifstream input_file (file_name + ".in");	

	int no_tests;
	if (input_file >> no_tests) {

		for (int test = 0; test < no_tests; test++) {

			long long l, x;						
			if (input_file >> l >> x) {
					
				string s;
				input_file >> s;
				bool ok = break_string(s, x);
				
				string yes_no;
				if (ok)	yes_no = "YES";
				else		yes_no = "NO" ;
				
				output_file << "Case #" << (test + 1) << ": " << yes_no << std::endl;
			
			} 
			else
				output_file << "Case #" << (test + 1) << ": " << "Error reading m and n" << std::endl;
		}
	}

	input_file .close();
	output_file.close();

	return 0;
}