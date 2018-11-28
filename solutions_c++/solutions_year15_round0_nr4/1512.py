#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <set>
#include <list>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int x, r, c;
		cin >> x >> r >> c;
		cout << "Case #" << t << ": ";
		if(x == 1) cout << "GABRIEL";
		else if(x == 2)
		{
			if((r*c) % 2 == 1) cout << "RICHARD";
			else cout << "GABRIEL";
		}
		else if(x == 3)
		{
			if((r*c > 3) && (((r*c) % 3) == 0)) cout << "GABRIEL";
			else cout << "RICHARD";
		}
		else
		{
			if(r <= 2 || c <= 2 || r*c == 9) cout << "RICHARD";
			else cout << "GABRIEL";
		}
		cout << '\n';
	}
}