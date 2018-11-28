#include <string>
#include <fstream>
#include <vector>

using namespace std;

int process_audience(string& s)
{
	int extra_friends = 0;
	int no_of_standings = 0;
	for (int i = 0; i < s.length(); i++) {
		
		if (s[i] == '0')
			continue;

		if (no_of_standings < i) {

			extra_friends += i - no_of_standings;
			no_of_standings = i;
		}

		no_of_standings += s[i] - '0';
	}

	return extra_friends;
}

int main()
{
	// string file_name = "sample";

	//string file_name = "A-small-attempt0";
	string file_name = "A-large";	

	ofstream output_file(file_name + ".out");
	ifstream input_file (file_name + ".in");	

	int no_tests;
	if (input_file >> no_tests) {

		for (int test = 0; test < no_tests; test++) {

			int n;			
			string s;
			if (input_file >> n >> s) {
												
				int number_of_friends_invited = process_audience(s);
				output_file << "Case #" << (test + 1) << ": " << fixed << number_of_friends_invited << std::endl;
			} 
			else
				output_file << "Case #" << (test + 1) << ": " << "Error reading m and n" << std::endl;
		}
	}

	input_file .close();
	output_file.close();

	return 0;
}