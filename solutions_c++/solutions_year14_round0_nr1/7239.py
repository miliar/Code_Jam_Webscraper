#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

string solve()
{
	int x, y;
	int a[4][4], b[4][4];
	cin >> x;
	for(int i(0); i != 4; ++i)
		for(int j(0); j !=4; ++j)
			cin >> a[i][j];
	cin >> y;
	for(int i(0); i != 4; ++i)
		for(int j(0); j != 4; ++j)
			cin >> b[i][j];
	
	bool found(false);
	int ans;
	for(auto i : a[x - 1])
		for(auto j : b[y - 1])
			if(i == j)
				if(found)
					return "Bad magician!";
				else
				{
					found = true;
					ans = i;
				}
	if(found)
	{
		char str[10];
		sprintf(str, "%d", ans);
		return string(str);
	}
	else
		return "Volunteer cheated!";
}

int main()
{
	int t;
	cin >> t;
	for(int ci(1); ci <= t; ++ci)
		cout << "Case #" << ci << ": " << solve() << endl;
}
