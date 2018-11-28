/*#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
	ofstream out("output2.txt");
	ifstream in("A-small-attempt2.in");
	int T;
	in >> T;
	for (int k = 1; k <= T;k++)
	{
		vector<int> myVec1, myVec2;
		int row1;
		in >> row1;
		row1--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int x;
				in >> x;
				if (i == row1)
				{
					myVec1.push_back(x);
				}
			}
		}

		int row2;
		in >> row2;
		row2--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int x;
				in >> x;
				if (i == row2)
				{
					myVec2.push_back(x);
				}
			}
		}

		// input correct
		int count = 0;
		int number;
		for (int i = 0; i < myVec1.size(); i++)
		{
			for (int j = 0; j < myVec2.size(); j++)
			{
				if (myVec1[i] == myVec2[j])
				{
					count++;
					number = myVec1[i];
				}
			}
		}
		out << "Case #" << k << ": ";
		if (count == 0)
		{
			out << "Volunteer cheated!" << endl;
		}
		else if (count == 1)
		{
			out << number << endl;
		}
		else out << "Bad magician!" << endl;
	}
	out.close();
	in.close();
	return 0;
}*/


/*#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("B-large.in");
	ofstream out("large-output.txt");
	int T;
	in >> T;
	for (int i = 1; i <= T;i++)
	{
		double C, F, X;
		in >> C >> F >> X;
		double sum = 0.0000000;
		double current_rate = 2.0000000;
		while (true)
		{
			double time_farm = C / current_rate;
			double time_done = X / current_rate;
			double next_rate = current_rate + F;
			if (time_done < time_farm + X / next_rate)
			{
				sum += time_done;
				break;
			}
			else
			{
				sum += time_farm;
				current_rate = next_rate;
			}
		}
		out << "Case #" << i << ": ";
		out << fixed << setprecision(7) << sum << endl;
	}
	in.close();
	out.close();
}*/

#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("D-small-attempt0.in");
	ofstream out("outputC0.txt");
	int T;
	in >> T;
	for (int k = 1; k <= T;k++)
	{
		vector<double> Naomi, Ken;
		int number;
		in >> number;
		for (int i = 0; i < number; i++)
		{
			double x;
			in >> x;
			Naomi.push_back(x);
		}
		for (int i = 0; i < number; i++)
		{
			double x;
			in >> x;
			Ken.push_back(x);
		}

		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());

		int count = 0;
		int iK = 0, jK = number - 1;
		for(int iN = 0; iN < number; iN++)
		{
			if (Naomi[iN] < Ken[iK])
			{
				jK--;
			}
			else
			{
				count++;
				iK++;
			}
		}

		int count2 = 0;
		int iN = number-1;
		iK = 0;
		jK = number - 1;
		while (iN > -1)
		{
			if (Naomi[iN] > Ken[jK])
			{
				iN--;
				iK++;
				count2++;
			}
			else
			{
				iN--;
				jK--;
			}
		}
		out << "Case #" << k << ": " << count << ' ' << count2 << endl;
	}
	return 0;
}