#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");


	int T = 0;
	in >> T;
	for (int n = 1; n <= T; n++)
	{
		bool findone = false;
		int findtotal = 0, result = -1;
		bool status[20];
		for (int j = 0; j < 20; j++)
		{
			status[j] = false;
		}
		int ans1=0, ans2=0;
		in >> ans1;
		int a[5];
		for (int i = 1; i <= 4; i++)
		{
			in >> a[1] >> a[2] >> a[3] >> a[4];
			if (ans1 == i)
			{
				for (int k = 1; k <= 4; k++)
				{
					findtotal++;
					status[a[k]] = true;
				}
			}
		}

		in >> ans2;

		for (int i = 1; i <= 4; i++)
		{
			in >> a[1] >> a[2] >> a[3] >> a[4];
			if (ans2 == i)
			{
				for (int k = 1; k <= 4; k++)
				{
					if (status[a[k]] == false)
					{
						findtotal++;
						status[a[k]] = true;
					}
					else
					{
						result = a[k];
					}
				}
			}
		}
		if (findtotal == 8)
		{
			out << "Case #" << n << ": " << "Volunteer cheated!" << endl;
		}
		else if (findtotal == 7)
		{
			out << "Case #" << n << ": " << result << endl;
		}
		else
		{
			out << "Case #" << n << ": " << "Bad magician!" << endl;
		}
	}


	in.close();
	out.close();

	return 0;
}