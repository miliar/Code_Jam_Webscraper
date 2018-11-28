#include<iostream>
using namespace std;
#include<vector>
#include<string>

int r1, r2;

int g1[4][4], g2[4][4];

int main() 
{
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("Aout.txt", "wt", stdout);
	char buffer [50];
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cin >> r1;

		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> g1[i][j];
		cin >> r2;

		--r1, --r2;

		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> g2[i][j];

		int n[20] = {0};
		for(int i = 0; i < 4; ++i)
			n[g1[r1][i]]++, n[g2[r2][i]]++;

		vector<int> v;
		for(int i = 1; i <= 16; ++i)
			if(n[i] > 1)
				v.push_back(i);

		string ans = "";
		if(v.size() == 1)
		{
			sprintf (buffer, "%d", v[0]);
			ans = buffer;
		}
		else if(v.size() > 1)
		{
			ans = "Bad magician!";
		}
		else
		{
			ans = "Volunteer cheated!";
		}

		

		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
