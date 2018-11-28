/*
PROG:test
LANG:C++
*/

//# include <iostream>
# include <fstream>
# include <cmath>
# include <vector>
# include <algorithm>
# include <math.h>
# include <time.h>
# include <string>
# include <string.h>
# include <map>
# include <queue>
# include <stack>
//int ay[] = {31,28,31,30,31,30,31,31,30,31,30,31};
using namespace std;

ifstream cin("file.in");
ofstream cout("file.out");

string s;

int t, n, san, num;

int main()
{
	cin >> t;
	for (int i=0; i<t; i++) {
		cin >> n >> s;
		san = 0, num = 0;
		for (int j=0; j<=n; j++) {
			if (san < j) num += (j - san), san = j;
			san += s[j]-48;
		}
		cout << "Case #" << i+1 << ": " << num << '\n';
	}
	
	return 0;
}
//1 1 0 0 0 1
