#include <iostream>
#include <string.h>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int main()
{
	long int T = 0;
	long long int N = 0;
	long long int out = 0;
	string test;

	bool b0 = false;
	bool b1 = false;
	bool b2 = false;
	bool b3 = false;
	bool b4 = false;
	bool b5 = false;
	bool b6 = false;
	bool b7 = false;
	bool b8 = false;
	bool b9 = false;

	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		b0 = false;
		b1 = false;
		b2 = false;
		b3 = false;
		b4 = false;
		b5 = false;
		b6 = false;
		b7 = false;
		b8 = false;
		b9 = false;

		cin >> N;
		out = N;
		//cout << "N = " << N << endl;

		for (int a = 1; ; a++)
		{
			test = std::to_string(out);

			for (int c = 0; c<test.length(); c++)
			{
				if (test[c] == '1')
					b1 = true;
				else if (test[c] == '2')
					b2 = true;
				else if (test[c] == '3')
					b3 = true;
				else if (test[c] == '4')
					b4 = true;
				else if (test[c] == '5')
					b5 = true;
				else if (test[c] == '6')
					b6 = true;
				else if (test[c] == '7')
					b7 = true;
				else if (test[c] == '8')
					b8 = true;
				else if (test[c] == '9')
					b9 = true;
				else if (test[c] == '0')
					b0 = true;
			}

			if (b1 && b2 && b3 && b4 && b5 && b6 && b7 && b8 && b9 && b0)
			{
				cout << "Case #" << i << ": " << out << endl;

				break;
			}

			if (N != 0)
			{
				out = N * (a + 1);
			}
			else
			{
				cout << "Case #" << i << ": INSOMNIA" << endl;

				break;
			}
			//cout << out << endl;
		}
	}
	getchar();
	getchar();
	return 0;
}
