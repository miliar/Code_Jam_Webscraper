#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream myfile;
	myfile.open("input.txt");
	
	ofstream ofile;
	ofile.open("output.txt");

	int total_cases = 0;

	myfile >> total_cases;

	int c = 1;
	while (c<=total_cases)
	{
		string data;
		int stood = 0;
		int ans = 0;
		int max_level = 0;
		
		myfile >> max_level;
		myfile >> data;

		for (int i = 0; i <= max_level;i++)
		{
			int temp = data.at(i) - '0';
		
			if (temp > 0)
			{

				if (stood < i)
				{
					ans += i - stood;
					stood += ans;
				}
				stood += temp;
			}
			
		}

		ofile << "Case #" << c++ << ": " << ans << endl;
	}


	return 0;
}