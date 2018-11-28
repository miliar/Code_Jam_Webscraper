/*
 * =====================================================================================
 *
 *       Filename:  standing_ovation.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/11/2015 10:21:43 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Nikhil Sharma (ns), nsharma9@ncsu.edu
 *   Organization:  NCSU
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

class standing_ovation
{
	int my_id;
	int audiance;
	int total_friends;
	static int count;
	std::string data;
	int max_shyness;
	int char_to_int (char c)
	{
		return (int)(c - '0');
	}
	public:
	standing_ovation():audiance(0),total_friends(0){ my_id = count++; }
	~standing_ovation(){}
	void standing_ovation_init(std::string _data)
	{
		std::istringstream (_data.substr(0,_data.find(" "))) >> max_shyness;
		data = _data.erase(0, _data.find(" ") + 1);
		for(int i=0; i <= max_shyness; i++)
		{
			int friends_previous_level=0;
			int audiance_this_level = char_to_int(data[i]);
			if(audiance < i)
			{
				friends_previous_level = i - audiance;
				total_friends += friends_previous_level;
			}
			audiance += audiance_this_level + friends_previous_level;
		}
		std::cout << "case #"<< my_id <<": " << total_friends << std::endl;
	}
};

int standing_ovation::count = 1;

int main(int argc, char *argv[])
{
	int tests;
	std::ifstream file_stream("A-large.in");
	std::string line_content;
	std::getline(file_stream, line_content);
	std::istringstream (line_content) >> tests;
	standing_ovation* standing_ovation_arr = new standing_ovation[tests];
	for(int i=0; i < tests; i++)
	{
		if(!std::getline(file_stream, line_content))
		{
			std::cerr << "check looping. we ran out of entries" << std::endl;
		}
		standing_ovation_arr[i].standing_ovation_init(line_content);
	}
	file_stream.close();
	delete[] standing_ovation_arr;
	return 0;
}
