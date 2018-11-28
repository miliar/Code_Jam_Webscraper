#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Consonants

int main(void)
{
	ifstream input_file;
	input_file.open("QuestionA/A-small-attempt2.in");
	//input_file.open("QuestionA/input.in");

	ofstream output_file;
	output_file.open("QuestionA/A-small-attempt2.out", std::ios_base::trunc);
	//output_file.open("QuestionA/output.out", std::ios_base::trunc);

	int game_count;
	input_file >> game_count;
	for(int iter = 1; iter <= game_count; iter++)
	{
		// read word and n
		string word;
		int n;
		input_file >> word >> n;

		int size = word.size();		
		int count = 0;
		int found_last = -1;
		int current_pos = 0;
		for(int i = 0; i <= (size - n); i++)
		{			
			for(; current_pos < n; current_pos++)
			{
				if(word[current_pos + i] == 'a' ||
				   word[current_pos + i] == 'e' ||
				   word[current_pos + i] == 'i' ||
				   word[current_pos + i] == 'u' ||
				   word[current_pos + i] == 'o') break;
			}
			if(current_pos == n)
			{
				// total
				int comb = (i + 1) * (size - (i + n - 1));				
				if(found_last >= 0)
				{
					int diff = (found_last + 1) * (size - (i + n - 1));				
					comb -= diff;
				}
				found_last = i;				
				count += comb;
				current_pos = n - 1;
			}
			else
			{				
				current_pos = 0;
			}
		}

		output_file << "Case #" << iter << ": " << count << std::endl;
		
	}
	
	return 0;
}