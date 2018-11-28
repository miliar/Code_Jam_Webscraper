#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <math.h>
#include <stdlib.h>
#include <cstdlib>
#include <stdio.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
#include <map>
#include <set>
using namespace std;
const int O = 2e9;
const double E = 1e-9;
const double pi = 3.1415926536;
int DX[] = { 0, 0, -1, 1 };
int DY[] = { -1, 1, 0, 0 };

/*bool valid(int x,int y)
{
return ( (x>=0 && x<n) && (y>=0 && y<n) );
}
*/
int main()
{
	//ifstream cin("A-small-attempt0.txt");
	ofstream cout("A-small-attempt.txt");

	int t,cas=1;
	cin >> t;
	while (t--)
	{
		int n, ans = 0,prev=0;
		string s;
		cin >>n>> s;
		prev = s[0] - '0';
		for (int i = 1; i < s.size(); i++)
		{
			if (i>prev)
	
				ans += (i -prev), prev += (i-prev)+ (s[i]-'0');
					
			else
				prev += (s[i]-'0');
		}
		cout << "Case #" << cas++ << ": " << ans << endl;
	}

}