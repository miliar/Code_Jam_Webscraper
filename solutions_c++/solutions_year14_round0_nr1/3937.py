#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	
	int T;
	input >> T;
//	cout << "T = "<<T << endl;

	unsigned n;
	string s;
	unsigned a[4];
	unsigned temp, numb, ans;

	for (unsigned t=0; t<T; ++t)
	{
		numb = 0;
		input >> n;
		for (int i=1; i<n; ++i)
		{
			for (int i = 0; i < 4; i++)
				input >> temp;
		}
		for (int i=0; i<4; ++i)
		{
			input >> a[i];
		}
		for (int i = n; i<4; ++i)
		{
			for (int i = 0; i < 4; i++)
				input >> temp;
		}

		input >> n;
		for (int i = 1; i<n; ++i)
		{
			for (int i = 0; i < 4; i++)
				input >> temp;
		}
		for (int i = 0; i<4; ++i)
		{
			input >> temp;
			for (int j = 0; j < 4; ++j)
			{
				if (temp == a[j])
				{
					++numb;
					ans = a[j];
				}
			}
		}
		for (int i = n; i<4; ++i)
		{
			for (int i = 0; i < 4; i++)
				input >> temp;
		}

		output << "Case #" << t + 1 << ": ";
		switch (numb)
		{
		case 1:
			output << ans;
			break;
		case 0:
			output << "Volunteer cheated!";
			break;
		default:
			output << "Bad magician!";
			break;
		}
		output << "\n";

	}




	input.close();
	output.close();
	//	system("pause");
	return 0;
}
