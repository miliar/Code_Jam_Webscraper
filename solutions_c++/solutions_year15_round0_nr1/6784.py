#include <iostream>
using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for(int c = 1; c <= T ; c++)
	{
	int max;
	cin >> max;
	int total = 0;
	int req = 0;
	string line;
	cin >> ws;
	cin >> line;
		for(int i = 0; i <= max; i++)
		{

			int j = line[i] - '0';
			if(j == 0)
				continue;
			if(total + req>= i)
				total += j;
			else
			{
				req += i - (total + req);
				total += j;
			}
		}
		cout << "Case #" << c << ": " << req << endl;
	}
}