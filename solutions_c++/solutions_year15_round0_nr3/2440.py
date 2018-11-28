#include <iostream>
#include <sstream>
#include <climits>
#define SIZE 10000

using namespace std;
char input[SIZE];
char table[8][4];
//l = -1
//m = -i
//n = -j
//o = -k
void FillTable()
{
	table[0][0] = 'h'; table[0][1] = 'i'; table[0][2] = 'j'; table[0][3]='k';
	table[1][0] = 'i'; table[1][1] = 'l'; table[1][2] = 'k'; table[1][3]='n';
	table[2][0] = 'j'; table[2][1] = 'o'; table[2][2] = 'l'; table[2][3]='i';
	table[3][0] = 'k'; table[3][1] = 'j'; table[3][2] = 'm'; table[3][3]='l';

	table[4][0] = 'l'; table[4][1] = 'm'; table[4][2] = 'n'; table[4][3]='o';
	table[5][0] = 'm'; table[5][1] = 'h'; table[5][2] = 'o'; table[5][3]='j';
	table[6][0] = 'n'; table[6][1] = 'k'; table[6][2] = 'h'; table[6][3]='m';
	table[7][0] = 'o'; table[7][1] = 'n'; table[7][2] = 'i'; table[7][3]='h';
}
	
int main()
{
	int T = 0;
	string line;
	getline(std::cin, line);
	std::istringstream stream(line);
	stream >> T;
	FillTable();

	for(int i = 1; i <= T; i++)
	{
		unsigned long L;
		unsigned long X;
		getline(std::cin, line);
		std::istringstream stream1(line);
		stream1 >> L >> X;
		getline(std::cin, line);
		std::istringstream stream(line);
		for (int j=0; j < L; j++) {
			stream >> input[j];
		}

		char result = 'h';
		int pos = 0;
		for(int x = 0; x < X; x++)
		{
			for(int y = 0; y < L; y++)
			{
				result = table[result - 'h'][input[y] - 'h'];
				if(pos == 0 && result == 'i')
				{
					pos = 1;
					result = 'h';
				}
				if(pos == 1 && result == 'j')
				{
					pos = 2;
					result = 'h';
				}
				if(pos == 2 && result == 'k')
				{
					pos = 3;
					result = 'h';
				}
			}
		}

		if(pos == 3 && result == 'h')
			cout << "Case #" << i << ": YES" << endl;
		else
			cout << "Case #" << i << ": NO" << endl;
		
	}
}