#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cctype>
#include <vector>
//#include <time.h>
using namespace std;

int findmax(const vector<int> & list);
bool is_possible(const vector<vector<int>> & table, const vector<int> & col, const vector<int> & row, int n, int m);

bool is_possible(const vector<vector<int>> & table, const vector<int> & col, const vector<int> & row, int n, int m)
{
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			int x = table[r][c];
			if (x < col[c] && x < row[r]) return false;
		}
	}
	return true;
}

int findmax(const vector<int> & list)
{
	int size = list.size();
	int max = list[0];
	for (int i = 1; i < size ; i++)
		if (list[i] > max) max = list[i];
	return max;
}

int main()
{
	//clock_t init, final;
	//init = clock();
	int tekrar;
	string line;
	ifstream input("f.txt");
	ofstream output("out.txt");
	getline(input,line);
	tekrar = atoi(line.c_str());
	for (int i = 1; i <= tekrar; i++)
	{
		int n,m;
		getline(input,line);
		istringstream temp(line);
		temp >> n >> m;
		vector<vector<int>> table;
		vector<int> row;
		vector<int> col;
		for (int row = 0; row < n; row++)
		{
			vector<int> t;
			getline(input,line);
			istringstream temp2(line);
			for (int col = 0; col < m; col++)
			{
				int o;
				temp2 >> o;
				t.push_back(o);
			}
			table.push_back(t);
		}
		for (int r = 0; r < n; r++)
			row.push_back(findmax(table[r]));
		for (int r = 0; r < m; r++)
		{
			int max = table[0][r];
			for (int c = 1; c < n; c++)
				if (table[c][r] > max) max = table[c][r];
			col.push_back(max);
		}
		bool is_ok = is_possible(table,col,row,n,m);
		output << "Case #" << i << ": ";
		if (is_ok) output << "YES";
		else output << "NO";
		if (i != tekrar) output << endl;
	}
	output.close();
	//final = clock();
	//cout << "The operation takes : " << (double)(final - init) / ((double)CLOCKS_PER_SEC) << " seconds." ;
	system("PAUSE");
	return 0;
}
