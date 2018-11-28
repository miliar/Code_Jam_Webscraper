#include <fstream>
#include <string>

using namespace std;

int main()
{
	int numberOfCases;
	ifstream in("B-large.in");
	ofstream out("output.txt");
	in >> numberOfCases;
	for (int i = 0; i < numberOfCases; i++)
	{
		string pancakes;
		in >> pancakes;
		int flips = 1;
		char lastPancake;
		lastPancake = pancakes[0];
		for (int j = 1; j < pancakes.length(); j++)
		{
			if (pancakes[j] != lastPancake)
			{
				flips++;
				lastPancake = pancakes[j];
			}
		}
		if (lastPancake == '+')
			flips--;
		out << "Case #" << i + 1 << ": " << flips << endl;
	}
	return 0;
}