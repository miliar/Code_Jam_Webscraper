#include <vector>
#include <string>
#include <iostream>
#include <fstream>

#define INPUT_FILE_NAME "D:/A-large.in"
#define OUTPUT_FILE_NAME "D:/fout.out"

using namespace std;

void parse_input(string input_line, int& max_shyness , vector<int> &people_values)
{
	people_values.clear();
	// parse input line
	string delimiter = " ";
	string values = input_line.substr(input_line.find(delimiter)+1);
	// set the max shyness
	max_shyness = (input_line[0] - '0');
	// set the values
	int value ;
	for (int i=0 ; i<values.size(); i++)
	{
		value = (int)(values[i]-'0');
		people_values.push_back(value);
	}
}

int get_answer(int max_shyness , vector<int> people_values)
{
	int numOfPeople = people_values.size();
	int neededPeople = 0;
	int sum = 0;
	int diff;
	for (int i = 0 ; i<numOfPeople ;i++)
	{
		diff = sum - i; 
		if (diff < 0)
		{
			neededPeople -= diff;
			sum -= diff;
		}
		sum += people_values[i];

	}
	return neededPeople;
}

int main()
{
	// the fstream
	fstream fileInput(INPUT_FILE_NAME,fstream::in);
	fstream fileOutput(OUTPUT_FILE_NAME,fstream::out);

	int t = 0;
	fileInput>>t;
	string temp;
	getline(fileInput,temp);
	

	for (int i=0 ; i<t ; i++)
	{
		getline(fileInput,temp);

		int max_shyness;
		vector<int> people_values;

		parse_input(temp,max_shyness,people_values);

		int answer = get_answer(max_shyness,people_values);

		fileOutput<<"Case #"<<i+1<<": "<<answer<<endl;
	}
	return EXIT_SUCCESS;
}