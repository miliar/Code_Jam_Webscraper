#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int i = 0; i < T; i++)
	{
		string s;
		cin >> s;

		string res = "";
		res += s[0];

		for(int j = 1; j < s.length(); j++)
		{
			//char der = res[res.length() - 1];
			char izq = res[0];

			//cout << izq << endl;

			//Append derecha
			if(s[j] < izq)
			{
				res.push_back(s[j]);
			}

			//Append izquierda
			else
			{
				res = s[j] + res;
			}

		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}
}