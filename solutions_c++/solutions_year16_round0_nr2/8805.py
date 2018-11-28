#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
  	freopen("B-large.out", "w", stdout);
	int cases, flips;
	vector <string> stack(cases);
	cin >> cases;
	for(int i = 0; i < cases; i++)
	{
		cin >> stack[i];
		flips = 0;
		for(int z = 1; z < stack[i].size(); z++)
		{
			if(stack[i].substr(z, 1) != stack[i].substr(z - 1, 1))
			{
				flips++;
			}
		}
		if(stack[i].substr(stack[i].size() - 1, 1) == "-")
		{
			flips++;
		}
		cout << "Case #" << i + 1 << ": " << flips << endl;
	}
}

