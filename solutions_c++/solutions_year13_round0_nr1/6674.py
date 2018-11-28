#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

string tab[4];

bool check_table(vector<char> table, char p)
{
	bool ans = true;
	for(int i=0;i<4;i++)
	{
		if(table[i] != p && table[i] != 'T')
			ans = false;
	}
	
	return ans;
}

vector<char> make_row(int r)
{
	vector<char> row;
	for(int i=0; i<4; i++)
		row.push_back(tab[r][i]);
	return row;
}

vector<char> make_col(int c)
{
	vector<char> col;
	for(int i=0; i<4; i++)
		col.push_back(tab[i][c]);
	return col;
}

vector<char> make_diag(int d)
{
	vector<char> diag;
	if(d == 0)
	{
		diag.push_back(tab[0][0]);
		diag.push_back(tab[1][1]);
		diag.push_back(tab[2][2]);
		diag.push_back(tab[3][3]);
	}
	else
	{
		diag.push_back(tab[0][3]);
		diag.push_back(tab[1][2]);
		diag.push_back(tab[2][1]);
		diag.push_back(tab[3][0]);
	}
	return diag;
}
bool tictac(char p)
{
	bool ans = false;
	for(int i=0; i<4; i++)
	{
		if(ans == false)
			ans = check_table(make_row(i), p);
		if(ans == false)
			ans = check_table(make_col(i), p);

	}
	ans = (ans || check_table(make_diag(0), p) || check_table(make_diag(1), p));
	return ans;
}

bool if_draw()
{
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(tab[i][j] == '.')
				return false;
	return true;
}
void print_tab()
{
	for(int i=0; i<4; i++)
		cout << tab[i]<< endl;
}

int main()
{
	int n;
	string tmp;

	scanf("%d", &n);

	for(int i=0; i<n; i++)
	{
		for(int l=0; l<4; l++)
		{
			cin >> tmp;
			tab[l] = tmp;
		}
		cin >> tmp;
		
		printf("Case #%d: ", i+1);
		if(tictac('X'))
			printf("X won\n");
		else if(tictac('O'))
			printf("O won\n");
		else if(if_draw())
			printf("Draw\n");
		else
			printf("Game has not completed\n");
				
	}

	return 0;
}

