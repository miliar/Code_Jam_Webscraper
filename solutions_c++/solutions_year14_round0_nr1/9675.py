#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

#define GRID_DIM 4
#define MAX_BUFFER 16
#define VOLUNTEER_CHEATED "Volunteer cheated!"
#define BAD_MAGICIAN "Bad magician!"

void readMatrix(FILE *f, int (*matrix)[GRID_DIM][GRID_DIM])
{
	int i, j =0;
	int data = 0;
	
	for (i = 0; i < GRID_DIM; i++)
    {
        for (j = 0; j < GRID_DIM; j++)
        {
			fscanf_s(f, "%d", &(*matrix)[i][j]);
        }
	}
}

void readData(FILE *f, int *answer1, int (*firstGrid)[GRID_DIM][GRID_DIM], int *answer2, int (*secondGrid)[GRID_DIM][GRID_DIM])
{
	fscanf_s(f, "%d", &(*answer1));
	readMatrix(f, firstGrid);

	fscanf_s(f, "%d", &(*answer2));
	readMatrix(f, secondGrid);
}

vector<int> getRow(int answer, int grid[GRID_DIM][GRID_DIM])
{
	int i, j = 0;
	vector<int> possible_cards;
	
	for (i = 0; i < GRID_DIM; i++)
	{
		if (i == (answer - 1)) 
		{
			for (j = 0; j < GRID_DIM; j++)
			{
				possible_cards.push_back(grid[i][j]);
			}
		}
	}

	return possible_cards;
}

void getResults(vector<int> possibleCards1, vector<int> possibleCards2, int *nrPossibleCards, int *volunteerCard)
{
	int i, j = 0;
	int nr = 0;
	int sizePossibleCards1 = possibleCards1.size();
	int sizePossibleCards2 = possibleCards2.size();
	
	for (i=0; i<sizePossibleCards1; i++)
	{
		for (j=0; j<sizePossibleCards2; j++)
		{
			if (possibleCards1[i] == possibleCards2[j])
			{
				*volunteerCard = possibleCards1[i];
				nr++;
			}
		
		}
	}

	*nrPossibleCards = nr;
}

void solve(int nrPossibleCards, int volunteerCard, std::string &output)
{
	if (nrPossibleCards == 0)
	{
		output.append(VOLUNTEER_CHEATED);
	}
	else if (nrPossibleCards == 1)
	{
		char str[MAX_BUFFER] = {0};
		sprintf_s(str, "%d", volunteerCard);
		output.append(str);
	}
	else
	{
		output.append(BAD_MAGICIAN);
	}
}

void writePretext(int i, std::string &output)
{
	char str[MAX_BUFFER] = {0};

	output.assign("Case #");
	
	sprintf_s(str, "%d", i);
	output.append(str);
	
	output.append(": ");
}

int main(int argc, char **argv)
{
	// input variables 
	int T = 0;
	FILE *fin = NULL;
	FILE *fout = NULL;
	const char *filename = argv[1];
	const char * filename_out = "out.txt";

	// output variables
	int nrPossibleCards = 0;
	int volunteerCard = -1;
	std::string output;
	

	fin = fopen(filename, "r");
	if (fin == NULL)
	{
		printf("Could not open file %s\n", filename);
		exit(-1);
	}

	fout = fopen(filename_out, "w+");
	if (fout == NULL)
	{
		printf("Could not open file %s\n", filename_out);
		exit(-1);
	}

	fscanf_s(fin, "%d", &T);

	for (int i = 1; i <= T; i++)
	{
		int answer1 = 0;
		int answer2 = 0;
		
		int firstGrid[GRID_DIM][GRID_DIM] = {0};
		int secondGrid[GRID_DIM][GRID_DIM] = {0};
		
		readData(fin, &answer1, &firstGrid, &answer2, &secondGrid);
		
		vector<int> possibleCards1 = getRow(answer1, firstGrid);
		vector<int> possibleCards2 = getRow(answer2, secondGrid);
	
		getResults(possibleCards1, possibleCards2, &nrPossibleCards, &volunteerCard);

		writePretext(i, output);

		solve(nrPossibleCards, volunteerCard, output);
		
		fprintf(fout, "%s\n", output.c_str());
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
