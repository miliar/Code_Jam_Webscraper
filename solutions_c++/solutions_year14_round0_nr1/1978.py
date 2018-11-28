#include <fstream>

#define CARD_DIM 4

using namespace std;

ifstream fin("D:\\Input.txt");
ofstream fout("D:\\Output.txt");

int T;

int main(int argc, const char* argv[])
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		int a, b, cards_a[CARD_DIM][CARD_DIM], cards_b[CARD_DIM][CARD_DIM], answer = 0, answer_count = 0;

		fin >> a;
		for(int j = 0; j < CARD_DIM; j++)
			for(int k = 0; k < CARD_DIM; k++)
				fin >> cards_a[j][k];
		fin >> b;
		for(int j = 0; j < CARD_DIM; j++)
			for(int k = 0; k < CARD_DIM; k++)
				fin >> cards_b[j][k];

		for(int j = 0; j < CARD_DIM; j++)
			for(int k = 0; k < CARD_DIM; k++)
				if(cards_a[a - 1][j] == cards_b[b - 1][k])
					answer_count++, answer = cards_a[a - 1][j];
		fout << "Case #" << i + 1 << ": ";
		if(answer_count > 1)
			fout << "Bad magician!";
		if(answer_count == 1)
			fout << answer;
		if(answer_count < 1)
			fout << "Volunteer cheated!";
		fout << "\n";
	}
	return 0;
}