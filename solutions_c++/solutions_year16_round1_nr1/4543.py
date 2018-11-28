#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


void loadFile(vector<string> & in)
{
	int total = 0;
	string line, parsing = "";
	ifstream myfile("small_input.txt");
	int i = 0;
	size_t ss;


	if (myfile.is_open())
	{
		while (!myfile.eof())
		{
			getline(myfile, line);

			if (line == "")
				continue;
			if (i != 0)
			{
				in.push_back(line);
			}
			i++;
		}
		myfile.close();
	}
}

void saveFile(vector<string> & out)
{
	ofstream myfile("small_output.txt");

	if (myfile.is_open())
	{
		
		for (int i = 0; i < out.size(); i++)
		{
			myfile << "Case #" << i+1 << ": "<<out[i];
	
			if (i == out.size() - 1)
			{
				break;
			}
			myfile << endl;
		}
		myfile.close();
	}

}





vector<string> getAll(string input)
{
	vector<string> out;
	vector<string> actual;

	string temp1 = "";
	string temp2 = "";
	string temp3 = "";
	string temp4 = "";

	char tempchar ;

	temp3.push_back(input[0]);
	out.push_back(temp3);

	for (int i = 1; i < input.size(); i++)
	{
		tempchar = input[i];

		while (out.size() != 0)
		{
			temp1.clear();
			temp2.clear();

			temp4 = out[out.size()-1];
			out.pop_back();

			//at start
			temp1.push_back(tempchar);
			temp1.append(temp4);

			//at end
			temp2.append(temp4);
			temp2.push_back(tempchar);

			actual.push_back(temp1);
			actual.push_back(temp2);
		}
		
		out = actual;
		actual.clear();
	}

	return out;
}

string getLastword(vector<string> ins)
{
	string output = "";
	string max = ins[0];

	for (int i = 1; i < ins.size(); i++)
	{
		if (ins[i]>max)
		{
			max = ins[i];
		}
	}

	return max;
}


int main()
{
	vector<string> inputs;
	vector<string>allOuts;
	loadFile(inputs);



	for (int i = 0; i < inputs.size(); i++)
	{
		 vector<string> tempOut=getAll(inputs[i]);
		 allOuts.push_back(getLastword(tempOut));
	}
	
	saveFile(allOuts);

	return 0;
}