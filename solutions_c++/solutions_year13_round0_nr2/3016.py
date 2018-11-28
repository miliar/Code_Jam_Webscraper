#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

string str(int i) 
{
	char s[100];
	sprintf(s, "%d", i);
	return string(s); 
}

vector< vector<bool> > possible;
vector< vector<int> > lawn;

int main()
{
	int cases;
	cin >> cases;
	for(int cs = 0; cs < cases; ++cs)
	{
		string answer = "YES";

		int m, n;
		cin >> n >> m;

		lawn.resize(n);
		possible.resize(n);
		for(int i = 0; i < n; ++i) {
			lawn[i].resize(m);
			possible[i].resize(m);
		}

		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				cin >> lawn[i][j];
				possible[i][j] = false;
			}
		}

		// for all rows
		for(int i = 0; i < n; ++i) 
		{
			int maximum = 0;
			for(int j = 0; j < m; ++j) 
				if(lawn[i][j] > maximum) maximum = lawn[i][j];

			for(int j = 0; j < m; ++j) 
				if(lawn[i][j] == maximum) possible[i][j] = true;
		}

		// for all columns
		for(int j = 0; j < m; ++j)
		{
			int maximum = 0;
			for(int i = 0; i < n; ++i) 
				if(lawn[i][j] > maximum) maximum = lawn[i][j];

			for(int i = 0; i < n; ++i) 
				if(lawn[i][j] == maximum) possible[i][j] = true;
		}

		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				if(!possible[i][j]) {
					answer = "NO";
					goto endFor;
				}
			}
		}
		endFor:

		cout << "Case #" << cs+1 << ": " << answer << endl;
	}
	return 0;
}
