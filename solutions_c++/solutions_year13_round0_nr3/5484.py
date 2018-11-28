#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;

bool isPalindrome(long long n)
{
	vector<int> num;
	while (n)
	{
		num.push_back(int(n)%10);
		n = n/10;
	}
	
	vector<int>::iterator itrb = num.begin(), itre = num.end()-1;

	while (itrb < itre)
	{
		if (*itrb == *itre)
		{
			++itrb;
			--itre;
		}
		else
		{
			return false;
		}
	}

	return true;
}

int main()
{
	int testcase;
	cin >> testcase;
	long count;
	fstream file("FairAndSquare.txt", iostream::out);

	int tnum = 0;
	while (tnum < testcase)
	{
		long long n, m;
		cin >> n >> m;

		count = 0;
		file << "Case #" << tnum+1 << ": ";
		for (long long i = n; i <= m; ++i)
		{
			long long j = sqrt(long double(i));
			
			if (isPalindrome(j))
			{
				if (j*j == i)
				{
					if (isPalindrome(i))
					{
						++count;
					}
				}
			}
		}

		file << count << endl;
		++tnum;
		count = 0;
	}
}