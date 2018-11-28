#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	ofstream file("Ali.txt.txt");
	int t,l=1;
	cin >> t;
	while (t--){
		file << "Case #" << l << ": ";
		string s;
		int k;
		cin >> s>>k;
		int c = 0;
		bool n = true;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				c++;
				if (i > s.size() - k)
				{
					n = false;
					break;
				}
				else
				{
					int a = k;
					for (int j = i; a != 0; j++)
					{
						if (s[j] == '-')
						{
							s[j] = '+';
						}
						else
						{
							s[j] = '-';
						}
						a--;
					}
				}
			}
		}
		if (n)
		{
			file << c << endl;
		}
		else
		{
			file << "IMPOSSIBLE" << endl;
		}
		l++;
	}
	 system("pause");
}