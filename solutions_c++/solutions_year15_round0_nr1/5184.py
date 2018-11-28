#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	int max_input;
	cin >> max_input;
	for (int i = 0; i < max_input; i++)
	{
		int max_Shy;
		cin >> max_Shy;
		string input;
		cin >> input;
		if (max_Shy == 0)
		{
			cout << "Case #" << (i + 1) << ": " << 0 << endl; continue;
		}
		int invited = 0;
		int counter = 0;
		counter = input[0] - '0';
		for (int j = 1; j < input.length(); j++)
		{

			if ((counter+invited) < j)
			{
				invited += (j - (counter + invited));
			}
			counter += (input[j] - '0');
		}
		cout << "Case #" << (i + 1) << ": " << invited << endl;
	}
	return 0;
}