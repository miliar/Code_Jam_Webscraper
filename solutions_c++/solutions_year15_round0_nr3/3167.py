#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string multiply(string a, string b)
{
	if (a == "1")
		return b;
	if (a == "-1")
		return "-"+b;
	if (a == b)
		return "-1";
	if ((a == "-" + b) || ("-" + a == b))
		return "1";

	if ((a == "i") && (b == "j"))
		return "k";
	if ((a == "i") && (b == "k"))
		return "-j";
	if ((a == "-i") && (b == "j"))
		return "-k";
	if ((a == "-i") && (b == "k"))
		return "j";

	if ((a == "j") && (b == "i"))
		return "-k";
	if ((a == "j") && (b == "k"))
		return "i";
	if ((a == "-j") && (b == "i"))
		return "k";
	if ((a == "-j") && (b == "k"))
		return "-i";

	if ((a == "k") && (b == "i"))
		return "j";
	if ((a == "k") && (b == "j"))
		return "-i";
	if ((a == "-k") && (b == "i"))
		return "-j";
	if ((a == "-k") && (b == "j"))
		return "i";

	cout << "Multiplication error";
	system("pause");
}
void main()
{
	ifstream input;
	input.open("C-small-attempt0.in");

	if (!input.is_open())
	{
		cout << "Error opening file\n";
		system("pause");
	}

	int tot_cases;
	input >> tot_cases;

	ofstream output;
	output.open("solution.out");

	for (int i = 0; i < tot_cases; i++)
	{
		output << "Case #" << i + 1 << ": ";

		int L = 0;
		int X = 0;

		input >> L;
		input >> X;
		string data;
		input >> data;

		string i_trap = "1", j_trap = "1", k_trap = "1";
		int i_flag = 0, j_flag = 0;

		for (int i = 0; i < X; i++)
		{
			for (int j = 0; j < L; j++)
			{
				if (i_flag == 0)
				{
					string val;
					val.push_back(data[j]);
					i_trap = multiply(i_trap, val);
					if (i_trap == "i")
						i_flag = 1;
					continue;
				}

				if (j_flag == 0)
				{
					string val;
					val.push_back(data[j]);
					j_trap = multiply(j_trap, val);
					if (j_trap == "j")
						j_flag = 1;
					continue;
				}

				string val;
				val.push_back(data[j]);
				k_trap = multiply(k_trap, val);
			}
		}

		if (k_trap == "k")
			output << "YES" << '\n';
		else
			output << "NO" << '\n';
	}

	output.close();
	input.close();
}