#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

char **data;
int row = 4;
int col = 4;

int main()
{
	int tests;
	int count;
	int dots;
	char winner;
	bool won;
	ifstream in("data.in", ifstream::in);
	in >> tests;
	for(int i = 0; i < tests; i++)
	{
		won = 0;
		dots = 0;
		char temp;
		data = (char **)malloc(sizeof(char*)*row);
		for(int k = 0; k < row; k++)
		{
			*(data+k) = (char*)malloc(sizeof(char)*col);
		}
		for(int j = 0; j < row; j++)
			for(int k = 0; k < col; k++)
				in >> data[j][k];
		for(int j = 0; j < row; j++)
		{
			count = 0;
			temp = data[j][0];
			if(temp == 'T')
				temp = data[j][3];
			if(temp != '.')
			for(int k = 0; k < col; k++)
			{
				if(data[j][k] == temp || data[j][k] == 'T')
					count ++;
				if(data[j][k] != '.')
					dots ++;
			}
			if(count == 4)
			{
				won = 1;
				winner = temp;
			}
		}
		for(int j = 0; j < col; j++)
		{
			count = 0;
			temp = data[0][j];
			if(temp == 'T')
				temp = data[3][j];
			if(temp != '.')
			for(int k = 0; k < row; k++)
				if(data[k][j] == temp || data[k][j] == 'T')
					count ++;
			if(count == 4)
			{
				won = 1;
				winner = temp;
			}
		}
		count = 0;
		temp = data[0][0];
		if(temp == 'T')
			temp = data[1][1];
		if(temp != '.')
		for(int p = 0; p < 4; p ++)
			if(data[p][p] == temp || data[p][p] == 'T')
					count ++;
		if(count == 4)
		{
			won = 1;
			winner = temp;
		}

		count = 0;
		temp = data[3][0];
		if(temp == 'T')
			temp = data[0][3];
		if(temp != '.')
		for(int p = 0; p < 4; p ++)
			if(data[3-p][p] == temp || data[3-p][p] == 'T')
					count ++;
		if(count == 4)
		{
			won = 1;
			winner = temp;
		}
		if(!won && dots != 16)
			cout << "Case #" << i+1 << ":" << " Game has not completed" << endl;
		if(won)
			cout << "Case #" << i+1 << ": " << winner <<  " won" << endl;
		else if(dots == 16)
			cout << "Case #" << i+1 << ":" << " Draw" << endl;
	}
	cin.get();
	return 0;
}
