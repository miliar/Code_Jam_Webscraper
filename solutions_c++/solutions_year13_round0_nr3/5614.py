#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	int probNum = 0;
	// Problem Num
	cin >> probNum;

	for(int i = 0; i < probNum; ++i)
	{
		__int64 lBoundary = 0;
		__int64 rBoundary = 0;
		int ans = 0;
		cin >> lBoundary >> rBoundary;

		const __int64 startNum = static_cast<int>(sqrt(lBoundary));
		for(__int64 n = startNum; n*n <= rBoundary; ++n)
		{
			const __int64 nSquare = n*n;
			if(nSquare < lBoundary) continue;

			stringstream ss;
			ss << nSquare;
			string nSquareStr = ss.str();
			int strLen = nSquareStr.length();

			stringstream sss;
			sss << n;
			string nStr = sss.str();
			int strLenN = nStr.length();

			bool bPalindrome = true;
		
			for(int j = 0; j <= strLenN/2 - 1; ++j)
			{
				if(nStr[j] != nStr[strLenN - j - 1])
				{
					bPalindrome = false;
				}
			}

			for(int j = 0; j <= strLen/2 - 1; ++j)
			{
				if(nSquareStr[j] != nSquareStr[strLen - j - 1])
				{
					bPalindrome = false;
				}
			}

			if(bPalindrome)
			{
				++ans;
			}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}

