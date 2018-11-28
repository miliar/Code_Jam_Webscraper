#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<sstream>
using namespace std;

int main()
{
	ifstream infile;
	infile.open("A-large.in", ios::in);
	int n;
	infile >> n;
	int max_shyness = 0;
	vector<string> output;
	for (int i = 0; i < n; i++)
	{
		infile >> max_shyness;
		string shynesses;
		infile >> shynesses;
		long long persons = 0;
		long long invite_persons = 0;

		for (int j = 0; j <= max_shyness; j++)
		{
			long long cur_person = shynesses[j] - '0';
			if (cur_person == 0)
				continue;
			long long shyness = j;
			if (shyness > persons)
			{
				invite_persons += j - persons;
				persons = j;
			}
			persons += cur_person;
		}

		string cur_output = "Case #";
		stringstream ss;
		ss << i+1;
		cur_output += ss.str();
		cur_output += ": ";
		stringstream ss1;
		ss1 << invite_persons;
		cur_output += ss1.str();
		output.push_back(cur_output);

	}

	infile.close();
	ofstream outfile;
	outfile.open("A-large.out", ios::out);
	for (int i = 0; i < n; i++)
	{
		outfile << output[i] << endl;
	}
	outfile.close();
	return -1;
}