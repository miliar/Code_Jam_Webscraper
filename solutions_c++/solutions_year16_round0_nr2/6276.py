//////////////////////////////////////////////
//Author: Adrian Seitan: seitan.adi@gmail.com
//////////////////////////////////////////////

#include<bits/stdc++.h>

using namespace std;

int decide(string& ps)
{
	int res = 0;
	
	if (ps.size() == 1){if (ps.at(0) == '-') return 1; else return 0;}

	while (1)
	{
		int k = 1; bool changeVal = false;
		for (; k < ps.size(); k++)
		{
			if (ps.at(k - 1) != ps.at(k)) { changeVal = true; break; }
		}
		k--;

		if ((k == ps.size()-1 && ps.at(0) == '-'))
		{
			changeVal = true;
		}

		
		{
			if (changeVal)
			{
				string compareString = ps.substr(0,k+1);
				res++;
				for (int w = 0; w <= k; w++)
				{
					if (compareString.at(k - w) == '-')
						ps.at(w) = '+';
					else
						ps.at(w) = '-';
				}
			}
		}

		unsigned int j = 0;
		for (; j < ps.size(); j++){ if (ps.at(j) == '-') break; }
		if (j == ps.size()) return res;
	}

	return res;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int cases, writtenCase = 1;
	cin >> cases;
	while (--cases >= 0)
	{
		string strLine;
		cin >> strLine;
		cout << "Case #" << writtenCase++ << ": " << decide(strLine) << endl;
	}
	return 1;
}
