#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main()
{
	string s;
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("output.txt");
	getline(infile, s);
	int n = stoi(s, 0);

	if (infile.is_open())
	{
		
		for (int i = 0; i < n; i++) //case loop
		{
			bool arr[10];
			for (int i = 0; i < 10; i++)
			{
				arr[i] = false;
			}

			outfile << "Case #" << i + 1 << ":  ";
			getline(infile, s);
			int x = stoi(s, 0);
			bool slept = false;
			if (x == 0)
			{
				outfile << "INSOMNIA" <<endl;
				slept = true;
			}
			int finalnum = 0;
			int j = 1;

			while (!slept)
			{
				int y = j * x;
				finalnum = y;


				//system("pause");
				if (arr[y % 10] == false)
					arr[y % 10] = true;
				while (y /= 10)
				{
					if (arr[y % 10] == false)
						arr[y % 10] = true;
				}

				if (arr[0] == true && arr[1] == true && arr[2] == true && arr[3] == true && arr[4] == true && arr[5] == true && arr[6] == true && arr[7] == true && arr[8] == true && arr[9] == true)
					slept = true;
				j++;
			}
			if (x != 0)
			{
				outfile << finalnum << endl;
			}
		}
		
		infile.close();
	}
	//system("pause")
}