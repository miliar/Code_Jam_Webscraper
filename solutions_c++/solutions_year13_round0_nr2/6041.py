#include <fstream>
#include <string>
#include <iostream>
#include <list>

std::string Solve (int **rows, int n, int m)
{
	int *rowsums = new int [n];
	int *colsums = new int [m];
	
	for (int i = 0; i < n; ++i)
	{
		rowsums[i] = 0;
	}

	for (int j = 0; j < m; ++j)
	{
		colsums[j] = 0;
	}

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			rowsums[i] += rows[i][j];
			colsums[j] += rows[i][j];
		}
	}

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if (rows[i][j] == 1 && rowsums[i] != m && colsums[j] != n)
			{
				delete[] rowsums;
				delete[] colsums;
				return "NO";
			}
		}
	}
	
	delete[] rowsums;
	delete[] colsums;
	return "YES";
}

void main ()
{	
	std::ifstream input ("Input.txt");
	std::string line("");
	getline (input, line);
	int tests_num = atoi(line.c_str());
	
	int n, m;
	int **rows;

	std::ofstream output ("Output.txt");

	for (int test = 0; test < tests_num - 1; ++test)
	{
		getline (input, line);
		n = atoi(line.substr(0, line.find_first_of(' ')).c_str());
		m = atoi(line.substr(line.find_first_of(' ') + 1).c_str());
		rows = new int* [n];
		for (int i = 0; i < n; ++i)
		{
			getline (input, line);
			rows[i] = new int [m];

			int space, start = 0, jm = -1;
			while ((space = line.find_first_of(' ', start)) != std::string::npos)
			{
				rows[i][++jm] = atoi(line.substr(start, space - start).c_str());
				start = space + 1;
			}
			rows[i][m - 1] = atoi(line.substr(line.find_last_of(' ') + 1).c_str());
			
		}
		output << "Case #" << test + 1 << ": " << Solve(rows, n, m) << std::endl;

		for (int i = 0; i < n; ++i)
		{
			delete[] rows[i];
		}
		delete[] rows;
	}

	getline (input, line);
	n = atoi(line.substr(0, line.find_first_of(' ')).c_str());
	m = atoi(line.substr(line.find_first_of(' ') + 1).c_str());
	rows = new int* [n];
	for (int i = 0; i < n; ++i)
	{
		getline (input, line);
		rows[i] = new int [m];

		int space, start = 0, jm = -1;
		while ((space = line.find_first_of(' ', start)) != std::string::npos)
		{
			rows[i][++jm] = atoi(line.substr(start, space - start).c_str());
			start = space + 1;
		}
		rows[i][m - 1] = atoi(line.substr(line.find_last_of(' ') + 1).c_str());
			
	}
	output << "Case #" << tests_num << ": " << Solve(rows, n, m);

	for (int i = 0; i < n; ++i)
	{
		delete[] rows[i];
	}
	delete[] rows;
	
	output.close();
	input.close();
}