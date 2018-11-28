#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>

using namespace std;

char winner;
int flag_win = 0; // 0 no win, 1 win
int flag_rest = 0; // 1 = draw, 2 = not finished

void eval_row(char arr[4])
{
	//cout << arr[0] << arr[1] << arr[2] << arr[3] << endl;
	int x, o, dot, t;
	x = o = dot = t = 0;

	flag_win = 0;
	
	for (int i = 0; i < 4; i++)
	{
		switch (arr[i])
		{
		case 'X':
			x++;
			break;
		case 'O':
			o++;
			break;
		case '.':
			dot++;
			break;
		case 'T':
			t++;
			break;
		default:
			break;
		}
	}

	//cout <<"x"<<x<<"o"<<o<<"t"<<t<<endl;


	if (x == 3 && t == 1)
	{
		winner = 'X';
		flag_win = 1;
		return;
	}
	if (x == 4)
	{
		winner = 'X';
		flag_win = 1;
		return;
	}
	if (o == 3 && t == 1)
	{
		winner = 'O';
		flag_win = 1;
		return;
	}
	if (o == 4)
	{
		winner = 'O';
		flag_win = 1;
		return;
	}
}

int eval_state(vector<string> lines_in, int start_point)
{
	char field[16];
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			field[(4*i)+j] =
				lines_in[start_point+i][j];
			//cout << field[(4*i)+j] << endl;
		}
	}

	// horizontal check

	for (int i = 0; i < 16; i++)
	{
		char a, b, c ,d;
		a = field[i];
		b = field[++i];
		c = field[++i];
		d = field[++i];
		//cout << a << b << c << d << endl;
		char row_arr[4] = {a, b, c, d};
		eval_row(row_arr);
		
		if (flag_win == 1) return 1;
	}

	// vertical check

	for (int i = 0; i < 4; i++)
	{
		char a, b, c ,d;
		a = field[i];
		b = field[i+4];
		c = field[i+8];
		d = field[i+12];
		//cout << a << b << c << d << endl;
		char row_arr[4] = {a, b, c, d};
		eval_row(row_arr);
		
		if (flag_win == 1) return 1;
	}

	// diagonal check one

	{
		char a, b, c, d;
		a = field[0];
		b = field[5];
		c = field[10];
		d = field[15];

		char row_arr[4] = {a, b, c, d};
		eval_row(row_arr);

		if (flag_win == 1) return 1;
	}

	// diagonal check two

	{
		char a, b, c, d;
		a = field[3];
		b = field[6];
		c = field[9];
		d = field[12];

		char row_arr[4] = {a, b, c, d};
		eval_row(row_arr);

		if (flag_win == 1) return 1;
	}

	// no wins possible, only draw or not finished

	if (flag_win == 0)
	{

		for (int i = 0; i < 16; i++)
		{
			if (field[i] == '.')
			{
				flag_rest = 2; // not finished
				return 1;
			}
		}
		flag_rest = 1;
	}
			
					

	return 1;
}
			

int main()
{
	vector<string> lines;
	ifstream input("input.txt");
	if (input.is_open())
	{
		while (input.good())
		{
			string line;
			getline(input, line);
			lines.push_back(line);
			//cout << line << endl;
		}
		input.close();
	} else {
		cout << "Couldn't open file" << endl;
	}

	int case_num = atoi(lines[0].c_str());
	
	for (int i = 1; i <= case_num; i++)
	{
		flag_win = 0;
		flag_rest = 0;
		eval_state(lines, (5*i)-4);
		//cout << flag_win << endl;
		cout << "Case #" << i << ": ";
		if (flag_win == 1)
		{
			cout << winner << " won" << endl;
		} else {
			if (flag_rest == 1)
			{
				cout << "Draw" << endl;
			} else {
				cout << "Game has not completed" << endl;
			}
		}
		
	}

	return 0;
}


