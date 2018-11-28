// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const int MAXN = 1e9;

bool is_v(char c)
{
	return (c == 'a' || c == 'i' || c == 'o' || c == 'u' || c == 'e');
}

bool check(string s, int n)
{
	int curr = 0;
	for(int i=0; i<s.size(); i++)
	{

			if (!is_v(s[i])) curr ++;
			if ( i >= n) curr -= !is_v(s[i-n]);
			if (curr == n)
				return true;
	}
	return false;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test=0; test<t; test++)
	{
		string l;
		int n;
		int result  = 0;
		cin >> l >> n;
		for(int i=0; i<l.size(); i++)
		{
			string s;
			for(int j=i; j<l.size(); j++)
			{
				s += l[j];
				result += check(s, n);
			}
		}
		cout << "Case #" << test+1 << ": " << result << endl;
	}

	return 0;
}
