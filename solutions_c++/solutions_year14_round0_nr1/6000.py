#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream input_data;
	input_data.open("A-small-attempt0.in");
	ofstream output_data;
	output_data.open("MagicTrickOutput.txt");

	int T(0); // number of test cases
	//string strN;
	//getline(input_data, strN);
	input_data >> T;
	// loop through all test cases
	for (int i = 0; i < T; i++)
	{
		// Vector of results
		vector<int> results;
		// First Row of answers
		int first_row1[4], first_row2[4], first_row3[4], first_row4[4];
		int first_row_value(0);
		input_data >> first_row_value;
		// Fill first row
		for (int r = 0; r < 4; r++)
		{
			input_data >> first_row1[r];
		}
		// Fill second row
		for (int r = 0; r < 4; r++)
		{
			input_data >> first_row2[r];
		}
		// Fill thrid row
		for (int r = 0; r < 4; r++)
		{
			input_data >> first_row3[r];
		}
		// Fill fourth row
		for (int r = 0; r < 4; r++)
		{
			input_data >> first_row4[r];
		}

		// Second row of answers
		int second_row1[4], second_row2[4], second_row3[4], second_row4[4];
		int second_row_value(0);
		input_data >> second_row_value;
		// Fill first row
		for (int r = 0; r < 4; r++)
		{
			input_data >> second_row1[r];
		}
		// Fill second row
		for (int r = 0; r < 4; r++)
		{
			input_data >> second_row2[r];
		}
		// Fill thrid row
		for (int r = 0; r < 4; r++)
		{
			input_data >> second_row3[r];
		}
		// Fill fourth row
		for (int r = 0; r < 4; r++)
		{
			input_data >> second_row4[r];
		}

		// Now check which rows have common factors
		switch  (first_row_value)
		{
		case 1:
			// Check the second values too
			switch (second_row_value)
			{
			case 1:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row1[i] == second_row1[j])
						{
							results.push_back(first_row1[i]);
						}
					}
				}
				break;
			case 2:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row1[i] == second_row2[j])
						{
							results.push_back(first_row1[i]);
						}
					}
				}
				break;
			case 3:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row1[i] == second_row3[j])
						{
							results.push_back(first_row1[i]);
						}
					}
				}
				break;
			case 4:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row1[i] == second_row4[j])
						{
							results.push_back(first_row1[i]);
						}
					}
				}
				break;
			}
			break;
		case 2:
			switch (second_row_value)
			{
			case 1:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row2[i] == second_row1[j])
						{
							results.push_back(first_row2[i]);
						}
					}
				}
				break;
			case 2:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row2[i] == second_row2[j])
						{
							results.push_back(first_row2[i]);
						}
					}
				}
				break;
			case 3:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row2[i] == second_row3[j])
						{
							results.push_back(first_row2[i]);
						}
					}
				}
				break;
			case 4:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row2[i] == second_row4[j])
						{
							results.push_back(first_row2[i]);
						}
					}
				}
				break;
			}
			break;
		case 3:
			switch (second_row_value)
			{
			case 1:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row3[i] == second_row1[j])
						{
							results.push_back(first_row3[i]);
						}
					}
				}
				break;
			case 2:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row3[i] == second_row2[j])
						{
							results.push_back(first_row3[i]);
						}
					}
				}
				break;
			case 3:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row3[i] == second_row3[j])
						{
							results.push_back(first_row3[i]);
						}
					}
				}
				break;
			case 4:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row3[i] == second_row4[j])
						{
							results.push_back(first_row3[i]);
						}
					}
				}
				break;
			}
			break;
		case 4:
			switch (second_row_value)
			{
			case 1:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row4[i] == second_row1[j])
						{
							results.push_back(first_row4[i]);
						}
					}
				}
				break;
			case 2:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row4[i] == second_row2[j])
						{
							results.push_back(first_row4[i]);
						}
					}
				}
				break;
			case 3:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row4[i] == second_row3[j])
						{
							results.push_back(first_row4[i]);
						}
					}
				}
				break;
			case 4:
				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						if (first_row4[i] == second_row4[j])
						{
							results.push_back(first_row4[i]);
						}
					}
				}
				break;
			}
			break;
		}
		// Now check how many values are in the results vector
		if (results.size() == 1)
		{
			output_data << "Case #" << (i + 1) << ": " << results[0] << endl;
		}
		else if (results.size() > 1)
		{
			output_data << "Case #" << (i + 1) << ": Bad magician!" << endl; 
		}
		else if (results.size() == 0)
		{
			output_data << "Case #" << (i + 1) << ": Volunteer cheated!" << endl;
		}
	}
	input_data.close();
	output_data.close();
	return 0;
}