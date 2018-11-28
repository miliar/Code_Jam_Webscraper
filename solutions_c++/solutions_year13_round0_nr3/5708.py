#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>
#include <cstdlib>
#include <math.h>
using namespace std;

#define REP_i(i, n) for(int i=0;i<n;i++)
#define rep_i(n) REP_i(i,n)
#define REP_j(j, n) for(int j=0;j<n;j++)
#define rep_j(n) REP_j(j,n)
#define REP_k(k, n) for(int k=0;k<n;k++)
#define rep_k(n) REP_k(k,n)

string IntToString(int number)
{
	ostringstream ss;
	ss << number;
	return ss.str();
}

bool CheckPalindrome(string str)
{
	int j=0, k=str.size()-1;

	//cout << k << endl;
	for(j=0;j<=k;j++)
	{
		//cout << "j " << j << " k " << k << endl;
		if(str[j] != str[k])
		{
			return false;
		}
		k--;
	}

	return true;
}

int main()
{
	int prob_num, start, last, count=0;

	cin >> prob_num;

	rep_i(prob_num)
	{
		cin >> start;
		cin >> last;
		
	//	cout << "start: " << start << endl;
		//cout << "last: " << last << endl;
		
		int dec_tmp = last;
		while(dec_tmp >= start)
		{
			string dec_str = IntToString(dec_tmp);

			// judge palindrome
		
			if (CheckPalindrome(dec_str))
			{
				//cout << "clear! 1" << endl;
				double s_dec_tmp = sqrt(static_cast<double>(dec_tmp));
				int dectest = static_cast<int>(s_dec_tmp);
				if (s_dec_tmp == static_cast<double>(dectest))
				{
					//cout << "clear! 2" << endl;
					 dec_str = IntToString(static_cast<int>(s_dec_tmp));

					if (CheckPalindrome(dec_str))
					{
						count++;
					}
				}
			}

			dec_tmp--;
		}

		cout << "Case #" << i+1 << ": " << count << endl;
		count = 0;
	}

	return 0;
}
