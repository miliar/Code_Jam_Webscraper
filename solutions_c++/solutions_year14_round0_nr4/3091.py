// Google Code Jam
// Qualification Round Problem 4
// Deceitful War
//

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int play_ken(double told, double* blocks, int num_blocks);
int play_naomi(double& told, double* blocks, int num_blocks);
int play_deceit(double& told, double* blocks, double* ken_blocks, int num_blocks);

int main(int argc, char** argv)
{
	if(argc < 2)
	{
		cout << "Argument required: Input file." << endl;
		return 1;
	}

	ifstream file_in;
	ofstream file_out;

	int num_problems;
	double *blocks_naomi, *blocks_ken, *blocks_naomi2, *blocks_ken2;
	int chosen_naomi, chosen_ken;

	cout.precision(5);
	cout << fixed << showpoint;
	file_out << fixed << showpoint;
	file_out.precision(5);

	file_in.open(argv[1], ios::in);
	if(!file_in.is_open())
	{
		cerr << "Error opening input file!" << endl;
		return 2;
	}
	
	file_out.open("output.txt", ios::out);
	if(!file_out.is_open())
	{
		cerr << "Error opening output file!" << endl;
		return 3;
	}

	// Read number of problems
	
	file_in >> num_problems;

	cout << num_problems << " in input set." << endl;

	for(int problem = 0; problem < num_problems; problem++)
	{
		// Read number of blocks
		int num_blocks;
		file_in >> num_blocks;

		// Create arrays
		blocks_naomi = new double[num_blocks];
		blocks_ken = new double[num_blocks];
		blocks_naomi2 = new double[num_blocks];
		blocks_ken2 = new double[num_blocks];

		// Read blocks in
		for(int i = 0; i < num_blocks; i++) file_in >> blocks_naomi[i];
		for(int j = 0; j < num_blocks; j++) file_in >> blocks_ken[j];

		// Copy blocks into secondary arrays
		for(int i = 0; i < num_blocks; i++)
		{
			blocks_naomi2[i] = blocks_naomi[i];
			blocks_ken2[i] = blocks_ken[i];
		}

		int score_norm = 0;
		int score_deceit = 0;

		// Play round of the game, getting the normal outcome.

		for(int i = 0; i < num_blocks; i++)
		{
			//cout << "Round " << i << endl;
			//cout << "--------" << endl;
			
			double n_told = 0.0F;
			int n_chosen = play_naomi(n_told, blocks_naomi, num_blocks);
			int k_chosen = play_ken(n_told, blocks_ken, num_blocks);

			//cout << "Naomi chose block " << n_chosen << ", which has a mass of " << blocks_naomi[n_chosen] << endl;
			//cout << "Ken chose block " << k_chosen << " in response, with a mass of " << blocks_ken[k_chosen] << endl << endl;	

			if(blocks_naomi[n_chosen] > blocks_ken[k_chosen]) score_norm++;

			blocks_naomi[n_chosen] = 0.0;
			blocks_ken[k_chosen] = 0.0;
		}

		// Play round of the game, getting the 'deceitful' outcome

		for(int i = 0; i < num_blocks; i++)
		{
			cout << "Round " << i << endl;
			cout << "--------" << endl;
			
			double n_told = 0.0F;
			int n_chosen = play_deceit(n_told, blocks_naomi2, blocks_ken2, num_blocks);
			int k_chosen = play_ken(n_told, blocks_ken2, num_blocks);

			cout << "Naomi chose block " << n_chosen << ", saying it was " << n_told << ", which has a mass of " << blocks_naomi2[n_chosen] << endl;
			cout << "Ken chose block " << k_chosen << " in response, with a mass of " << blocks_ken2[k_chosen] << endl << endl;	

			if(blocks_naomi2[n_chosen] > blocks_ken2[k_chosen]) score_deceit++;

			blocks_naomi2[n_chosen] = 0.0;
			blocks_ken2[k_chosen] = 0.0;
		}

		cout << "Round " << problem+1 << ": Naomi's score is " << score_norm << " | " << score_deceit << endl << endl;

		file_out << "Case #" << problem+1 << ": " << score_deceit << " " << score_norm << endl;

	}
	
	file_in.close();
	file_out.close();
	return 0;
}

int play_ken(double told, double* blocks, int num_blocks)
{
	// Ken will choose the block that will barely defeat
	// Naomi's told choice if he has one, otherwise
	// choose lightest block
	
	int idex = 0;
	for(int i = 0; i < num_blocks; i++)
	{
		if(blocks[i] <= 0.0) 
		{
		   	if(idex == i)idex++;	
			continue;
		}
		if(blocks[i] > told)
		{
			if(blocks[idex] < told)
			{
				idex = i;
			}
			else
			{
				if(blocks[idex] > blocks[i])
				{
					idex = i;
				}
			}
		}
	}

	if(blocks[idex] > told)
	{
		return idex;
	}
	else
	{
		for(int i = 0; i < num_blocks; i++)
		{
			if(blocks[i] == 0.0) continue;
			if(blocks[i] < blocks[idex]) idex = i;
		}
	}

	return idex;
}

int play_naomi(double& told, double* blocks, int num_blocks)
{
	// Naomi's normal play will consist of 'blindly' playing
	// the blocks from highest value to lowest value

	int idex = 0;
	for(int i = 0; i < num_blocks; i++)
	{
		if(blocks[i] <= 0.0) 
		{
		   	if(idex == i)idex++;	
			continue;
		}
		if(blocks[i] > blocks[idex])
		{
			idex = i;
		}
	}

	told = blocks[idex];

	return idex;
}

int play_deceit(double& told, double* blocks, double* ken_blocks, int num_blocks)
{
	// Play lowest block, tell as being higher than highest block.
	// Ken will always try to 'discard' his lowest block in these situations.
	
	// First test for special case of there being only two blocks left
	int nblocks = 0;
	for(int i = 0; i < num_blocks; i++) 
		if(blocks[i] != 0.0) nblocks++;

	int ldex = 0;
	for(int i = 0; i < num_blocks; i++) // Get our lowest block
	{
		if(blocks[i] == 0.0)
		{
			if(ldex == i) ldex++;
			continue;
		}

		if(blocks[i] < blocks[ldex]) ldex = i;
	}

	// Get Ken's lowest block and highest block.
	int kldex = 0, khdex = 0;
	for(int i = 0; i < num_blocks; i++)
	{
		if(ken_blocks[i] == 0.0)
		{
			if(kldex == i) kldex++;
			if(khdex == i) khdex++;
			continue;
		}

		if(ken_blocks[i] < ken_blocks[kldex]) kldex = i;
		if(ken_blocks[i] > ken_blocks[khdex]) khdex = i;
	}

	// Check if our lowest block is enough to defeat Ken's lowest block.
	
	if(blocks[ldex] > ken_blocks[kldex])
	{
		// If it is, we play our lowest, but say it's higher than his highest
		// block, forcing him to play his lowest.

		told = ken_blocks[khdex]+0.00001;
		return ldex;
	}
	else
	{
		// Otherwise we do a discard play (Play our lowest to force Ken to discard highest)
		told = ken_blocks[khdex]-0.00001;
		return ldex;
	}
}
