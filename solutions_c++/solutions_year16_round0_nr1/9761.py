#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;


int main()
{
	ifstream in;
	in.open("C:\\Users\\hsitce170-10\\Desktop\\A-small-attempt0.in");
	ofstream out;
	out.open("C:\\Users\\hsitce170-10\\Desktop\\out.txt");

	bool numbers[10];
	

	int str;
	in >> str;
	int numberOfTestCases = str;
	long long number;
	for (long long caseNumber = 1; caseNumber <= numberOfTestCases; caseNumber++)
	{
		for (int i = 0; i < 10; i++)
			numbers[i] = false;
		in >> str;
		number = str;
		if (number != 0){
			for (long long i = 1;; i++)
			{
				
				number = str*i;

				int temp = number;
				while (temp > 0){
					int digit = temp % 10;
					numbers[digit] = true;
					temp /= 10;
				}
				int flag = 1;
				for (int h = 0; h < 10; h++)
				if (numbers[h] == false)
				{
					flag = 0;
					break;
				}
				if (flag == 1)
				{
					out << "Case #" << caseNumber << ": " << i*str << endl;
					break;
				}

			}
		}
		else
		{
			out << "Case #" << caseNumber << ": INSOMNIA" << endl;
		}

	}

	in.close();
	out.close();
	//system("pause");
}