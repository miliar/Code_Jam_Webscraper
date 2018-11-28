#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
using namespace std;
FILE *stream;
int main()
{
	freopen_s(&stream,"A-small-attempt0.in","r",stdin);
	freopen_s(&stream,"output.txt","w",stdout);
	int t;
	cin >> t;
	for (int c = 1; c <= t;++c)
	{
		int a1, a2;
		cin >> a1;
		a1--;
		vector <int> v(4);
		set <int> res1;
		for (int i = 0; i < 4; ++i)
		{
			cin >> v[0] >> v[1] >> v[2] >> v[3];
			if (i == a1)
			{
				for (int j = 0; j < 4; ++j)
					res1.insert(v[j]);
			}
		}
		int k = 0, res = 0;
		cin >> a2;
		a2--;
		for (int i = 0; i < 4; ++i)
		{
			cin >> v[0] >> v[1] >> v[2] >> v[3];
			if (i == a2)
			{
				for (int j = 0; j < 4; ++j)
				{
					if (res1.find(v[j]) != res1.end())
					{
						k++;
						res = v[j];
					}
				}
					
			}
		}
		if (k == 0)
		{
			cout << "Case #" << c << ": Volunteer cheated!\n";
			continue;
		}
		if (k == 1)
		{
			cout << "Case #" << c << ": "<<res<<"\n";
			continue;
		}
		cout << "Case #" << c << ": Bad magician!\n";
	}
	
	return 0;
}