#include <iostream>
#include <fstream>
#include <unordered_set>

using namespace std;

// Lawnmower

int main(void)
{
	ifstream input_file;
	input_file.open("round2/B-large.in");

	int games;
	
	ofstream output_file;
	output_file.open("round2/output-large.out", std::ios_base::trunc);

	input_file >> games;
	for(int game = 1; game <= games; game++)
	{
		int N;
		int M;
		input_file >> N >> M;
		int * input = new int[N * M];
		int total = (N * M);
		for(int i = 0; i < total; i++)
		{
			input_file >> input[i];
		}

		unordered_set<int> used_rows;
		unordered_set<int> used_cols;

		while(true)
		{
			if(used_rows.size() == N || used_cols.size() == M)
			{
				output_file << "Case #" << game << ": YES" << endl;
				break;
			}
			
			// find minimum
			int min_row = -1;
			int min_col = -1;
			int min = 200;
			for(int i = 0; i < N; i++)
			{
				if(used_rows.find(i) != used_rows.end()) continue;
				for(int j = 0; j < M; j++)
				{
					if(used_cols.find(j) != used_cols.end()) continue;

					if(input[(i * M) + j] < min)
					{
						min = input[(i * M) + j];
						min_row = i;
						min_col = j;
					}
				}
			}

			// check whole row & column to be same 
			bool row_check = true;
			bool col_check = true;
			// row
			for(int j = 0; j < M; j++)
			{
				if(input[(min_row * M) + j] > min)
				{
					row_check = false;
					break;
				}
			}
			// column
			for(int i = 0; i < N; i++)
			{
				if(input[(i * M) + min_col] > min)
				{
					col_check = false;
					break;
				}
			}

			if((row_check || col_check) == false)
			{
				output_file << "Case #" << game << ": NO" << endl;
				break;
			}

			if(row_check) used_rows.insert(min_row);
			else if(col_check) used_cols.insert(min_col);
		}
	}

	input_file.close();
	output_file.close();

	return 0;
}