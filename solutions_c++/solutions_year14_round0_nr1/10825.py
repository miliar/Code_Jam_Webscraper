#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int arr[4], count = 0, choice = 0, same = 0, temp = 0, required, del;
	
	ifstream fin;
	ofstream fout;
	fout.open("output.in");
	fin.open("A-small-attempt2.in");
	
	if (fin)
	{
		fin >> count;
		for (int i = 0; i < count; i++)
		{
			fin >> choice;
			int x = 0;
			for (int j = 0; j < 16; j++)
			{
				if (j>=(choice -1)*4 && j < choice*4)
				{
					fin >> arr[x++];
				}
				else
				{
					fin >> del;
				}
			}

			fin >> choice;
			for (int j = 0; j < 16; j++)
			{
				if (j >= (choice - 1) * 4 && j < choice * 4)
				{
					fin >> temp;
					for (int i = 0; i < 4; i++)
					{
						if (temp == arr[i])
						{
							same++;
							required = arr[i];
						}
					}
				}
				else
				{
					fin >> del;
				}
			}

			if (same == 1)
			{
				fout << "Case #" << i + 1 << ": " << required << endl;
			}
			else if (same > 1)
			{
				fout << "Case #" << i + 1 << ':' << " Bad Magician!" << endl;
			}
			else if (same == 0)
			{
				fout << "Case #" << i + 1 << ':' << " Volunteer cheated!" << endl;
			}

			same = required = x = choice = 0;
		}
	}

	fin.close();
	fout.close();
	return 0;

}