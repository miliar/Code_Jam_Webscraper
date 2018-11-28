#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;


void loadCards(vector<vector<int>>&cards,ifstream& in)
{
	for (int i = 0; i < cards.size(); i++)
	{
		for (int j = 0; j < cards.size(); j++)
		{
			int num;
			
			in >> num;
			cards[i][j] = num;
		}
	}
}

void getRow(vector<vector<int>>&cards, vector<vector<int>>&rows, int answer, int round)
{
	for (int r = 0; r < cards.size(); r++)
	{
		if (r != answer-1)
		{
			continue;
		}
		else
		{
			for (int c = 0; c < cards.size(); c++)
			{
				rows[round][c] = cards[r][c];
			}

			break;
		}
	}
}

int main()
{
	string file = "A-small-attempt0.in";
	string file2 = "A-small.txt";
	ifstream in;
	ofstream out;

	int T = 0;
	vector<vector<int>>cards;
	vector<vector<int>>rows;
	int solutions[2];

	cards.resize(4);

	rows.resize(2);

	
	for (int i = 0; i < cards.size(); i++)
	{
		cards[i].resize(4);
	}

	for (int i = 0; i < rows.size(); i++)
	{
		rows[i].resize(4);
	}
	
	in.open(file);
	out.open(file2);

	in >> T;

	for (int i = 1; i <= T; i++)
	{
		
		for (int j = 0; j < 2; j++)
		{
			int answer;

			in >> answer;

			loadCards(cards,in);

			getRow(cards, rows, answer, j);
		}

		int si = 0;
		for (int k = 0; k < 4; k++)
		{

			int num1 = rows[0][k];

			for (int l = 0; l < 4; l++)
			{
				int num2 = rows[1][l];

				if (num1 == num2)
				{
					solutions[si] = num1;

					si++;

				}
			}

			if (si > 1)
			{
				out << "Case #" << i << ": Bad magician!" << endl;
				break;
			}
		}

		
		if (si == 0)
		{
			out << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		else if (si==1)
		{
			out << "Case #" << i << ": " << solutions[0]<<endl;
		}


	}
	



}