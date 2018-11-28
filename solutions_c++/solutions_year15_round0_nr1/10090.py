#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>

using namespace std;

int main(void)
{
	ifstream inf; inf.open("A-small-attempt2.in");
	ofstream outf; outf.open("A-small-attempt2.out");

	int arr[1001];
	char readline[1100];

	int count;

	inf >> count;

	inf.getline(readline, 1100);

	for (int i = 0; i < count; i++)
	{
		memset(arr, 0, sizeof(int)* 1001);

		int size, stand = 0, need = 0;

		inf.getline(readline, 1100);

		size = atoi(readline) + 1;

		for (int j = 0; j < size; j++)
		{
			if ((stand < j) && ((readline[j + 2] - 48) != 0))
			{
				need += j - stand;
				stand += need;
			}
			stand += readline[j + 2] - 48;
		}

		outf << "Case #" << i + 1 << ": " << need << endl;
	}

	return 0;
}