#include <fstream>

int main()
{
	std::ifstream in("C:\\Users\\Сергей\\Desktop\\in.txt");
	std::ofstream out("C:\\Users\\Сергей\\Desktop\\out.txt");

	int t = 0;

	in >> t;

	for (int i = 0; i < t; i++)
	{
		bool emp = false;
		int a[4][4];

		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				char c;

				in >> c;

				if (c == '.')
					emp = true;

				switch (c)
				{
				case 'X':
					a[j][k] = 1;
					break;
				case 'O':
					a[j][k] = 100;
					break;
				case 'T':
					a[j][k] = -1;
					break;
				default:
					a[j][k] = 0;
					break;
				}
			}

		int res = -1;

		for (int j = 0; j < 4; j++)
		{
			bool b = false;
			int sum = 0;

			for (int k = 0; k < 4; k++)
				if (a[j][k] == -1)
					b = true;
				else
					sum += a[j][k];

			if (b)
				if (sum == 3)
					sum = 4;
				else if (sum == 300)
					sum = 400;

			if (sum == 4)
				res = 0;
			if (sum == 400)
				res = 1;
		}

		for (int j = 0; j < 4; j++)
		{
			bool b = false;
			int sum = 0;

			for (int k = 0; k < 4; k++)
				if (a[k][j] == -1)
					b = true;
				else
					sum += a[k][j];

			if (b)
				if (sum == 3)
					sum = 4;
				else if (sum == 300)
					sum = 400;

			if (sum == 4)
				res = 0;
			if (sum == 400)
				res = 1;
		}

		bool b = false;
		int sum = 0;

		for (int j = 0; j < 4; j++)
			if (a[j][j] == -1)
				b = true;
			else
				sum += a[j][j];

		if (b)
			if (sum == 3)
				sum = 4;
			else if (sum == 300)
				sum = 400;

		if (sum == 4)
			res = 0;
		if (sum == 400)
			res = 1;

		b = false;
		sum = 0;

		for (int j = 0; j < 4; j++)
			if (a[j][3 - j] == -1)
				b = true;
			else
				sum += a[j][3 - j];

		if (b)
			if (sum == 3)
				sum = 4;
			else if (sum == 300)
				sum = 400;

		if (sum == 4)
			res = 0;
		if (sum == 400)
			res = 1;

		out << "Case #" << i + 1 << ": ";

		if (res == 0)
			out << "X won" << std::endl;
		else if (res == 1)
			out << "O won" << std::endl;
		else if (emp)
			out << "Game has not completed" << std::endl;
		else
			out << "Draw" << std::endl;
	}
}