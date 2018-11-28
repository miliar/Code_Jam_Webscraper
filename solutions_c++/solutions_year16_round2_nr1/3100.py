#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int c[128];
const string DIGITS[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
const string ORD = "ZWUXFVORGE";
const string dd = "0246571389";
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, l, j;
	string s, result;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		result = "";
		cout << "Case #" << i << ": ";
		cin >> s;
		l = s.size();
		for(j = 0; j < 128; j++)
			c[j] = 0;
		for(j = 0; j < l; j++)
			c[s[j]]++;
		for(int k = 0; k < 10; k++)
		{
			int temp = c[ORD[k]];
			for(j = 0; j < temp; j++)
			{
				result += dd[k];
				for(int pp = 0; pp < DIGITS[dd[k] - '0'].size(); pp++)
					c[DIGITS[dd[k] - '0'][pp]]--;
			}
		}
		sort(result.begin(), result.end());
	    cout << result << endl;
	}
	return 0;
}
