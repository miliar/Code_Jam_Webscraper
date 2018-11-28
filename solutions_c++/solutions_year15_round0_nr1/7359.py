#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::string input;
std::vector<std::string> input_lines;
std::string output = "";

const char* io_sizes[] = { "sample", "small", "large" };
std::string io_name = io_sizes[2]; //change this index for different size

void read_input_file() {
	std::ifstream input_file;
	input_file.open("input-" + io_name + ".txt", std::ios::in);

	input_file.ignore(std::numeric_limits<std::streamsize>::max());
	std::streamsize size = input_file.gcount();
	input_file.seekg(0, std::ifstream::beg);
	char* input_buffer = new char[size];

	input_file.seekg(0, std::ifstream::beg);
	input_file.read(input_buffer, size);
	input_file.close();

	input_buffer[size] = '\0';
	input = input_buffer;
}

void split_input() {
	size_t pos = 0;
	const std::string delimiter = "\n";
	std::string token;
	while ((pos = input.find(delimiter)) != std::string::npos) {
		token = input.substr(0, pos);
		if (token != "") { input_lines.push_back(token); }
		input.erase(0, pos + delimiter.length());
	}
	input_lines.push_back(input);

	std::cout << input.c_str();
}

void write_output_file() {
	std::ofstream output_file;
	output_file.open("output-" + io_name + ".txt", std::ios::out);
	output_file.write(output.c_str(), output.length());
	output_file.close();
}

int main(int argc, char* argv[]) {
	read_input_file();
	split_input();

	int num_cases = std::atoi(input_lines[0].c_str());
	for (int c = 0; c < num_cases; ++c) {
		std::string line = input_lines[c + 1];
		//get any number between 0 and space
		int space_index = line.find(" ");
		int max_shy = std::atoi(line.substr(0, space_index).c_str());
		line.erase(0, space_index + 1);

		int standing = 0;
		int invited = 0;
		for (int i = 0; i < line.length(); ++i) { //i is shyness level
			int members = line[i] - 48; //get digit
			if (members != 0) {
				if (standing + invited < i) {
					invited += i - (standing + invited);
				}
				standing += members;
			}
		}
		output += "Case #";
		output += std::to_string(c + 1);
		output += ": ";
		output += std::to_string(invited);
		output += "\n";
	}

	write_output_file();

	return 0;
}
