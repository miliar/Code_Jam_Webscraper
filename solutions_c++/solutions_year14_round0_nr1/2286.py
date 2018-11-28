#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <fstream>
#include <stack>
#include <queue>
#include <set>
#include <string>
#include <iomanip>
#include <deque>

using namespace std;

#define PI 3.14159265358979323846

using namespace std;

void main()
{
	ifstream inp("E:\\Note\\Input.txt");
	cin.rdbuf(inp.rdbuf());
	ofstream outp("E:\\Note\\Output.txt");
	cout.rdbuf(outp.rdbuf());
	int t;
	cin >> t;
	for (int x = 0; x < t; x++){
		int line;
		cin >> line;
		line--;
		vector <int> v;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int q;
				cin >> q;
				if (i == line)
					v.push_back(q);
			}
		cin >> line;
		line--;
		int c = 0;
		int ans = -1;;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int q;
				cin >> q;
				if (i == line)
				{
					if (find(v.begin(), v.end(), q) != v.end()){
						ans = q;
						c++;
					}
				}
			}
		if (c == 0)
			cout << "Case #" << x+1 << ": Volunteer cheated!" << endl;
		else
			if (c == 1)
				cout << "Case #" << x+1 << ": " << ans << endl;
			else
				cout << "Case #" << x+1 << ": Bad magician!" << endl;

	}
}