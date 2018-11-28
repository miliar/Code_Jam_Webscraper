#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <stdio.h>
#include <string>
#include <set>
using namespace std;

int main()
{
	FILE* handle;
	freopen_s(&handle, "input.txt", "r", stdin);
	freopen_s(&handle, "output.txt", "w", stdout);
	
	int res = 0;
	long long cases = 0, counter = 0;
	cin >> cases;

	while (counter < cases)
	{
		res = 0;
		int max = 0;
		cin >> max;
		int* aud = new int[max];
		string audience = "";
		cin >> audience;

		int clapping = 0;
		for (int i = 0; i <= max; i++)
		{
			if (clapping < i)
			{
				clapping += 1;
				res++;
			}
			clapping += std::stoi(audience.substr(i, 1));

			if (clapping > max)
				break;
		}
				
		cout << "Case #" << counter + 1 << ": " << res;
		cout << endl;
		counter++;
	}
	return 0;
}
