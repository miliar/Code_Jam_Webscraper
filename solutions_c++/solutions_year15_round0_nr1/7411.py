#include <iostream>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	int count;
	int extras;
	int add;
	for(int i = 0; i < cases; i++)
	{
		count = 0;
		extras = 0;
		add = 0;
		string s;
		int m;
		cin >> m >> s;
		count += (int)s[0] - '0';
		for(int j = 1; j <= m; j++)
		{
			
			if (j <= count)
			{
				count = count + s[j] - '0';
				//cout << "count " << count << " j " << j << endl;
			}
			else if(j > count && s[j] - '0' > 0)
			{
				add = j - count;
				//cout << "add " << add << endl;
				extras = extras + add;
				count = j + s[j] - '0';
				//cout << "extras " << extras << " count " << count << " j " << j << endl;
			}
		}
		cout << "Case #" << i + 1 << ": " << extras << endl;
	}
}

