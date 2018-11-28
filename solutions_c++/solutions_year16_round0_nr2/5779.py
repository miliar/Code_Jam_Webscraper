#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;


char flip(char &x)
{
	if (x == '+') { return '-'; }
	else { return '+'; }
}


void maneuver(vector<char> &v, int p)
{
	vector<char> temp;
	for (int i = p-1; i>=0 ; i--)
	{
		temp.push_back(flip(v[i]));
	}

	for (int j = 0; j < p;j++)
	{
		v[j] = temp[j];
	}

}





int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		// for every test case
		string s;
		cin >> s;
		vector<char>cakes;

		for (int k = 0; k < s.length(); k++)
		{
			cakes.push_back(s[k]);
		}
		int manu_count=0;
		for (int j=1; j<cakes.size(); j++)
		{
			char temp = cakes[0];
			if (temp != cakes[j])
			{
				// flip from 0 to j
				maneuver(cakes,j);
				manu_count++;
			}
		}
		
		if (cakes[0] == '-')
		{
			maneuver(cakes, cakes.size());
			manu_count++;
		}

		cout <<"Case #"<<i+1<<": "<<manu_count << endl;
	}

	return 0;
}