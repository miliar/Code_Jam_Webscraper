#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

bool isPalindrom(long long n)
{
	vector <int>  num;

	while (n != 0)
	{
		num.push_back(n % 10);
		n /= 10;
	}

	for (int i = 0; i < num.size() / 2; i++)
		if (num[i] != num[num.size() - 1 - i])
			return false;

	return true;
}

void main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");

	int T, A, B;
	in >> T;
	
	for (int k = 0; k < T; k++)
	{
		in >> A >> B;
		int count = 0;

		for (long long i = A; i <= B; i++)
			if (isPalindrom(i))
			{
				double sqrtI = sqrt(i);
				if (ceil(sqrtI) - floor(sqrtI) == 0)
					if (isPalindrom((long long)sqrtI))
						count++;
			}

		out << "Case #" << k + 1 << ": " << count << endl;
	}
}
