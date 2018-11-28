#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool checkarray(bool arr[10])
{
	bool checker = true;
	for(int i = 0; i < 10; i++)
	{
		checker = checker && arr[i];
		if(!checker)
		{
			return false;
		}
	}
	return checker;

}

int main()
{
	ifstream read;
	read.open("A-large.in");

	ofstream write;
	write.open("output.txt");
	
	int T;
	read >> T;

	for (int i = 0; i < T; i++)
	{
		write<<"Case #"<<i+1 <<": "; 
		
		bool numbers[10] = {false};
		bool isZero = false;
		bool done = false;
		string num;
		read >> num;
		long long int value = atoi(num.c_str());
		long long int temp = 0;

		while(!isZero && !done)
		{
			temp = temp + value;
			string numup = to_string(temp);

			for(int j = 0; j < numup.size(); j++)
			{
				int x = numup[j] - '0';
				numbers[x] = true;

			}
			if(value == 0 )
			{
				write << "INSOMNIA" << endl;
				isZero = true;
				continue;
			}
			if(checkarray(numbers))
			{
				write << atoi(numup.c_str()) << endl;
				done = true;
				continue;
			}
		}
	}
	
	return 0;
}