#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool isSquare(const unsigned long long& a)
{
	return (sqrt(long double(a)) == unsigned long long(sqrt(long double(a))));
}

bool isPalindrome(unsigned long long a)
{
	vector<char> digits;

	while (a > 0)
	{
		digits.push_back(a % 10);
		a /= 10;
	}

	bool isPal = true;

	for (int i = 0; i < digits.size() / 2; ++i)
	{
		if (digits[i] != digits[digits.size() - 1 - i])
		{
			isPal = false;
			break;
		}
	}

	return isPal;
}

int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T;

	fin >> T;

	for (int i = 0; i < T; ++i)
	{
		unsigned long long A, B;
		fin >> A >> B;

		unsigned long long smaller;
		smaller = ceil(sqrt(long double(A)));

		int counter = 0;
		int tmp;

		while ((tmp = pow(long double(smaller), 2)) <= B)
		{
			if (isSquare(tmp) == true)
			{
				if (isPalindrome(tmp) && isPalindrome(smaller))
				{
					counter++;
					cout << tmp << endl;
				}
			}
			smaller++;
			while (!isPalindrome(smaller))
			{
				smaller++;
			}
		}

		//for (unsigned long long i = A; i <= B; ++i)
		//{
		//	if (isSquare(i) == true)
		//	{
		//		if (isPalindrome(sqrt(long double(i))) == true)
		//		{
		//			if (isPalindrome(i))
		//			{
		//				counter++;
		//				//cout << i << endl;
		//			}
		//		}
		//	}
		//}

		fout << "Case #" << i + 1 << ": " << counter << endl;

	}

	fin.close();
	fout.close();

	system("pause");

	return 0;
}