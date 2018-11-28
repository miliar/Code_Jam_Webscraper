#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int test_cases = 0;

	ifstream i_file;
	i_file.open("input.txt");
	i_file >> test_cases; 
	
	ofstream o_file;
	o_file.open("output.txt");

	int first_row_chosen;
	int second_row_chosen;
	int first_cards[4][4];
	int second_cards[4][4];

	int correct_counter[2];

	for (int i=0; i<test_cases; i++)
	{
		correct_counter[0] = 0;
		correct_counter[1] = 0;
		i_file >> first_row_chosen;
		first_row_chosen--;
		
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
				i_file >> first_cards[j][k];
		}

		i_file >> second_row_chosen;
		second_row_chosen--;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				i_file >> second_cards[j][k];

				if (j == second_row_chosen)
				{
					for (int l=0; l<4; l++)
					{
						if (second_cards[second_row_chosen][k] == first_cards[first_row_chosen][l])
						{
							correct_counter[0] = correct_counter[0] + 1;
							correct_counter[1] = first_cards[first_row_chosen][l];
						}
					}
				}

			}
		}

		if (correct_counter[0] == 1)
			o_file << "Case #" << i + 1 << ": " << correct_counter[1] << endl;
		else if(correct_counter[0] > 1)
			o_file << "Case #" << i + 1 << ": Bad magician!" << endl;
		else
			o_file << "Case #" << i + 1 << ": Volunteer cheated!" << endl;



	}

}