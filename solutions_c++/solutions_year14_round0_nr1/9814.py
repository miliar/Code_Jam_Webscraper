#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <limits>

inline int string_to_int(const std::string& str)
{
	std::stringstream convert (str);
	int temp;
	convert >> temp;
	return temp;
}

inline void print_vector(const std::vector<int> vec)
{
	for(int i = 0; i < vec.size(); i ++)
		std::cout << vec[i] << " ";
	std::cout << "\n";
}

void string_to_int_vector(std::string& line, std::vector <int>& row)
{
	int i = line.find(' ');
	int j = 0;

	while (i != std::string::npos)
	{
		row.push_back(string_to_int(line.substr(j, i - j)));
		j = i + 1;
		i = line.find(' ', j);
	}
	row.push_back(string_to_int(line.substr(j, line.length() - j)));
}

void getRow(std::ifstream& myfile, std::vector<int>& row, const int& answer)
{
	std::string line;

	int i = 0;

	for (; i < answer - 1; i ++)
		myfile.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
	getline(myfile, line);
	
	string_to_int_vector(line, row);

	while (i++ < row.size() - 1)
		myfile.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
}

short int getUniqueElement(std::vector<int>& row1, std::vector<int>& row2)
{
	int ret = std::numeric_limits<short int>::min();

	for (int i = 0; i < row1.size(); i ++)
	{
		for (int j = 0; j < row2.size(); j ++)
		{
			if (row1[i] == row2[j])
			{
				if (ret != std::numeric_limits<short int>::min())
					return std::numeric_limits<short int>::min();
				ret = row1[i];
			}
		}
	}
	if (ret == std::numeric_limits<short int>::min())
		return 0;

	return ret;
}

int main(int argc, char* argv[])
{
	std::ifstream myfile(argv[1]);



	std::string line;

	getline(myfile, line);
	int T = string_to_int(line);

	int count  = 1;

	while (myfile.good())
	{
		getline(myfile, line);
		int answer1 = string_to_int(line);
		std::vector<int> row1;
		getRow(myfile, row1, answer1);
	//	print_vector(row1);

		getline(myfile, line);
		int answer2 = string_to_int(line);
		std::vector<int> row2;		
		getRow(myfile, row2, answer2);
	//	print_vector(row2);

		short int ret = getUniqueElement(row1, row2);

		std::cout << "Case #" << count ++;
		if (!ret)
			std::cout << ": Volunteer cheated!\n";
		else if (ret < 0)
			std::cout << ": Bad magician!\n";
		else
			std::cout << ": " <<ret << "\n";
	}
	return 0;
}