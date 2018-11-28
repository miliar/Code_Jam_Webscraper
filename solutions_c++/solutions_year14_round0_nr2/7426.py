#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <iomanip>

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

bool is_profitable(const double& cookies, const double& gain, const double& C, const double& F, const double& X)
{
	// Calculate seconds to reach goal
	double seconds = (X - cookies) / gain;

	// Calculate seconds to reach farm
	double seconds_farm = (C - cookies) / gain;

	// Calculate seconds to reach goal after buying farm
	seconds_farm += X / (gain + F);

	// Return true if farm is profitable
	return (seconds_farm < seconds);
}

void buy_farm(double& cookies, double& gain, const double& C, const double& F)
{
	if (cookies >= C)
	{
		cookies -= C;
		gain += F;
	}
}

void process(std::string& content)
{
	// Split input on newline character
	std::vector<std::string> lines = split(content, '\n');

	std::stringstream output;

	int count = atoi(lines[0].c_str());

	// Loop through each test case
	for (int i = 0; i < count; ++i)
	{
		output << "Case #" << i + 1 << ": ";

		std::vector<std::string> input = split(lines[i + 1], ' ');
		double C = atof(input[0].c_str());
		double F = atof(input[1].c_str());
		double X = atof(input[2].c_str());

		double seconds = 0.0;
		double cookies = 0.0;
		double gain = 2.0;

		// Do we want to save for a farm?
		bool save_farm = is_profitable(cookies, gain, C, F, X);

		while (cookies < X)
		{
			if (save_farm)
			{
				// Calculate seconds to farm
				double elapsed = (C - cookies) / gain;
				seconds += elapsed;
				cookies += elapsed * gain;
				buy_farm(cookies, gain, C, F);
				save_farm = is_profitable(cookies, gain, C, F, X);
			}
			else
			{
				// Calculate seconds to goal
				double elapsed = (X - cookies) / gain;
				seconds += elapsed;
				break;
			}
		}

		output << std::fixed << std::setprecision(7) << seconds << "\n";
	}

	std::cout << output.str();

	content = output.str();
	content.resize(content.size() - 1);
}

int main()
{
	std::string content;
	if (!read_file("B-large.in", content))
		return EXIT_FAILURE;

	process(content);

	if (!write_file("B-large.out", content))
		return EXIT_FAILURE;

	return EXIT_SUCCESS;
}