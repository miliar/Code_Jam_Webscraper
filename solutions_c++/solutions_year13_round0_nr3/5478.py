#include<iostream>
#include<fstream>
#include<string>
#include<sstream>

using namespace std;

bool IsPalindrome(string number);

int main()
{
	string line = "";
	int index = 1;
	int fscount = 0;
	int numberOfTestCases = 0;
	ofstream outFile;
	ifstream inFile("test.in");
	outFile.open("test.out");

	if(inFile.is_open())
	{
		getline(inFile, line);

		int start = 0, end = 0;
		
		numberOfTestCases = stoi(line);

		for(int i = 0; i < numberOfTestCases; i++)
		{
			bool palindrome = false;

			getline(inFile, line);

			stringstream stream;
			stream << line;

			stream >> start;
			stream >> end;

			for(int k= start; k <= end; k++)
			{
				stream = stringstream();
				stream << k;
				palindrome = IsPalindrome(stream.str());

				if(palindrome)
				{
					int ksqrt = sqrt(k);
					
					if(ksqrt*ksqrt == k) 
					{
						stream = stringstream();
						stream << ksqrt;
						palindrome = IsPalindrome(stream.str());

						if(palindrome)
						{
							fscount++;
						}
					}
				}
			}

			outFile << "Case #" << index << ": " << fscount << endl;

			index++;
			fscount = 0;
		}

		
		outFile.close();
	}

	return 0;
}

bool IsPalindrome(string number)
{
	bool palindrome = true;
	int start = 0;
	int end = number.length()-1;

	do
	{
		if(number[start] != number[end])
		{
			palindrome = false;
		}
		start++;
		end--;
	}
	while(start < end);

	return palindrome;
}