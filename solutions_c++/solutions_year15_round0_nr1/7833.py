#include<iostream>
#include<fstream>
#include<string>


void num_friends(const std::string& input)
{
	std::ifstream in(input);
	std::ofstream out("D:/standing_ovation_output_large.txt");
	
	int num_testcase = 0;
	in >> num_testcase;
	int S_max = 0;

	for (int i = 1; i <= num_testcase; i++)
	{
		in >> S_max;
		int* arr = new int[S_max + 1];

		char c = in.get();
		
		for (int j = 0; j < S_max + 1; j++)
		{
			if((c = in.get()) != EOF && c != '\n')
			{
				arr[j] = c - '0';
			}

			if (c == '\n')
				break;
		}

		
		int num_people = 0;
		int friends = 0;
		
		for (int j = 0; j < S_max + 1; j++)
		{
			if (j >(num_people + friends))
			{
				friends += j - (num_people + friends);
			}
			
			num_people += arr[j];
		}

		out << "Case #" << i << ": " << friends << "\n";
		delete[] arr;
	}
}

int main()
{
	num_friends("D:/A-large.in");
	return 0;
}