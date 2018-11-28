#include<iostream>
#include<fstream>
#include<string>

int main()
{
	int n, count;
	char curr, extra;
	std::string reader;
	std::ifstream fin;
	std::ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	fin >> n;
	std::getline(fin, reader, '\n');
	for (int i = 0; i < n; i++)
	{
		count = 0;
		std::getline(fin, reader, '\n');
		curr = reader[0];
		for (int i = 0; reader[i] != '\0'; i++)
		{
			if (reader[i] != curr)
			{
				curr = reader[i];
				count++;
			}
		}
		if (curr == '-')count++;
		fout << "Case #" << i+1 << ": " << count << "\n";
	}
}