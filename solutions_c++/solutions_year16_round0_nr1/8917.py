#include <fstream>
#include <vector>
#include <iostream>
#include <string>
#include <math.h>
using namespace std;
int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("output.txt");
	int T;
	int temp, temp2;
	bool digit[10] = { 0,0,0,0,0,0,0,0,0,0 };
	vector<int> vec;
	infile >> T;
	for (int i = 0; i < T; i++)
	{
		infile >> temp;
		vec.push_back(temp);
	}
	for (int i = 0; i < T; i++)
	{
		if (vec[i] == 0)
		{
			outfile << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		temp = 1;
		while (!digit[0] || !digit[1] || !digit[2] || !digit[3] || !digit[4] || !digit[5]
			|| !digit[6] || !digit[7] || !digit[8] || !digit[9])
		{
			temp2 = temp * vec[i];
			for (int g = 0;  pow(10,g) <= temp * vec[i]; g++)
			{
				digit[temp2 % 10] = true;
				temp2 = temp2 - (temp2 % 10);
				temp2 = temp2 / 10;
			}
			temp++;
		}
		outfile << "Case #" << i + 1 << ": " << (temp - 1)* vec[i] << std::endl;
		for (int b = 0; b < 10; b++)
			digit[b] = false;
	}
}