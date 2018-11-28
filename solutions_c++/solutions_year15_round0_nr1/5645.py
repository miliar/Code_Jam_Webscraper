#include <iostream>
using namespace std;

unsigned int studyCase();

int main(int argc, char* argv[])
{
	unsigned int numberOfCases = 0;
	unsigned int res = 0;
	cin >> numberOfCases;
	for (int i = 0; i < numberOfCases; ++i)
	{
		res = studyCase();
		cout << "Case #" << i+1 << ": " << res << endl; 
	}
	return 0;
}

unsigned int studyCase()
{
	// Init
	unsigned int maxShyness = 0;
	char c;
	unsigned int array[maxShyness];
	int sum = 0, numberOfGuests = 0;
	cin >> maxShyness;
	for (int i = 0; i <= maxShyness; ++i)
	{
		cin >> c;
		array[i] = (int)c - '0';
		while (sum < i)
		{
			numberOfGuests++;
			sum++;
		}
		sum += array[i];
	}
	return numberOfGuests;
}

