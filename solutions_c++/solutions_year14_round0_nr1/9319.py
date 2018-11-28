#include <iostream>
#include <string>
#include <string.h>
#include <fstream>

using namespace std;

int main()
{
	int first_time[4][4];
	int second_time[4][4] ;
	ifstream inputfile ("input.txt");
	char s[10];
	inputfile.getline(s,10);
	int test_cases = atoi (s);
	int first_choice = 0;
	int second_choice = 0;
	string output = "";
	int chosen_number = 0;


	for(int k=0;k<test_cases;k++)
	{
		output += "Case #" + to_string(k+1) + ": ";
		char s[10];
		int counter = 0;
		inputfile.getline(s,10);
		first_choice = atoi (s);
		for(int i=0;i<4;i++)
		{
			char input_line[20];  
			inputfile.getline(input_line,20);
			string number = "";
			int index = 0;
			for(int j=0;j<input_line[j]!=0;j++)
			{
				if(input_line[j] != ' ')
				{
					number += input_line[j];
				}
				else
				{
					first_time[i][index++] = atoi(number.c_str());
					number = "";
				}
			}
			first_time[i][index] = atoi(number.c_str());
		}

		inputfile.getline(s,10);
		second_choice = atoi (s);
		for(int i=0;i<4;i++)
		{
			char input_line[20];  
			inputfile.getline(input_line,20);
			string number = "";
			int index = 0;
			for(int j=0;j<input_line[j]!=0;j++)
			{
				if(input_line[j] != ' ')
				{
					number += input_line[j];
				}
				else
				{
					second_time[i][index++] = atoi(number.c_str());
					number = "";
				}
			}
			second_time[i][index] = atoi(number.c_str());
		}

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(first_time[first_choice-1][i] == second_time[second_choice-1][j])
				{
					counter ++;
					chosen_number = first_time[first_choice-1][i];
				}
			}
		}

		if(counter == 0)
		{
			output += "Volunteer cheated!\n";
		}

		else if(counter == 1)
		{
			output += to_string(chosen_number)+"\n";
		}
		else
		{
			output += "Bad magician!\n";
		}

	}


		ofstream out_file("out.txt");
		out_file << output;
	
	system("pause");
	return 0;
}