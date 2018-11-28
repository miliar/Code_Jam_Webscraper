#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <functional>
using namespace std;

#define MAX 1000

int main()
{
	int n;
	string s;
	int count = 0;
	bool flagMinus = false;
	freopen("B-large.in", "rt", stdin);
	freopen("Output", "wt", stdout);
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		cin >> s;
		for(int j = 0; j < s.length(); j++)
		{
			if(s[j] == '-' && flagMinus == false)
			{
				count++;
				flagMinus = true;
			}
			else if(j + 1 < s.length() && s[j] == '+' && s[j+1] == '-')
			{
				count += 2;
				flagMinus = true;
			}
		}
		printf("Case #%d: %d\n", i+1, count);
		count = 0;
		flagMinus = false;
	}
	return 0;
}