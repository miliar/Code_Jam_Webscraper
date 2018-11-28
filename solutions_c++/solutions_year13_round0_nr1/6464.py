#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool Search(string str, char occ)
{
	return str.find_first_of(occ) != string::npos;
}

char GetWinner(string line)
{
	if(!Search(line, 'O') && !Search(line, '.')) return 'X';
	else if(!Search(line, 'X') && !Search(line, '.')) return 'O';
	
	return '.';
}

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");

	int T;
	input >> T;
	input.ignore();

	for(int test = 1 ; test <= T ; ++test)
	{
		char winner = '.';
		bool filled = true;
		string line;
		vector<string> m;
		for(int i = 0 ; i < 4 ; ++i)
		{
			getline(input,line);
			m.push_back(line);

			// Horizontal Checks
			if(filled && Search(line, '.'))
				filled = false;
			else if(winner == '.')
				winner = GetWinner(line);
		}

		getline(input,line);

		if(winner == '.')
		{
			// Verticals Checks
			for(int x = 0 ; x < 4 && winner == '.' ; ++x)
			{
				string line;
				for(int y = 0 ; y < 4 ; ++y)
					line.push_back(m[y][x]);

				winner = GetWinner(line);
			}
		}

		if(winner == '.')
		{
			// Diagonals Checks
			string d1, d2;
			for(int i = 0 ; i < 4 ; i++)
			{
				d1.push_back(m[i][i]);
				d2.push_back(m[3-i][i]);
			}

			winner = GetWinner(d1);
			if(winner == '.')
				winner = GetWinner(d2);
		}

		output << "Case #" << test << ": ";
		if(winner == '.')
		{
			if(filled)
				output << "Draw";
			else
				output << "Game has not completed";
		}
		else
			output << winner << " won";

		if(test + 1 <= T)
			output << endl;
	}

	input.close();
	output.close();
}