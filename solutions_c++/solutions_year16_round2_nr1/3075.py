#include<iostream>
#include<cstring>
using namespace std;

int mat[10] = { 0 };
int character[30] = { 0 };
char str[2010];

void proccess() {

	for (int i = 0; i < 10; i++)
		mat[i] = 0;

	for (int i = 0; i < 30; i++)
		character[i] = 0;

	int len = strlen(str);

	for (int i = 0; i < len; i++)
	{
		character[str[i] - 'A']++;
	}
	

	if (character['Z' - 'A'] > 0)
	{
		mat[0] = character['Z' - 'A'];
		character['E' - 'A'] -= character['Z' - 'A'];
		character['R' - 'A'] -= character['Z' - 'A'];
		character['O' - 'A'] -= character['Z' - 'A'];
		character['Z' - 'A'] = 0;
	}

	if (character['W' - 'A'] > 0)
	{
		mat[2] = character['W' - 'A'];
		character['T' - 'A'] -= character['W' - 'A'];
		character['O' - 'A'] -= character['W' - 'A'];
		character['W' - 'A'] = 0;
	}


	if (character['U' - 'A'] > 0)
	{
		mat[4] = character['U' - 'A'];
		character['F' - 'A'] -= character['U' - 'A'];
		character['O' - 'A'] -= character['U' - 'A'];
		character['R' - 'A'] -= character['U' - 'A'];
		character['U' - 'A'] = 0;
	}
	
	if (character['X' - 'A'] > 0)
	{
		mat[6] = character['X' - 'A'];
		character['S' - 'A'] -= character['X' - 'A'];
		character['I' - 'A'] -= character['X' - 'A'];
		character['X' - 'A'] = 0;
	}


	if (character['G' - 'A'] > 0)
	{
		mat[8] = character['G' - 'A'];
		character['E' - 'A'] -= character['G' - 'A'];
		character['I' - 'A'] -= character['G' - 'A'];
		character['H' - 'A'] -= character['G' - 'A'];
		character['T' - 'A'] -= character['G' - 'A'];
		character['G' - 'A'] = 0;
	}

	if (character['H' - 'A'] > 0)
	{
		mat[3] = character['H' - 'A'];
		character['T' - 'A'] -= character['H' - 'A'];
		character['R' - 'A'] -= character['H' - 'A'];
		character['E' - 'A'] -= character['H' - 'A'];
		character['E' - 'A'] -= character['H' - 'A'];
		character['H' - 'A'] = 0;
	}

	if (character['F' - 'A'] > 0)
	{
		mat[5] = character['F' - 'A'];
		character['E' - 'A'] -= character['F' - 'A'];
		character['V' - 'A'] -= character['F' - 'A'];
		character['I' - 'A'] -= character['F' - 'A'];
		character['F' - 'A'] = 0;
	}


	if (character['S' - 'A'] > 0)
	{
		mat[7] = character['S' - 'A'];
		character['N' - 'A'] -= character['S' - 'A'];
		character['E' - 'A'] -= character['S' - 'A'];
		character['V' - 'A'] -= character['S' - 'A'];
		character['E' - 'A'] -= character['S' - 'A'];
		character['S' - 'A'] = 0;
	}

	if (character['I' - 'A'] > 0)
	{
		mat[9] = character['I' - 'A'];
		character['E' - 'A'] -= character['I' - 'A'];
		character['N' - 'A'] -= character['I' - 'A'];
		character['N' - 'A'] -= character['I' - 'A'];
		character['I' - 'A'] = 0;
	}

	if (character['O' - 'A'] > 0)
	{
		mat[1] = character['O' - 'A'];
		character['N' - 'A'] -= character['O' - 'A'];
		character['E' - 'A'] -= character['O' - 'A'];
		character['O' - 'A'] = 0;
	}


}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		cin >> str;
		proccess();
		cout << "Case #" << i<<": ";
		for (int j = 0; j < 30; j++)
		{
			if (mat[j] != 0)
			{
				for (int k = 0; k < mat[j]; k++)
				{
					cout << j;
				}
			}
		}
		cout << endl;

	}
}