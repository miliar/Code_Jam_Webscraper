#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

// Helper function used to read in a file
bool read_file(const std::string& filename, std::string& content)
{
	// Create filestream
	std::ifstream file(filename, std::ios_base::in);
	// Check that file exists.  If not, return false
	if (file.bad())
		return false;

	// File is good.  Read contents
	std::stringstream buffer;
	buffer << file.rdbuf();

	// Get contents from the file
	content = buffer.str();

	// Close file and return true
	file.close();
	return true;
}

// Helper function used to write to a file
bool write_file(const std::string& filename, const std::string& content)
{
	// Create filestream
	std::ofstream file(filename, std::ios_base::out);
	if (file.bad())
		return false;

	// File is good.  Write contents
	file << content;

	// Close file and return true
	file.close();
	return true;
}

// Helper function used to split a string on a given delimeter
std::vector<std::string> split(const std::string& input, char delim)
{
	std::stringstream ss(input);
	std::string item;
	std::vector<std::string> output;
	while (std::getline(ss, item, delim))
		output.push_back(item);

	return output;
}

void process(std::string& content)
{
	// Split input on newline character
	std::vector<std::string> lines = split(content, '\n');

	std::stringstream output;

	int count = atoi(lines[0].c_str());

	// Loop through each block
	for (int i = 0; i < count; ++i)
	{
		std::cout << i << std::endl;
		output << "Case #" << i + 1 << ": ";

		int new_block = (i * 10) + 1;
		// Loop through each line in block
		int row_num = 1;
		std::map<std::string, int> possible_nums;
		for (int j = new_block; j < new_block + 10; j += row_num)
		{
			if ((j + 4) % 5 == 0)
			{
				row_num = lines[j][0] - '0';
				continue;
			}
			std::vector<std::string> temp = split(lines[j], ' ');
			for (auto& s : temp)
			{
				++possible_nums[s];
			}
			row_num = 5 - row_num;
		}

		// Check for duplicates
		auto sanity_check = 0;
		std::string result;
		for (auto iter = possible_nums.begin(); iter != possible_nums.end(); ++iter)
		{
			if (iter->second > 1)
			{
				++sanity_check;
				result = iter->first;
			}
		}

		if (sanity_check > 1)
			result = "Bad magician!";
		else if (sanity_check == 0)
			result = "Volunteer cheated!";

		output << result << "\n";
	}

	content = output.str();
	content.resize(content.size() - 1); // Remove last newline character
}

int main()
{
	std::string content;
	if (!read_file("A-small-attempt1.in", content))
		return EXIT_FAILURE;

	process(content);

	if (!write_file("A-small-attempt1.out", content))
		return EXIT_FAILURE;

	return EXIT_SUCCESS;
}