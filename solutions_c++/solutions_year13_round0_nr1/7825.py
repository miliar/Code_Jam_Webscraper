#include <fstream>
#include <string>
#include <iostream>
#include <map>

std::string Solve (std::string *rows,std::map<char, int>& f)
{
	int sum;
	bool dot_found = false;

	for (int i = 0; i < 4; ++i)
	{
		sum = f[rows[i][0]] + f[rows[i][1]] + f[rows[i][2]] + f[rows[i][3]];
		if (dot_found = sum < 0) continue;
		if (sum < 10) return "X won";
		if (sum % 10 == 0) return "O won";
	}

	for (int i = 0; i < 4; ++i)
	{
		sum = f[rows[0][i]] + f[rows[1][i]] + f[rows[2][i]] + f[rows[3][i]];
		if (sum > 0 && sum < 10) return "X won";
		if (sum > 0 && sum % 10 == 0) return "O won";
	}

	sum = f[rows[0][0]] + f[rows[1][1]] + f[rows[2][2]] + f[rows[3][3]];
	if (sum > 0 && sum < 10) return "X won";
	if (sum > 0 && sum % 10 == 0) return "O won";
	
	sum = f[rows[0][3]] + f[rows[1][2]] + f[rows[2][1]] + f[rows[3][0]];
	if (sum > 0 && sum < 10) return "X won";
	if (sum > 0 && sum % 10 == 0) return "O won";
	
	return dot_found ? "Game has not completed" : "Draw";
}

void main ()
{	
	std::map<char, int> f;
	f.insert (std::pair<char, int> ('X', 1));
	f.insert (std::pair<char, int> ('O', 10));
	f.insert (std::pair<char, int> ('T', 0));
	f.insert (std::pair<char, int> ('.', -101));
	
	std::ifstream input ("Input.txt");
	std::string line("");
	getline (input, line);
	int tests_num = atoi(line.c_str());
	
	std::string rows [4];

	std::ofstream output ("Output.txt");

	for (int i = 0; i < tests_num - 1; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			getline (input, rows[j]);		
		}
		output << "Case #" << i + 1 << ": " << Solve(rows, f) << std::endl;
		getline (input, line);	
	}

	for (int j = 0; j < 4; ++j)
	{
		getline (input, rows[j]);			
	}
	output << "Case #" << tests_num << ": " << Solve(rows, f);

	output.close();
	input.close();
}