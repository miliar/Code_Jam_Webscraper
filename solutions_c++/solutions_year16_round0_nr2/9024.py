/*
ID: behdad.1
LANG: C++11
PROB: 
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <queue>
#include <deque>
#include <math.h>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <string.h>
#include <limits.h>
#include <time.h>
#include <complex>

#define For(i,a,b) for(int i = a; i < b; i++)
#define Fori(i,s) for(auto i = s.begin(); i != s.end(); i++)
#define roF(i,b,a) for(int i = b; i >= a; i--)
#define roFi(i,s) for(auto i = s.rbegin(); i != s.rend(); i++)
#define trace(x) cout<<#x<<": "<<x<<endl;
#define _ <<" :: "<<
#define allof(x) x.begin(),x.end()
#define X real()
#define Y imag()

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

ifstream fin("file.in");
ofstream fout("file.out");
 
int main()
{
	int t;
	cin >> t;
	For (j,1,t+1)
	{
		string s;
		cin >> s;
		fout << "Case #" << j << ": ";
		int c = 0;
		For(i,1,s.size())
			if(s[i] != s[i-1])
				c++;
		if(s.back() == '-')
			c++;
		fout << c << endl;
	}
}
