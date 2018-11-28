#include <iostream>
#include <fstream>
using std::endl;

int main()
{
	std::ifstream cin;
	std::ofstream cout;

	cin.open("A-large.in");
	cout.open("A-large.out");
	
	size_t N;
	cin >> N;
	for(size_t i = 0; i < N; i++)
	{
		size_t sMax;
		cin >> sMax;

		size_t accCount = 0;
		size_t friendCount = 0;
		
		for(size_t j = 0; j < sMax + 1; j++)
		{
			char cShyCount;
			cin >> cShyCount;

			int difference = j - accCount;
			if(difference > 0)
			{
				friendCount += difference;
				accCount += difference;
			}

			accCount += cShyCount - '0';
		}

		cout << "Case #" << i + 1 << ": " << friendCount << endl;
	}
}
