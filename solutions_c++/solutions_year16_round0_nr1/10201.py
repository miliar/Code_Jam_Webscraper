#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		cout << "error" << endl;
		exit(-1);
	}

	ifstream in;
	ofstream out;
	in.open(argv[1]);
	out.open("outfile.txt");

	int line;
	int n, n2;
	int cnt;
	int check;
	in >> line;
	
	for (int i = 0; i < line; i++)
	{
		out << "Case #" << i + 1 << ": ";
		in >> n;
		cnt = 1;
		check = 0;
		if (n == 0)
		{
			out << "INSOMNIA" << endl;
			continue;
		}

		do {
			n2 = n * cnt++;
			for (int j = n2; j > 0; j /= 10)
			{
				check |= (1 << (j % 10));
			}
		} while (check != 0x3FF);

		out << n2 << endl;
	}

	in.close();
	out.close();

	return 0;
}